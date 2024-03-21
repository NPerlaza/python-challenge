import csv

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Open the CSV file
with open('/Users/NP/Documents/python-challenge/PyPoll/Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    # Loop through each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the results
results = []
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("\n".join(results))
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open('/Users/NP/Documents/python-challenge/PyPoll/analysis/results.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write("\n".join(results) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")