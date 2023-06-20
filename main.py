from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(user="postgres", password="Dennis97", host="localhost", port="5432", database="hellaCo")

cur=conn.cursor()

@app.route('/')
def hello_world():
    name="Dennis"
    return render_template("index.html", x=name)

@app.route('/employees')
def employees():
    cur.execute("Select * from employees")
    employees=cur.fetchall()
    print(employees)
    return render_template("employees.html", employees=employees)
    

if __name__ == "__main__":
    app.run()
