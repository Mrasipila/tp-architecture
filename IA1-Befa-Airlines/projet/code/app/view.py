from flask import Blueprint, request, render_template
from app.db import get_db
from . import API

bp = Blueprint('view', __name__)

@bp.route('/index', methods=('GET', 'POST'))
def index():
    string = "<br>"
    db = get_db()
    i = 1
    if request.method == 'GET':
        API.Load_Database('http://api-rg-esiea-tp.westeurope.azurecontainer.io/flights', db)
        return render_template('view/index.html')
    if request.method == 'POST':
        code = request.form['code']
        departure = request.form['departure']
        arrival = request.form['arrival']

        # Retrieving Data from file
        if db.execute('SELECT * FROM flights WHERE code = ?', (code,)).fetchone() is not None:
            rowCode = db.execute('SELECT * FROM flights WHERE code = ?', (code,)).fetchone()
        else:
            rowCode = db.execute("select * from flights where arrival=:a and departure=:b",
                                 {"a": arrival, "b": departure}).fetchall()

        if rowCode is not None:
            for i in range(len(rowCode)):
                db.execute("INSERT INTO reservations (code,departure,arrival,price) VALUES (?,?,?,?);",
                           (rowCode[i][0], rowCode[i][1], rowCode[i][2], rowCode[i][3]))
            db.commit()
        else:
            return "No Flights for your entries, maybe come next time"

        for i in range(len(rowCode)):
            string += str(rowCode[i][0]) + " " + str(rowCode[i][1]) + " " + str(rowCode[i][2]) + " " + str(
                rowCode[i][3]) + "<br>"

        return f"Transaction Done, You can go check your reservations for the flight {string}"


@bp.route('/list')
def list():
    db = get_db()
    data = db.execute("SELECT * FROM reservations").fetchall()
    print(db.execute("SELECT * FROM reservations").fetchall())
    return render_template('view/list.html', rowQ=data)
