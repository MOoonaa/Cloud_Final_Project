from flask import Flask, render_template, request, redirect 
#import sqlite3
import pymysql

app = Flask (__name__, static_folder='static')

# Configure MySQL connection
mysql_host = 'database'  # This matches the service name in your Docker Compose configuration
mysql_user = 'root'
mysql_password = 'root'
mysql_database = 'StudentsDB'

def connect_to_mysql():
    return pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_database)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['id']
        
        # Connect to MySQL database
        connection = connect_to_mysql()
        cursor = connection.cursor()
        
        # Execute query to check if the provided name and id exist in the student table
        query = "SELECT * FROM student WHERE name=%s AND id=%s"
        cursor.execute(query, (name, student_id))
        
        # Fetch one row (if exists)
        student = cursor.fetchone()
        
        connection.close()  # Close database connection
        
        if student:
            return redirect('/table')
        else:
            error_message = "Invalid Name or ID."

    return render_template('login.html', error_message=error_message)

@app.route('/table')
def show_table():
    connection = connect_to_mysql()
    cursor = connection.cursor()

    # Execute SELECT query to retrieve data from MySQL student table
    cursor.execute('SELECT * FROM student')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    connection.close()  # Close database connection

    return render_template('table.html', rows=rows)
    
if __name__ == '__main__':
    app.run(debug=True)
    