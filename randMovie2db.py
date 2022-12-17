import csv
from os import replace
import random
import re
import os

mega_dict = []
op_sys = os.name
line = "-----------------------------"

# Opens the watchlist csv file and reads it's content
with open('WATCHLIST.csv', newline='', encoding='ISO-8859-1') as f:
    reader = csv.reader(f, quotechar='"', delimiter=',')
    # We will store the header and use it's values as the keys to our object
    # which will contain all the details of a given movie.
    header = next(reader)
    iter = 0
    # Breaks down the content of the file to separate movies by rows
    for movie_item in f:        
        # The genres are separated with commas inside quotes.
        # We need to replace the commas so it won't break when we come to splitting
        # the details that are also separated by commas
        genre = str(re.findall('"([^"]*)"', movie_item))
        genre = genre.replace("'", '"').replace("[", "").replace("]", "")
        genreRefined = genre.replace(",", " -")
        genreRefined = str(genreRefined).replace("'", "").replace("[", "").replace("]", "")
        movie_item.replace(genre, genreRefined)
        # Now it's time to split the rows, and replace the genre with the reformatted one.
        movie = movie_item.split(",")    
        movie[11] = genreRefined
        movie_object = {} 
        # And push them into an key/value pair object
        # We get the keys from the csv's header that we stored earlier
        # and assign them to the values of the movie's description
        for key in header: 
            for value in movie: 
                movie_object[key] = value 
                movie.remove(value) 
                break  
        # Now we push the combined objects to a dictionary that will contain
        # all the movies.
        mega_dict.insert(int(movie_object["Position"]), movie_object)
  
# A movie gets chosen randomly from the large dictionary
chosen_one = random.choice(mega_dict)

# We must calculate the length that's originally is given in minutes
# to a hour:minute format
hours = chosen_one["Runtime (mins)"]
if hours == "":
    hours = 0
hours = str(int(float(hours) // 60))
separator = ":" 
minutes = chosen_one["Runtime (mins)"]
if minutes == "":
    minutes = 0
minutes = str(int(float(minutes) % 60))
if int(minutes) < 10:
    minutes = "0" + str(minutes)
chosen_one_length = hours + separator + minutes

# It prints the result
print()
print(line)
print()
print("Title: ", chosen_one["Title"])
print("Year:  ", chosen_one["Year"])
print("Genre: ", chosen_one["Genres"].replace('"', ""))
print("Length:", chosen_one_length )
print("Link:  ", chosen_one["URL"])
print()
print(line)
print()


# import mysql.connector
# from subprocess import PIPE, Popen, call

# tempDatabase = mysql.connector.connect(
# 			     host="127.0.0.1",
# 				 database="guardian3",
# 				 user="alice",
# 				 passwd="R4j4l3l4tt3",
#                  auth_plugin='mysql_native_password'
#                  )
# tempCursor = tempDatabase.cursor()		

# tempMovieQuery = "UPDATE TempTable SET temporary_data = %s WHERE id = %s"
# tempMovieValue = (chosen_one, "5")
# tempCursor.execute(tempMovieQuery, tempMovieValue)
# dbTemporary.commit()
# print(tempCursor.rowcount, "record(s) affected")

import mysql.connector
import json

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="alice",
  password="R4j4l3l4tt3",
  database="guardian3"
)

mycursor = mydb.cursor()

chosen_one = json.dumps(chosen_one)
print("dumping: " + chosen_one)
sql = "UPDATE TempTable SET temporary_data = %s WHERE id = %s"
val = (chosen_one, 5)
mycursor.execute(sql, val)
mydb.commit()

try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))




# # Clears the command line, depending on the operating system type
# if op_sys == "nt":
#     os.system("cls")
# else:
#     os.system('clear')

