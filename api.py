from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "plosoltra"
app.config["MYSQL_DB"] = "api"

mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM addresses")
    addresses = cur.fetchall()
    cur.close()

    return render_template('index.html', addresses=addresses)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        address_id = request.form['address_id']
        line_1_number_building = request.form['line_1_number_building']
        line_2_number_street = request.form['line_2_number_street']
        line_3_number_locality = request.form['line_3_number_locality']
        town_city = request.form['town_city']
        zip_postcode = request.form['zip_postcode']
        country_state_province = request.form['country_state_province']
        country = request.form['country']
        other_address_details = request.form['other_address_details']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO addresses (address_id, line_1_number_building, line_2_number_street, line_3_number_locality, town_city, zip_postcode, country_state_province, country, other_address_details) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (address_id, line_1_number_building, line_2_number_street, line_3_number_locality, town_city, zip_postcode, country_state_province, country, other_address_details))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
    
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        address_id = request.form['address_id']
        line_1_number_building = request.form['line_1_number_building']
        line_2_number_street = request.form['line_2_number_street']
        line_3_number_locality = request.form['line_3_number_locality']
        town_city = request.form['town_city']
        zip_postcode = request.form['zip_postcode']
        country_state_province = request.form['country_state_province']
        country = request.form['country']
        other_address_details = request.form['other_address_details']
        cur.execute("UPDATE addresses set address_id=%s, line_1_number_building=%s, line_2_number_street=%s, line_3_number_locality=%s, town_city=%s, zip_postcode=%s, country_state_province=%s, country=%s, other_address_details=%s WHERE id=%s", (address_id, line_1_number_building, line_2_number_street, line_3_number_locality, town_city, zip_postcode, country_state_province, country, other_address_details))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
    else:
        cur.execute("SELECT * FROM addresses WHERE address_id = %s", (id,))
        address= cur.fetchone()
        cur.close()

        return render_template('edit_add.html', address=address)

@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM addresses WHERE address_id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)