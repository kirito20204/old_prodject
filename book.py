import sqlite3
with sqlite3.connect('PhoneBook.db') as db:
    cursor=db.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS names(
id INT PRIMARY KEY, firstname TEXT, surname TEXT, phone_number INT);''')

def input_data():
    newId=input('Ведите id: ')
    newFIRSTNAME=input('Ведите имя')
    newSURNAME=input('Ведите Фамилию')
    newNEMBER=input('Ведите Номер телефонаn')
    cursor.execute(''' 
    INSERT INTO names(id, firstname, surname, phone_number)
    VALUES(?, ?, ?, ?)''', (newId, newFIRSTNAME, newSURNAME, newNEMBER))
    db.commit()

def viewbook():
    cursor.execute('SELECT * FROM names')
    for x in cursor.fetchall():
        print(x)
def selectname():
    b=input('Ведите фамилию')
    cursor.execute('SELECT * FROM names WHERE surname=?', [b])
    for x in cursor.fetchall():
        print(x)
 

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

cursor.execute('SELECT * FROM names')
for x in cursor.fetchall():
    print(x)
db.close()