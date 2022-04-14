import  numpy as np
from flask import Flask, url_for, request, render_template
from pymongo import MongoClient

myclient = MongoClient("mongodb+srv://beop:beopson@cluster0.lgzqe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = myclient.ClassWork

app = Flask(__name__)

@app.route('/')
def home():
 return render_template("home.html")

@app.route('/data', methods= ["POST", "GET"])
def data():
    data = {}
    if request.method =="POST":

     data['first_name'] = str(request.form["firstname"][0].upper() + request.form["firstname"][1:].lower())
     data['last_name'] = str(request.form["lastname"][0].upper() + request.form["lastname"][1:].lower())
     data['grade'] = int(request.form["grade"])
     data['age'] = int(request.form["age"])    
     db.ClassWork.insert_one(data)
    return render_template("home.html" )


if __name__ == "__main__":
    app.run(debug=False)

