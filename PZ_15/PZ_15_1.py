import sqlite3 as sq

# создаем базу и таблицу
with sq.connect("db.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        master TEXT,
        client TEXT,
        cleaning_type TEXT,
        price INTEGER,
        discount INTEGER
    )
    """)

# добавляем данные (10 записей)
with sq.connect("db.db") as con:
    cur = con.cursor()

    cur.execute("INSERT INTO services VALUES (1, 'Иванов', 'Петров', 'Ковер', 3000, 10)")
    cur.execute("INSERT INTO services VALUES (2, 'Сидоров', 'Иванова', 'Пальто', 2000, 5)")
    cur.execute("INSERT INTO services VALUES (3, 'Кузнецов', 'Смирнов', 'Куртка', 1800, 0)")
    cur.execute("INSERT INTO services VALUES (4, 'Орлов', 'Кузьмина', 'Платье', 2200, 10)")
    cur.execute("INSERT INTO services VALUES (5, 'Попов', 'Федоров', 'Ковер', 3200, 15)")
    cur.execute("INSERT INTO services VALUES (6, 'Васильев', 'Алексеев', 'Шторы', 3500, 20)")
    cur.execute("INSERT INTO services VALUES (7, 'Зайцев', 'Морозова', 'Куртка', 1700, 5)")
    cur.execute("INSERT INTO services VALUES (8, 'Семенов', 'Лебедев', 'Ковер', 2800, 15)")
    cur.execute("INSERT INTO services VALUES (9, 'Николаев', 'Ковалев', 'Пальто', 2100, 10)")
    cur.execute("INSERT INTO services VALUES (10, 'Григорьев', 'Соколов', 'Пиджак', 1600, 0)")

# --- ПОИСК (3 запроса) ---
with sq.connect("db.db") as con:
    cur = con.cursor()

    print("Поиск 1:")
    cur.execute("SELECT * FROM services WHERE price > 2000")
    print(cur.fetchall())

    print("Поиск 2:")
    cur.execute("SELECT * FROM services WHERE cleaning_type = 'Ковер'")
    print(cur.fetchall())

    print("Поиск 3:")
    cur.execute("SELECT * FROM services WHERE discount >= 10")
    print(cur.fetchall())

# --- ОБНОВЛЕНИЕ (3 запроса) ---
with sq.connect("db.db") as con:
    cur = con.cursor()

    cur.execute("UPDATE services SET price = price + 100 WHERE cleaning_type = 'Ковер'")
    cur.execute("UPDATE services SET discount = discount + 5 WHERE price > 2000")
    cur.execute("UPDATE services SET price = price - 200 WHERE discount > 10")

# --- УДАЛЕНИЕ (3 запроса) ---
with sq.connect("db.db") as con:
    cur = con.cursor()

    cur.execute("DELETE FROM services WHERE discount = 0")
    cur.execute("DELETE FROM services WHERE price < 1700")
    cur.execute("DELETE FROM services WHERE cleaning_type = 'Пиджак'")

# --- ВЫВОД ---
with sq.connect("db.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM services")

    print("Итог:")
    for row in cur:
        print(row)