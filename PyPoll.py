import csv
import os 


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")

# # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")


# Read the file object with the reader function.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)


# Read and print the header row.
    headers = next(file_reader)
    print(headers)