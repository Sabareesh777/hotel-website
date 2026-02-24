from flask import Flask, render_template, request
from openpyxl import load_workbook
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Rooms Page
@app.route('/rooms')
def rooms():
    return render_template("rooms.html")


# Booking Page
@app.route('/booking', methods=['GET','POST'])
def booking():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        room = request.form['room']
        date = request.form['date']
        payment = request.form['payment']

        # Get correct path for Render hosting
        filepath = os.path.join(os.getcwd(), "hoteldata.xlsx")

        # Load Excel file
        file = load_workbook(filepath)
        sheet = file.active

        # Add new booking row
        sheet.append([name, phone, room, date, payment])

        # Save file
        file.save(filepath)

        return "<h2>Booking Successful</h2><a href='/'>Go Home</a>"

    return render_template("booking.html")


# Contact Page
@app.route('/contact')
def contact():
    return render_template("contact.html")


# IMPORTANT for Render hosting
if __name__ == "__main__":
    app.run()
