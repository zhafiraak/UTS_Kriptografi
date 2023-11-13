from flask import Flask, render_template, request, redirect, url_for
from playfair_encrypt import initializeMatrix, prepareText, playfairEncrypt
import sqlite3

app = Flask(__name__)

# Inisialisasi database SQLite
conn = sqlite3.connect('customer_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, nama TEXT, alamat TEXT, password TEXT, key TEXT)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/simpan_data', methods=['POST'])
def simpan_data():
    nama = request.form['nama']
    alamat = request.form['alamat']
    password = request.form['password']
    key = request.form['key']

    # Inisialisasi matriks Playfair Cipher
    matrix = initializeMatrix(key)

    # Enkripsi password
    prepared_password = prepareText(password)
    encrypted_password = playfairEncrypt(prepared_password, matrix)

    # Simpan data nasabah ke database
    conn = sqlite3.connect('customer_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers (nama, alamat, password, key) VALUES (?, ?, ?, ?)", (nama, alamat, encrypted_password, key))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/data')
def data():
    conn = sqlite3.connect('customer_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    data = c.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
