from flask import Flask, render_template, request, redirect
import mysql.connector
import config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB
    )

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, phone, course, address))
    conn.commit()
    conn.close()
    return redirect('/students')

@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
