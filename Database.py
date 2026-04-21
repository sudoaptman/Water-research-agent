import os
import mysql.connector
from dotenv import load_dotenv

# Load credentials from the .env file
load_dotenv()

def get_db_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME')
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_from_db(sector):
    """Retrieves water hardness data for a specific postcode sector."""
    conn = get_db_connection()
    if not conn:
        return None
        
    cursor = conn.cursor(dictionary=True)
    query = "SELECT ppm_value, classification FROM water_zones WHERE postcode_sector = %s"
    cursor.execute(query, (sector,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return result

def save_to_db(sector, data):
    """Saves new water hardness data to the database."""
    conn = get_db_connection()
    if not conn:
        return False
        
    cursor = conn.cursor()
    query = """
        INSERT INTO water_zones (postcode_sector, ppm_value, classification) 
        VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(query, (sector, data['ppm_value'], data['classification']))
        conn.commit()
        success = True
    except mysql.connector.Error as err:
        print(f"Failed to save data: {err}")
        success = False
        
    cursor.close()
    conn.close()
    return success
