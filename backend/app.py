from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/update', methods=['POST'])
def update_bin():
    level = request.json['level']
    status = "FULL" if level > 80 else "OK"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bins(level,status) VALUES(?,?)",(level,status))
    conn.commit()
    conn.close()

    return jsonify({"message":"Data updated"})

@app.route('/status', methods=['GET'])
def get_status():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bins ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()
    conn.close()

    if data:
        return jsonify({"level":data[1],"status":data[2]})
    return jsonify({"level":0,"status":"UNKNOWN"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
