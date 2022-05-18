import sqlite3
with sqlite3.connect('company.db') as db:
    cursor=db.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS users(
userid INT PRIMARY KEY, name TEXT, dept TEXT, salary INT);''')
def input_data():
    newId=input('Ведите id: ')
    newNAME=input('Ведите имя')
    newDEPT=input('Ведите должность')
    newSALARY=input('Ведите зарплату')
    cursor.execute(''' 
    INSERT INTO users(userid, name, dept, salary)
    VALUES(?, ?, ?, ?)''', (newId, newNAME, newDEPT, newSALARY))
    db.commit()
a='y'
while a=='y':
    a=input('Хотите вести новые данные (y/n)?')
    if a=='n':
        break
    elif a=='y':
        input_data()
    else:
        print('Error')
        break

cursor.execute('DELETE FROM users WHERE userid=1')
db.commit()
cursor.execute('SELECT * FROM users')
for x in cursor.fetchall():
    print(x)
db.close()
