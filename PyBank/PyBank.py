#Import the OS module
import os

#Import module for reading CSV files
import csv

#Specify the file path of the csv file we want to work with
csvpath=os.path.join('Budget_Data.csv')

#Open the csv file
with open(csvpath , newline='') as budfile:
    
    #Use the csv reader to specify the variable that holds the file and the delimiter
    csvreader = csv.reader(budfile, delimiter=',')
    
    #Skip the header row
    header = next(csvreader)
    
    #Create empty list to hold profit/loss for each month
    ProfLoss = []
    #Create empty list to hold months
    MonthL = []
    
    #Set variables and initial count of month total and profit/loss total to 0
    Months = 0
    NetPL = 0
    
    for month in csvreader:
        #Add 1 to month counter for each row of data
        Months += 1
        
        #Add monthly profit/loss to overall profit and loss variable
        NetPL += int(month[1])
        
        #Add monthly profit/loss values to profit/loss list
        ProfLoss.append(int(month[1]))
        
         #Add months to month list
        MonthL.append(month[0])
        
    #Create a list of profit and loss differences between each consecutive month 
    PLMonthDiff= [(ProfLoss[x+1] - ProfLoss[x]) for x in range(len(ProfLoss)-1)]

    #Average of all values in profit loss diff list
    averagePL = sum(PLMonthDiff)/len(PLMonthDiff)
 
    #Greatest increase and decrease in profits and month that they occured
    ProfMax = max(PLMonthDiff)
    ProfMin = min(PLMonthDiff)    

    #Retrieve index number of months with greatest profit increase and decrease
    PMaxMonInd = PLMonthDiff.index(ProfMax) + 1
    PMinMonInd = PLMonthDiff.index(ProfMin) + 1
        
    #Define months where greatest profit increase and decrease occurred
    MaxMonth = MonthL[PMaxMonInd]
    MinMonth = MonthL[PMinMonInd]    
    
    #Print results to terminal
    print(f'Total Months: {Months}')
    print(f'Total: ${NetPL}')    
    print(f'Average Change: ${averagePL:.2f}')
    print(f'Greatest Increase in Profits: {MaxMonth} (${ProfMax})')  
    print(f'Greatest Decrease in Profits: {MinMonth} (${ProfMin})')    

#-------------------------------------------
#WRITE TXT FILE WITH RESULTS
#-------------------------------------------
#Specify file path to write to
output_file = open("PyBankResults.txt","w")

#Print results to text file
output_file.write(f'Total Months: {Months}\n')
output_file.write(f'Total: ${NetPL}\n')    
output_file.write(f'Average Change: ${averagePL:.2f}\n')
output_file.write(f'Greatest Increase in Profits: {MaxMonth} (${ProfMax})\n')  
output_file.write(f'Greatest Decrease in Profits: {MinMonth} (${ProfMin})\n')    

output_file.close()



    

    
   