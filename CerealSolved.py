#import modules
import os
import csv

#open the csv
cerealCSV = os.path.join(".","resources","cereal.csv")
with open(cerealCSV, "r", encoding="UTF-8") as csvfile:
    #create my csv reader
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    print(f"The header is: {csvheader}")
    #iterate rows (for loops)
    for row in csvreader:
        #if statement (if teh cereal contains 5 or more grams of fiber, print)
        if float(row[7]) >= 5:
            #print row ifcondition meets
            print(row)