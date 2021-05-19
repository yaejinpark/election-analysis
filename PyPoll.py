# In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# import datetime as dt
import csv
import os # Useful when I don't know the full path of a file

# print("The time right now is", dt.datetime.now())

# Assign a variable to load the election results file
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the analysis results file
file_to_save = os.path.join("analysis", "election_results.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty candidates dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# With 'with,' I don't have to keep opening and closing the data file to obtain data I need.
with open(file_to_load) as election_data:

# TODO: Perform analysis on election results

	# Read the file object with the reader function
	file_reader = csv.reader(election_data)

	# Print the headers row
	headers = next(file_reader)
	
	# Iterate through each row in the CSV file
	for row in file_reader:
		# 2. Add to the total vote count
		total_votes += 1

		# Get the candidate name from each row
		candidate_name = row[2]

		# Check if duplicate candidate name exists in the candidate options list
		if candidate_name not in candidate_options:
			# Add the candidate name to the list
			candidate_options.append(candidate_name)

			# Begin tracking each candidate's vote count
			candidate_votes[candidate_name] = 0

		# Add a vote to that candidate's count.
		candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
	
	# Print the final vote count to the terminal.
	election_results = (
		f"\nElection Results\n"
		f"-------------------------\n"
		f"Total Votes: {total_votes:,}\n"
		f"-------------------------\n")
	print(election_results, end="")

	# Save the final vote count to the text file.
	txt_file.write(election_results)
	
	# Iterate through the candidates list
	for candidate_name in candidate_votes:

		# Retrieve vote count of a candidate
		votes = candidate_votes[candidate_name]

		# Calculate the vote percentage
		vote_percentage = float(votes)/float(total_votes) * 100

		# Determine winning vote count and candidate
		if (votes > winning_count) and (vote_percentage > winning_percentage):
			# If true, set the votes as winning count, percentage as winning percentage, and candidate with said two data as winning candidate
			winning_count = votes
			winning_percentage = vote_percentage
			winning_candidate = candidate_name

		candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
		print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

		# Save the candidate results to the text file.
		txt_file.write(candidate_results)

	# Winning candidate summary
	winning_candidate_summary = (
	    f"-------------------------\n"
	    f"Winner: {winning_candidate}\n"
	    f"Winning Vote Count: {winning_count:,}\n"
	    f"Winning Percentage: {winning_percentage:.1f}%\n"
	    f"-------------------------\n")
	print(winning_candidate_summary)

	# Save winning candidate summary to text file
	txt_file.write(winning_candidate_summary)



