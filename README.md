# Election Audit - Berkeley DA
Yae Jin Park\
Module 3: PyPoll with Python

## Assignment Overview
Through this project's mock election audit, I was able to fully comprehend how to analyze data from a given CSV file and learn the basics of Python's logical operators. I was given a CSV file with that contains information on voter ID number, voter's county/district, and the name of voter's candidate of choice. My task was to parse through each row of the CSV file (where a single row represented a set of data that contains the voter information mentioned), count the votes, and find which candidate got the most votes and which county had the largest turnout.

The next sections will show and explain my results from finishing the analysis task.

## Election Audit Results
I was able to obtain the desired election results in two forms: output from running the Python code in the terminal and output text file in which I wrote the results of the analysis. The first image shows the output in the terminal, and the second of the text file.

* ![Election Audit Results in the Terminal](https://github.com/yaejinpark/election-analysis/blob/main/resources/deliverable1.PNG)
* ![Election Audit Results in the Output Text File](https://github.com/yaejinpark/election-analysis/blob/main/resources/deliverable2.PNG)

As shown in the two images above, the output results are the same content-wise and therefore proves that my analysis Python code worked. 

Result Summary:
- Total votes cast in this election: 369,711\
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)\
- County with the largest turnout: Denver\
- Breakdown of the number of votes and the percentage of the total votes each candidate received:
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)\
- Winning candidate and their data:
* Winner: Diana DeGette
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

## Election Audit Summary
Though it seemed like a huge task to analyze the results at first, breaking the task down into smaller steps helped me think about how to write the code so that it can perform the same analysis on similarly structured election data files. First, none of the candidate names or county names are hardcoded - this code simply extracts them from data rows by storing them inside arrays, without duplicates. Then the code creates a dictionary with said list and keeps a counter for the vote each time the for-loops iterate through a row for each candidate and county with the if-statement that sets the condition of when to count the vote. Here are a couple of examples that prove my case.

### Example 1 - A New Challenger Approaches
What if I the data had one more candidate? Would the code successfuly register this candidate's data? I altered the CSV file's second row so that there is a strange vote for a strange candidate as the following image:

![Strange Candidate](https://github.com/yaejinpark/election-analysis/blob/main/resources/whothis.png)

Since I didn't hardcode any names, this candidate should appear in the results when I run the code... and he did (though he only received one vote)!

![Strange Result](https://github.com/yaejinpark/election-analysis/blob/main/resources/ex1results.png)

### Example 2 - More Candidates, More Votes
What if example 1 worked just because the new challenger only had one vote? I made more changes to the CSV file so that the new challenger has more votes (repeating voter id indicates election fraud, but let's ignore that for now). This time, the new candidate got a significant amount of votes (a whopping 9,999 votes) to alter the percentage of the votes each candidate received. If my code works correctly, the percentage for each candidate should be different from what is shown in the audit results section.

![More Votes](https://github.com/yaejinpark/election-analysis/blob/main/resources/somanyvotes.png)
![More Votes Results](https://github.com/yaejinpark/election-analysis/blob/main/resources/ex2results.png)

So it seems that for any new candidate or how many number of votes for said candidate is recorded, my analysis code is functioning properly. If I could use more modules or a database, maybe I can upgrade the code to take in only unique voter IDs for counting fairly.