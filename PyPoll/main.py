import csv
import os

# Construct the path to the CSV file
csv_file = os.path.join("/Users", "jacksoler1", "Bootcamp Modules", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Open the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header_fields = next(reader)  # Saves header fields and skips the header row

    votes = [] #creates a list of votes
    ccs_count = 0 #starts counter for first contestant
    dg_count = 0 #starts counter for second contestant
    rad_count = 0 #starts counter for third contest
    for row in reader: #goes through each row
        votes.append(row[2]) #puts everything in the third column in a list
    for i in range(0, len(votes)): #for loop in votes list
        if votes[i] == 'Charles Casper Stockham':
            ccs_count = ccs_count + 1 #counts votes for first contestant
        if votes [i] == 'Diana DeGette':
            dg_count = dg_count + 1 #counts votes for second contestant
        if votes [i] == 'Raymon Anthony Doane':
            rad_count = rad_count + 1 #counts votes for third contestant
    if dg_count > ccs_count and dg_count > rad_count:
        winner = 'Diana DeGette' 
    elif ccs_count > dg_count and ccs_count > rad_count:
        winner = 'Charles Casper Stockham' 
    else:
        winner = 'Charles Casper Stockham' #determines winner
        

total_votes = len(votes)
percent_ccs = (ccs_count/total_votes)*100
percent_dg = (dg_count/total_votes)*100
percent_rad = (rad_count/total_votes)*100 #determines percentages

percent_ccs = round(percent_ccs, 3)
percent_dg = round(percent_dg, 3)
percent_rad = round(percent_rad, 3) #rounds percentages


print('Election Results')
print("Total Votes:", total_votes)
print("Charles Casper Stockham:",percent_ccs, "% (",ccs_count,")")
print("Diana DeGette:",percent_dg, "% (",dg_count,")")
print("Raymond Anthony Doane:",percent_rad, "% (",rad_count,")")
print("Winner:", winner) #prints