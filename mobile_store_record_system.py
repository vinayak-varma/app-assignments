import csv
import argparse

p=argparse.ArgumentParser(
    description='Mobile Store Record System')
p.add_argument('filename',
               help='Mobile CSV file')
args=p.parse_args()
try:
    records=[]
    with open(args.filename, 'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            records.append(row)
    print("All Mobile Records:")
    for row in records:
        print("Brand:", row['Brand'])
        print("Model:", row['Model'])
        print("Price:", row['Price'])
        print("RAM:", row['RAM'])
        print("Storage:", row['Storage'])
        print()
    brand=input("Enter Brand Name to search: ")
    found=False
    for row in records:
        if row['Brand'] == brand:
            print("Mobile Found!")
            print("Brand:", row['Brand'])
            print("Model:", row['Model'])
            print("Price:", row['Price'])
            print("RAM:", row['RAM'])
            print("Storage:", row['Storage'])
            print()
            found=True
    if not found:
        print("Mobile not found")
except FileNotFoundError:
    print("Error: CSV file not found")