import sqlite3

host_name = "data.db"
def create_table():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("create table student(regno integer primary key, name text, sem integer, placed integer)")
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()


create_table()

def add_new_student(regno,name,sem,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("insert into student(regno,name,sem,placed)values(?,?,?,?)",(regno,name,sem,placed))
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()


add_new_student(10,'max',6,0)
add_new_student(12,'Lehan',6,2)
add_new_student(11,'RR007',6,3)


def show_students():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student")
        rows = cursor.fetchall()
        for row in rows:
            if row[3] == 0:
                status = 'Not Placed'
            else:
                status = 'Placed'
            print(f"reg_no:{row[0]}  Name: {row[1]} Sem: {row[2]} status:{status}")
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()


show_students()

def update_stu_status(regno, placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("update student set placed = ? where regno = ?", (placed,regno))
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()


update_stu_status(12, 3)

def show_student_regno(regno):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno, name, sem, placed from student where regno=?",(regno))
        row = cursor.fetchall()
        if row:
            if row[3] == 0:
                status = 'placed'
            else:
                status = 'not Placded'
            print(f"reg_no:{row[0]}  Name: {row[1]} Sem: {row[2]} status:{status}")
        else:
            print('not found')
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()

      