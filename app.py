from flask import Flask,render_template,request
from openpyxl import load_workbook

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/rooms')
def rooms():
    return render_template("rooms.html")


@app.route('/booking',methods=['GET','POST'])
def booking():

    if request.method=='POST':

        name=request.form['name']
        phone=request.form['phone']
        room=request.form['room']
        date=request.form['date']
        payment=request.form['payment']

        file=load_workbook("hoteldata.xlsx")
        sheet=file.active

        sheet.append([name,phone,room,date,payment])

        file.save("hoteldata.xlsx")

        return "<h2>Booking Successful</h2><a href='/'>Home</a>"

    return render_template("booking.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


app.run(debug=True)
