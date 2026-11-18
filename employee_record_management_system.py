import csv
import argparse

p=argparse.ArgumentParser(
    description='Employee Record Management System')
p.add_argument('filename',
               help='Employee CSV file')
args=p.parse_args()
try:
    records=[]
    with open(args.filename, 'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            records.append(row)
    print("All Employee Records:")
    for row in records:
        print("ID:", row['EmployeeID'])
        print("Name:", row['Name'])
        print("Department:", row['Department'])
        print("Salary:", row['Salary'])
        print()
    emp_id=input("Enter Employee ID to search: ")
    found=False
    for row in records:
        if row['EmployeeID']==emp_id:
            print("Employee Found!")
            print("ID:", row['EmployeeID'])
            print("Name:", row['Name'])
            print("Department:", row['Department'])
            print("Salary:", row['Salary'])
            found=True
            break
    if not found:
        print("Employee not found")
except FileNotFoundError:
    print("Error: CSV file not found")