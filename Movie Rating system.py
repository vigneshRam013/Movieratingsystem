#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
movies = {
    'Id':[],
    'Title':[],
    'year' :[],
    'Rating':[]
          }
movies_df = pd.DataFrame(movies)
movies_df.head()


# In[ ]:


#Welcome Message
print("Welcome to the movie rating system")

#Writing a csv file 
a = open("movie_rating.csv", "w")

#Building UI
print("The list of Available options are: ")
print("1.Add a Movie \n2.Change Rating \n3.Remove Movies\n4.Print Movies \n99. Exit")

#Getting user from input and performing operations as required.
while True:
    _input = int(input("Please make a selection: "))
    if _input == 1:
        add_movie = {'Id': (str(input("Please enter the movie Id: "))),
                  'Title': (str(input("Please enter the name of the Movie: "))),
                  'year': (int(input("Please enter the Year of release "))),
                  'Rating': (int(input("How much rating for the movie? ")))}
        movies_df = movies_df.append(add_movie, ignore_index = True)
        print("Movie Added Successfully")
        print(movies_df)
    elif _input == 2:
        change_rating = {'Id': (str(input("Please enter the movie Id: "))),
                         'Rating': (int(input("How much rating for the movie? ")))}
        movies_df['Id'] = movies_df['Id']. replace([''], ['change_rating'])
        print("Rating changed Successfully")
        print(movies_df)
    elif _input == 3:
        delete_movie = {'Id': (str(input("Please enter the movie Id: ")))}
        movies_df = movies_df.drop(delete_movie)
        print("Movie removed successfully")
        print(movies_df)
    elif _input == 4:
        print(movies_df)
    elif _input == 99:
        break
    else:
        print("Please enter an appropriate Value from 1 to 5")
        
    


# In[ ]:




