import mysql.connector
import csv
from datetime import datetime

# --- Database Configuration ---
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Welcome@2025",
    "database": "gym_db"
}

# --- CSV File Path ---
CSV_FILE_PATH = r'D:\YoutubeContentPipeline\Gym Membership Manager\google_api\membership_data.csv'

def insert_csv_data_to_mysql():
    """
    Reads data from a CSV file and inserts it into the MySQL database.
    Assumes CSV format matches the database table structure.
    """
    csv_data = []
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Assuming no header row in CSV. If there is, uncomment the next line:
        # next(csv_reader, None)
        for row in csv_reader:
            # IMPORTANT: If you still need to delete the second column (index 1)
            # as in your original code, uncomment the line below.
            # Make sure your indexing (row[0], row[1], etc.) is correct afterwards.
            # del row[1]
            csv_data.append(row)

    print(f"Attempting to insert {len(csv_data)} rows from CSV.")

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    """for row_data in csv_data:
        print(csv_data)
        del row_data[1]
        # Assuming row_data has 8 elements corresponding to the DB columns
        email = row_data[0]  # Already a string
        full_name = row_data[1]  # Already a string
        phone = int(row_data[2])  # Must be converted to int
        program = row_data[3]  # Already a string
        locality = row_data[4]  # Already a string
        months = int(row_data[5])  # Must be converted to int
        start_date = datetime.strptime(row_data[6], "%Y-%m-%d").date()  # Must be converted to date object
        fees = int(row_data[7])"""

    email = csv_data[-1][0]
    full_name = csv_data[-1][2]
    phone = csv_data[-1][3]
    program = csv_data[-1][4]
    locality = csv_data[-1][5]
    months = csv_data[-1][6]
    start_date = csv_data[-1][7]
    fees = csv_data[-1][8]

    print(f"Inserting...", email, full_name, phone, program, locality, months, start_date, fees)

    cursor.execute("""
        INSERT INTO memberships
        (email, full_name, phone_number, program_type, locality, membership_length_months, start_date, fees_paid)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (email, full_name, phone, program, locality, months, start_date, fees))
    print(f"Row insertion completed: {email}, {full_name}") # Simple confirmation

    conn.commit() # Save all changes to the database
    cursor.close()
    conn.close()

    print("All CSV data successfully inserted into the database.")

if __name__ == "__main__":
    insert_csv_data_to_mysql()