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

while True:    
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

    # Asks the user if (s)he wants to repeat the cylce or quit
    user_input = input('[R]epeat or [Q]uit? \n \n')

    # Clears the command line, depending on the operating system type
    if op_sys == "nt":
        os.system("cls")
    else:
        os.system('clear')
    # Executes the user's choice
    if (user_input.lower() == "q") or (user_input.lower() == "quit"):
        break
