CREATE TABLE IF NOT EXISTS memberships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    full_name VARCHAR(100),
    phone_number VARCHAR(15),
    program_type VARCHAR(50),
    locality VARCHAR(100),
    membership_length_months INT,
    start_date DATE,
    fees_paid DECIMAL(10,2)
)
