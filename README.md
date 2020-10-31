# PyPoll

## Overview of Election Audit: 
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest turnout.

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.0, Visual Studio Code, 1.49.3

## Election-Audit Results: 
-The Election-Audit Results can be found in the election_analysis.txt file.

The analysis of the election show that: 
-There were 369,711 votes cast in the election.
-The candidates were:
  -Charles Casper Stockham
  -Diana DeGette
  -Raymon Anthony Doane
-The candidate results were:
  -Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  -Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  -Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 
-The counties were:
  -Jefferson
  -Denver
  -Arapahoe
-The county results were:
  -Jefferson county received 10.5% of the voter turnout and 38,855 number of voters.
  -Denver county received 82.8% of the voter turnout and 306,055 number of voters.
  -Arapahoe countyreceived 6.7% of the voter turnout and 24,801 number of voters.
-The county with the largest turnout was:
  -Denver county, which received 82.8% of the votes and 306,055 number of voters.

## Election-Audit Summary: 
-The PyPoll.py script can be run with any csv data in other campaigns for state and local elections that follow the same three column format of the election_results.csv. The script can be modified for other csv data that contains more columns or less columns to extract data like candidate name, county name, party affliation, etc. from a particular row in the csv data so that the script can be run without errors. 
