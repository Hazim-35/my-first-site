from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_history(val):
    conn = sqlite3.connect('garage_system.db')
    cursor = conn.cursor()
    # البحث باللوحة أو الرقم التسلسلي
    cursor.execute("SELECT * FROM maintenance WHERE plate_number=? OR serial_number=?", (val, val))
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    return '''
    <html dir="rtl">
    <head>
        <style>
            body { background: #f8e1f4; font-family: Arial; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
            .box { background: white; padding: 50px; border-radius: 30px; border: 4px solid #8a2be2; text-align: center; box-shadow: 0 15px 30px rgba(0,0,0,0.1); width: 400px; }
            h1 { color: #8a2be2; margin-bottom: 5px; }
            h2 { color: #ff69b4; margin-top: 0; margin-bottom: 30px; font-size: 20px; }
            input { width: 100%; padding: 15px; border-radius: 10px; border: 2px solid #ff69b4; outline: none; text-align: center; font-size: 16px; }
            button { background: #8a2be2; color: white; border: none; padding: 15px 40px; border-radius: 10px; margin-top: 20px; cursor: pointer; font-size: 18px; font-weight: bold; width: 100%; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>مرحباً بكم في وكالة</h1>
            <h2>H S F للصيانة</h2>
            <form action="/view" method="get">
                <input type="text" name="search_val" placeholder="أدخل اللوحة أو الرقم التسلسلي">
                <button type="submit">استعلام عن السيارة 🔍</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/view')
def view():
    val = request.args.get('search_val')
    history = get_history(val)
    return render_template('history.html', history=history)

if __name__ == '__main__':
    # السماح بالدخول من أي جهاز في الشبكة
    app.run(host='0.0.0.0', port=5000)