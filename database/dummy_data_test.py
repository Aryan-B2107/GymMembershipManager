import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('en_IN')

programs = ['fatloss', 'muscle gain', 'maintenance']
localities = [
    'Sarang',
    'Madhuvanti',
    'Shubhakalyan',
    'Asawari',
    'Lalit',
    'Mangal Bhairav',
    'Sargam',
    'Pancham',
    'Sur',
    'Rythem'
]
#Remove all passwords, put them into .env
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Welcome@2025",
    database="gym_db"
)
cursor = conn.cursor()

# Reset the table (optional: deletes all existing data and resets ID)
#cursor.execute("TRUNCATE TABLE memberships")

# OR: Just reset auto-increment without deleting data
#cursor.execute("ALTER TABLE memberships AUTO_INCREMENT = 1")


for _ in range(20):
    full_name = fake.name()
    name_parts = full_name.split()
    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower() if len(name_parts) > 1 else ""

    email = f"{first_name}.{last_name}@example.in"

    phone = fake.msisdn()[0:10]
    program = random.choice(programs)
    locality = random.choice(localities)
    months = random.choice([3, 6, 12])
    start_date = fake.date_between(start_date='-1y', end_date='today')
    fees = random.randint(4000, 15000)

    cursor.execute("""
    INSERT INTO memberships 
    (email, full_name, phone_number, program_type, locality, membership_length_months, start_date, fees_paid)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (email, full_name, phone, program, locality, months, start_date, fees))
    print(email, full_name, phone, program, locality, months, start_date, fees)
conn.commit()
conn.close()
