#PyPoll Script

#Import Dependencies
import csv

# Define variables
total_votes = 0
candidate_votes = {}

# Access and read CSV file
with open('PyPoll/Resources/election_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:   
        # Count total votes
        total_votes += 1 
        # Count votes for each candidate
        if row['Candidate'] in candidate_votes:
            candidate_votes[row['Candidate']] += 1
        else:
            candidate_votes[row['Candidate']] = 1
            
# Determine election winner
winner = max(candidate_votes, key=candidate_votes.get)

# Calculate and format each candidate's vote percentage
candidate_percentages = {candidate: (votes/total_votes)*100 for candidate, votes in candidate_votes.items()}

# Save results to Analysis file
with open("Analysis.txt", "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")
    outfile.write("\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")
    outfile.write("\n")
    for candidate, votes in candidate_votes.items():
        outfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")
    outfile.write("\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")