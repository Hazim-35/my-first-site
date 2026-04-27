import sqlite3


def init_db():
    # إنشاء اتصال بقاعدة البيانات
    conn = sqlite3.connect('garage_system.db')
    cursor = conn.cursor()

    # إنشاء الجدول مع كافة التفاصيل المطلوبة
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL,
            serial_number TEXT NOT NULL,
            owner_name TEXT,
            car_type TEXT,
            car_color TEXT,
            vin_number TEXT,
            service_type TEXT,
            technician_name TEXT,
            price REAL,
            discount REAL,
            total_price REAL,
            service_date DATE,
            next_service DATE
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ تم إنشاء نظام قاعدة البيانات لوكالة H S F بنجاح!")


if __name__ == "__main__":
    init_db()