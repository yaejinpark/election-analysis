# In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import datetime as dt
import csv
import random
import numpy
import os # Useful when I don't know the full path of a file

# print("The time right now is", dt.datetime.now())

# Open the election results file
# file_path = "resources/election_results.csv"
file_path = os.path.join("resources", "election_results.csv")
# election_data = open(file_path,"r")

# With 'with,' I don't have to keep opening and closing the data file to obtain data I need.
with open(file_path) as election_data:
	print(election_data)

# TODO: Perform analysis on election results

# Close elction file
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()