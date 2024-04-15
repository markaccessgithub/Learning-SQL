import sqlite3

print("Welcome - Enter 1 for viewing a students centre location, and 2 for adding a student")
choice = int(input())
if choice == 1:
    name = input("Enter name: ")
    conn = sqlite3.connect("GoOnlinePt3.db")
    cur = conn.cursor()
    res = cur.execute(f"SELECT centre_id FROM student WHERE student_name = '{name}';")
    list = res.fetchone()
    print(list[0])
    new = cur.execute(f"SELECT centre_location FROM Centres WHERE centre_id = {list[0]};")
    print(new.fetchone())
elif choice == 2:
    name = input("Enter name: ")
    centre = int(input("Enter centre numebr: "))
    conn = sqlite3.connect("GoOnlinePt3.db")
    cur = conn.cursor()
    new = cur.execute("SELECT * FROM student;")
    list= new.fetchall()
    aa = cur.execute(f"INSERT INTO student (student_id, centre_id, student_name) VALUES ({(len(list))+1}, {centre}, '{name}');")
    res = cur.execute("SELECT * FROM student;")
    print(res.fetchall())

