## Coder-of-Delhi
# Using pure Python, this project builds a recommendation system that suggests friends and pages based on mutual connections and shared interests from JSON data, without using any external libraries.

## Step - 1
# Load the json file codebook_data.json

## Step - 2
# Read and Display the Data using read_and_display_data.py file
# Steps:
      1. Save the JSON data in a file (codebook_data.json ).
      2. Read the JSON file using Python.
      3. Print user details and their connections.
      4. Print available pages.
      
## Step - 3
# Cleaning the data using clean_data.py
# steps:
     1. Handle missing values
     2. Remove duplicate or inconsistent data
     3. Standardize the data forma

## Step - 4
# Build a ‘People You May Know’ feature! using people_you_may_know.py
# steps:
     1. Finds all friends of a given user.
     2. Identifies mutual friends between non-friends.
     3. Ranks recommendations by the number of mutual friends.

## Step - 5
# Build a ‘Pages You Might Like’ feature! using pages_you_might_like.py
# steps:
     1. Maps users to pages they have interacted with.
     2. Identifies pages liked by users with similar interests.
     3. Ranks recommendations based on common interactions


