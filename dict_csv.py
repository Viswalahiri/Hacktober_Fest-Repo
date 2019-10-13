#CSV module to perform operations on students.csv file
#os module to check if the file exist 
#re to validate the date format

import csv
import os
import re


if __name__ == "__main__":

    db = dict()

    b =  input("Enter Your Choice R = READ, A = APPEND, W = WRITE\n")
    if b == 'A':
        
        n = int(input("Count of Students to enter data\n"))
        for i in range(n):
            name = input("Enter name\n")
            dob = input("Enter Date of Birth format [DD-MM-YYYY]\n")
            db[name] = db.get(name, dob)
            if bool(re.match(("\d{1,2}-\d{1,2}-\d{4}"),dob)):
                with open("students.csv",'a') as csvfile:
                    csv_writer = csv.writer(csvfile, delimiter=",")
                    csv_writer.writerows(db.items())
            else:
                print("Enter Date is not in current format")

    elif b == 'W':

        print("Warning this will OVERWRITE all the DATA in STUDENTS.csv")
        ch = input("Countinue (Y/N)")

        if ch == 'y' or 'Y':
            n = int(input("Count of Students to enter data\n"))
            for i in range(n):
                name = input("Enter name\n")
                dob = input("Enter Date of Birth format [DD-MM-YYYY]\n")
                db[name] = db.get(name, dob)
                if bool(re.match(("\d{1,2}-\d{1,2}-\d{4}"),dob)):
                    with open("students.csv",'w') as csvfile:
                        csv_writer = csv.writer(csvfile, delimiter=",")
                        csv_writer.writerows(db.items())
                else:
                    print("Enter Date is not in current format")

    elif b == 'R':

        os.path.exists("students.csv")

        try:
            with open("students.csv",'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                for row in csv_reader:
                    print(row)

        except Exception as e:
            print("Not such file")


    else:
        print("Wrong Option")





