counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Pase are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
counties
for county in counties:
    print(county)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties_dict

#get keys of dictionary
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#get values of dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))

#get key-value pairs from dictionary
#for key, value in dictionary_name.items():
    #print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

#get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
#use range() function to do the above
for i in range(len(voting_data)):

      print(voting_data[i])
#get values from list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#get registered voters aka values from dict
for county_dict in voting_data:

     print(county_dict['registered_voters'])
#get only county name/keys
for county_dict in voting_data:
    print(county_dict['county'])

#f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#f strings and dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))

message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

counties_dict
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
voting_data
for county, voters in voting_data.items():
    print(f"{county} county has {voters} registered voters.")


import csv
dir(csv)

dir(str)

import random
dir(random)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results_copy.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
import os
dir(os)
dir(os.path)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#Write in new text file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

#Same thing but using "with" instead of open/close
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    ##txt_file.write("Hello World")
  
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

##CHECKPOINT
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results_copy.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    
    #RETRIEVE FIRST ITEM FROM A ROW
    #for row in file_reader:
        #print(row[0])
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)
    

   #CHECKPOINT2 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)