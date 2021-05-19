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

## Election Audit Summary
Though it seemed like a huge task to analyze the results at first, breaking the task down into smaller steps helped me think about how to write the code so that it can perform the analysis on similarly structured election data files. First, none of the candidate names or county names are hardcoded - this code simply extracts them from data rows by storing them inside arrays, without duplicates. Then the code creates a dictionary with said list and keeps a counter for the vote each time the for-loops iterate through a row for each candidate and county with the if-statement that sets the condition of when to count the vote. Here are a couple of examples that prove my case.

### Example 1 - A New Challenger Approaches
I altered the CSV file's second row so that there is a strange vote for a strange candidate as the following image:



## Other Observations
Naming convention