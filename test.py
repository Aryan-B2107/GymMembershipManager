import mysql.connector
from flask import Flask, request, jsonify
from datetime import datetime
from data_fetcher import form_data_fetcher
import csv

def insert_into_db():
    new_data_path = r'D:\YoutubeContentPipeline\Gym Membership Manager\google_api\membership_data.csv'

    csv_data = []
    with open(new_data_path, mode='r') as file:
        csvFile = csv.reader((file))
        for lines in csvFile:
            del lines[1]
            csv_data.append(lines)





    for i in range(len(csv_data)):
        array = ['ashok.balikondwar@ubs.com', 'Aryan Balikondwar', '657356723567', 'Fat Loss', 'Sargam', '3', '2025-07-30', '6256']

        email = str(csv_data[i][0])
        full_name = str(csv_data[i][1])
        phone = int(csv_data[i][2])
        program = str(csv_data[i][3])
        locality = str(csv_data[i][4])
        months = int(csv_data[i][5])
        start_date = datetime.strptime(csv_data[i][6], "%Y-%m-%d").date()
        fees = int (csv_data[i][7])
        print(email, full_name, phone, program, locality, months, start_date, fees)

if __name__ == "__main__":
    insert_into_db()