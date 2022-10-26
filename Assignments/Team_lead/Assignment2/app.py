from flask import Flask,render_template,request
import ibm_db

conn=ibm_db.connect("DATABASE=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hdj19914;PWD=hwFw5qwF1TR6TWLc;",'','')
print("Connnected DB")

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
@app.route("/signin",methods=['GET', 'POST'])
def signin():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        rollno = request.form["rollno"]
        print(name,email,password,rollno)
        insert_sql = "INSERT INTO ZQB38336.PERSONS VALUES (?, ?, ?, ?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, password)
        ibm_db.bind_param(prep_stmt, 3, email)
        ibm_db.bind_param(prep_stmt, 4, rollno)
        ibm_db.execute(prep_stmt)
        return render_template('login.html', msg = msg) 
    else:
        return render_template('signin.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        select_sql = "SELECT * FROM ZQB38336.PERSONS WHERE USERNAME = ? AND PASSWORD = ?"
        prep_stmt = ibm_db.prepare(conn, select_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, password)
        out = ibm_db.execute(prep_stmt)
        result_dict = ibm_db.fetch_assoc(prep_stmt)
        print(result_dict)
        if result_dict != False:
            return render_template('home.html',msg = msg)
        return render_template('login.html', msg = msg)

    else:
        return render_template('login.html', msg = msg)

@app.route('/home', methods =['GET', 'POST'])
def home():
    msg = ''
    return render_template('home.html', msg = msg)