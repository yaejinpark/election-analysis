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

# Assign a variable to load the election results file
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the analysis results file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# election_data = open(file_path,"r")

# With 'with,' I don't have to keep opening and closing the data file to obtain data I need.
with open(file_to_load) as election_data:

# TODO: Perform analysis on election results

	# Read the file object with the reader function
	file_reader = csv.reader(election_data)

	# Print the headers row
	headers = next(file_reader)
	print(headers)

	