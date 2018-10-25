#Import the OS module
import os

#Import module for reading CSV files
import csv

#Specify the file path of the csv file we want to work with
csvpath=os.path.join('Budget_Data.csv')

#Define a function that will collect requested data 

def getbudgetdata(BudData):
    
    #Total number of months will be found by adding total number of months together
    Months = 0
    for Month in BudData:
        Months += Month
    return Months
    print('something')
      
#Open the csv file
with open(csvpath , newline='') as budfile:
    
    #Use the csv reader to specify the variable that holds the file and the delimiter
    csvreader = csv.reader(budfile, delimiter=',')
    
    #Skip the header row
    header = next(csvreader)

    for row in csvreader:
        getbudgetdata(row)
    
    
    #Net amount of profits and losses
    NetPL = int(BudData[1])
    

#Open the csv file
with open(csvpath , newline='') as budfile:
    
    #Use the csv reader to specify the variable that holds the file and the delimiter
    csvreader = csv.reader(budfile, delimiter=',')
    
    #Skip the header row
    header = next(csvreader)
    
    
    #------------------------------------------------------------------------------
    #TOTAL NUMBER OF MONTHS
    #------------------------------------------------------------------------------
    #Use sum function with generator expression to count number of rows which should equal number of months
    Total_Months = sum(1 for row in csvreader)
    
    #print number of rows
    print('There are ' + str(Total_Months)+' months')
    
    #------------------------------------------------------------------------------
    #TOTAL NET AMOUNT OF PROFIT/LOSSES
    #------------------------------------------------------------------------------
    #Use sum function to sum profit loss column
    #Use index to define variable for profit/loss column in csv file
    ProfLoss = sum(int(row[1]) for row in csvreader)
    print('The net prof/less is ' + str(ProfLoss))
    
    
    #dummy variable created for test
    dummyv = 'Jan-2010'
    
    #test to see if i messed up
    for row in csvreader:
        if row[0]== dummyv:
            print (row[1])
            break
        
            
        
    