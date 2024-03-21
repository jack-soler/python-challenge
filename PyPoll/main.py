import csv
import os

# Construct the path to the CSV file
csv_file = os.path.join("/Users", "jacksoler1", "Bootcamp Modules", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Open the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    csv_title = next(reader) # Saves csv title and skips that row
    header_fields = next(reader)  # Saves header fields and skips the header row

    votes = []
    for row in reader:
        votes.append(row[0])

total_votes = len(votes)

print(total_votes)
