#PYPOLL
# =============================================================================
# #The total number of votes cast
# #A complete list of candidates who received votes
# #The percentage of votes each candidate won
# #The total number of votes each candidate won
# #The winner of the election based on popular vote.
# 
# =============================================================================

#Import the OS module
import os

#Import module for reading CSV files
import csv

#Specify the file path of the csv file we want to work with
csvpath=os.path.join('election_data.csv')
    
#Open the csv file
with open(csvpath , newline='') as elecfile:
    
    #Use the csv reader to specify the variable that holds the file and the delimiter
    csvreader = csv.reader(elecfile, delimiter=',')
    
    #Skip the header row
    header = next(csvreader)
     
    #Create empty list to hold all candidate names
    Cands = []

    #Create list of each vote with candidate name
    for row in csvreader:
         Cands.append(row[2])
 
    #Calculate total votes using list comprehension
    VoteTotLC = sum(1 for votes in Cands)
    
    #Print total votes
    print(f"Total Votes: {VoteTotLC}")
    
    #Define list which will store Candidate Names and their number of votes
        #Use set to group entire list (Cands) by candidate names
    CandVotes = [[name,
                  Cands.count(name)/VoteTotLC,
                  Cands.count(name)] for name in set(Cands)]

    #Print all candidate names, % of votes received and number of votes received 
    for names in CandVotes:
        print(f"{names[0]} {names[1]:.2%} ({names[2]})")
    
    #Define variable to find and hold winning vote percentage
    WinnerPercent = max([name[1] for name in CandVotes])
    
    #Find name of winning candidate using winning % as an index in CandVotes list
    for names in CandVotes:
        if names[1] == WinnerPercent:
            print(f"Winner: {names[0]}")
            #Define variable for Winner to reference in print out file
            Winner = names[0] 
    
    #print voting results
#    print(CandVotes)
#    print(CandVotesDict)
#    print(CandPercDict)
    
#-------------------------------------------
#WRITE TXT FILE WITH RESULTS
#-------------------------------------------
#Specify file path to write to
output_file = open("PyPollResults.txt","w")

#Print total results to text file

output_file.write(f'----------------------------\n')
output_file.write(f'Total Votes: {VoteTotLC}\n')
output_file.write(f'----------------------------\n')

#Print candidate stats
for names in CandVotes:
    output_file.write(f"{names[0]} {names[1]:.2%} ({names[2]})\n")
    
output_file.write(f'----------------------------\n')
output_file.write(f'Winner:{Winner}\n')    
output_file.write(f'----------------------------\n')

output_file.close()