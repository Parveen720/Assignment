#create a CSV file
import csv
data=[['Name','Address','Mobile','Email'],
     ['Parveen','Jaipur','1234556','Parveenyadavpy231@gmail.com'],
      ['Riya','Jaipur','123456','riyaaggarwal@gmail.com'],
      ['yadav','Jaipur','2345','yadav@gamil.com']

      ]

with open('data1.csv','w',newline="") as file1:
    writer=csv.writer(file1)
    for x in data:
        writer.writerow(x)

with open('data1.csv','r') as file1:
    reader=csv.reader(file1)
    for x in reader:
        print(x)