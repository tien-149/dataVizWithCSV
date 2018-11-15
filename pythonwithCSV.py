import csv
import numpy as np
import matplotlib.pyplot as plt 

#figure out what we want to use
categories = [] #these are column headers in the csv file
installs = [] #this is the installs row
ratings = [] #this is the ratings row

with open ('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		#move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: #this will be text, not data
			print('putting categories into a separate array')
			categories.append(row) #push the text into this array
			line_count += 1 # increament the line count for the next loop
		else:
			ratingsData = row[2]
			ratingsData = ratingsData.replace("NaN", "0")
			ratings.append(float(ratingsData)) #int will turn a string (piece of text) in to a number
			#print('pushing ratings data into the ratings array')
			installData = row[5]
			installData = installData.replace(",","") #get rid of the commas

			installs.append(np.char.strip(installData, "+")) #get rid of the tr
			line_count += 1


# Get some value that we can work with
#Howmany ratings are 4+
# How many ratings are below 2
# How many are in the middle
np_ratings = np.array(ratings) # turn plain Python list into a NUmpy array
popular_apps = np_ratings > 4
print("Popular apps", len(np_ratings[popular_apps]))


percent_popular = int(len(np_ratings[popular_apps]) / len(np_ratings) * 100)
print(percent_popular)

unpopular_apps = np_ratings < 4
print("Unpopular apps", len(np_ratings[unpopular_apps]))

percent_unpopular = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(percent_unpopular)

kinda_popular = int(100 - (percent_popular + percent_unpopular))
print(kinda_popular)


labels = "Sucks", "Meh", "Love it!"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ('yellowgreen', 'lightgreen', 'lightskyblue')
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Do we love us sone apps?")
plt.xlabel("User Ratings - App Installs (10000+ apps")
plt.show()


#print ('processed', line_count, 'lines of data')
print(categories)
print('first row of data', installs[0])
print('last row of data', installs[-1])


