from flask import Flask, request, jsonify
import logging
import psycopg2
from datetime import datetime
from sqlalchemy import create_engine

app = Flask(__name__)

# Database connection settings
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'logging_db'
DB_PORT = '5432'
DB_NAME = 'logging'  # Change this back to 'logging'


# Create a connection to the database (for logging)
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Set up logging for Flask app
logging.basicConfig(filename='app.log', level=logging.INFO)

# Database logging function (logs to 'revest' database)
def log_to_db(product_id, recommended_product, log_type="INFO"):
    try:
        # Create a connection to the database
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor()
        
        # Get the current timestamp
        timestamp = datetime.now()

        # Insert log into the database
        cursor.execute("""
            INSERT INTO logs (timestamp, product_id, recommended_product, log_type)
            VALUES (%s, %s, %s, %s)
        """, (timestamp, product_id, recommended_product, log_type))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        print("Log inserted into database.")

    except Exception as e:
        logging.error(f"Error logging to DB: {str(e)}")

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        product_id = data.get('product_id')

        # Log the incoming request to DB
        log_to_db(product_id, "Request received", "INFO")

        # Static recommendation logic
        recommended_product = "[1, 2, 3]"

        # Log the recommendation to DB
        log_to_db(product_id, recommended_product, "INFO")

        # Return the recommendation response
        return jsonify({
            "message": "Product recommendation generated successfully!",
            "product_id": product_id,
            "recommended_product": recommended_product
        })

    except Exception as e:
        # Log any errors to DB
        log_to_db(product_id, f"Error: {str(e)}", "ERROR")
        logging.error(f"{datetime.now()} - Error: {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
