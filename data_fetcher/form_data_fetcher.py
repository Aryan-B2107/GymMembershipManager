from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import csv
from datetime import datetime
# import mysql.connector  # Uncomment later if you use MySQL
# import pandas as pd     # Uncomment if syncing with CSV & DB

app = Flask(__name__)
CORS(app)


@app.route('/api/membership', methods=['POST'])
def create_membership():
    try:
        data = request.get_json()

        print("\n" + "=" * 50)
        print("NEW MEMBERSHIP APPLICATION RECEIVED!")
        print("=" * 50)

        print(f"📧 Email: {data.get('email', 'N/A')}")
        print(f"👤 Full Name: {data.get('fullName', 'N/A')}")
        print(f"📱 Phone: {data.get('phone', 'N/A')}")
        print(f"📋 Program Type: {data.get('programType', 'N/A')}")
        print(f"🏠 Location: {data.get('location', 'N/A')}")
        print(f"⏰ Membership Length: {data.get('membershipLength', 'N/A')} months")
        print(f"📅 Start Date: {data.get('startDate', 'N/A')}")
        print(f"💰 Fees: ₹{data.get('fees', 'N/A')}")
        print(f"✉️ Record Email: {data.get('recordEmail', False)}")
        print(f"🕐 Submitted At: {data.get('submittedAt', 'N/A')}")

        print("=" * 50)
        print("RAW DATA:")
        print(json.dumps(data, indent=2))
        print("=" * 50 + "\n")

        # Remove the 'submittedAt' key
        data.pop("submittedAt", None)

        # CSV file path
        csv_file = 'membership_data.csv'

        # Write to CSV
        try:
            with open(csv_file, 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
        except FileExistsError:
            with open(csv_file, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                writer.writerow(data)

        return jsonify({
            'success': True,
            'message': 'Data received and saved successfully!',
            'received_data': data
        }), 200

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to process data'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Membership API is running',
        'timestamp': datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    print("\n🚀 Starting Membership Form Backend...")
    print("📡 Server will run on: http://localhost:8000")
    print("📝 Available endpoints:")
    print("   POST /api/membership - Receive form data")
    print("   GET  /api/health - Health check")
    print("🎯 Waiting for form submissions...\n")

    app.run(host='0.0.0.0', port=8000, debug=True)


