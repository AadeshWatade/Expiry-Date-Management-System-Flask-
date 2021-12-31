from flask import Flask, render_template, url_for, flash,  redirect
from re import I
import re
from flask import *
import mysql.connector
from datetime import date, timedelta, datetime

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
database = "inventory")
mycursor = mydb.cursor()

@app.route('/')
def index():
    mycursor.execute('select * from product')
    allres = mycursor.fetchall()
    for i in allres:
        d0 = i[3]
        d1 = i[4]
        delta = d1-d0
        if delta.days < 0:
            query = "update product set Status= %s where Id = %s"
            value = ('Expired', i[0])
            mycursor.execute(query,value)
            flash("Product {} with Id {} has expired!".format(i[1],i[0]))

    return render_template('index.html', allres = allres)



@app.route('/submit',methods=["GET","POST"])
def submit():
    if request.method=='POST':
        pid=request.form.get('pid')
        pname=request.form.get('pname').capitalize()
        pquantity=request.form.get('pquantity')
        pedate=request.form.get('pedate')
        pedate=pedate.replace('-','')
        pcdate=date.today().strftime("%Y%m%d")
        mycursor.execute("insert into product(Id,Name,Quantity,CDate,EDate) values(%s, %s, %s, %s ,%s)",(pid,pname,pquantity,pcdate,pedate))
        mydb.commit()
    return redirect('/')

@app.route('/delete/<string:id>' , methods = ['POST', 'GET'])
def delete(id):
    mycursor.execute("delete from product where Id={0}".format(id))
    mydb.commit()
    return redirect("/")

@app.route('/mdelete/<string:mid>' , methods = ['POST', 'GET'])
def mdelete(mid):
    mycursor.execute("delete from medicines where m_id={0}".format(mid))
    mydb.commit()
    return redirect("/medicines")

@app.route('/medicines', methods=['GET', 'POST'])
def medicines():
    mycursor.execute('select * from medicines')
    allres = mycursor.fetchall()
    for i in allres:
        d0 = i[3]
        d1 = i[4]
        delta = d1-d0
        if delta.days < 0:
            query = "update medicines set Status= %s where m_id = %s"
            value = ('Expired', i[0])
            mycursor.execute(query,value)
            flash("Product {} with Id {} has expired!".format(i[1],i[0]))
    return render_template('medicines.html', allres = allres)

@app.route('/submitmedicines', methods=['GET', 'POST'])
def submitmedicines():
    if request.method=='POST':
        mid=request.form.get('Mid')
        mname=request.form.get('Mname').capitalize()
        mquantity=request.form.get('Mquantity')
        Exp_date=request.form.get('Exp_date')
        Exp_date=Exp_date.replace('-','')
        c_date=date.today().strftime("%Y%m%d")
        mycursor.execute("insert into medicines(m_id,m_name,m_quantity,c_date,e_date) values(%s, %s, %s, %s ,%s)",(mid,mname,mquantity,c_date,Exp_date))
        mydb.commit()
    return redirect('/medicines')

@app.route('/groceries', methods=['GET', 'POST'])
def groceries():
    mycursor.execute('select * from product')
    allres = mycursor.fetchall()
    for i in allres:
        d0 = i[3]
        d1 = i[4]
        delta = d1-d0
        if delta.days < 0:
            query = "update product set Status= %s where Id = %s"
            value = ('Expired', i[0])
            mycursor.execute(query,value)
            flash("Product {} with Id {} has expired!".format(i[1],i[0]))
    return render_template('groceries.html', allres = allres)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
