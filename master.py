# class K:
#     areem=[]
#     def __init__(self,name,email,passw,gend):
#         self.name=name
#         self.email=email
#         self.passw=passw
#         self.gend=gend
#     def info(self):
#         K.areem.append([self.name,self.email,self.passw,self.gend])
# m=K('g','gr','rrer','rerg')
# l=K('gyj','gti','rer','regrg')
# h=K('gjj','gr','rfhrer','rer')
# m.info()
# l.info()
# h.info()

# print(K.areem)

#######################################
#######################################
#######################################
#######################################
# import sqlite3 as s
# db=s.connect("app.db")
# cr=db.cursor()
# cr.execute("CREATE TABLE if not exists users (name TEXT ,id INTEGER)")
# l=['Kareem','Ahmed']
# for k,u in enumerate(l):
#     cr.execute(f"INSERT INTO users (name,id) VALUES('{u}',{k+1})")

# cr.execute("select name,id from users")
# ad=cr.fetchall()
# print(ad)
# # update on user 
# cr.execute("update users set name='kemoo' where id=1")
# # delete users table
# # cr.execute("delete from users")
# db.commit()
# db.close()

#######################################
#######################################
#######################################
#######################################


import sqlite3 as s
db=s.connect("app.db")
cr=db.cursor()
uid=1
cr.execute("CREATE TABLE if not exists users(name TEXT,age INTEGER,id INTEGER)")
my_msg="""
s => show
a => add
u => update
d => delete
q => quit
enter : """
inp=input(my_msg).strip().lower()

def save():
    db.commit()
    db.close()


def add():
    var1=input("enter your name : ")
    cr.execute(f"SELECT name FROM users where id={uid} and name='{var1}'")
    re=cr.fetchone()
    if re==None:
        var2=input("enter your age : ")
        cr.execute(f"INSERT INTO users VALUES('{var1}','{var2}',{uid})")
        print("added succesfuly")
    else:
        print('you cannot use this name')
        add()

def show():
    var1=input("enter your name : ")
    cr.execute(f"SELECT name FROM users where id={uid} and name='{var1}'")
    re=cr.fetchone()

    cr.execute(f"SELECT age FROM users where id={uid} and name='{var1}'")
    re2=cr.fetchone()
    if re==None:
        print('this name is not found add this')
        add()
    else:
        print(re[0])

def update():
    var1=input("enter your name : ")
    cr.execute(f"SELECT name FROM users where id={uid} and name='{var1}'")
    re=cr.fetchone()
    if re!=None:
        req=input('age or name: ')
        if req in ['age','name']:
            if req=='age':
                nage=input('enter new age:')
                cr.execute(f"update users set age='{nage}' where name='{var1}'")
                print('data is updated')
            else:
                mname=input('enter new name:')

                cr.execute(f"SELECT name FROM users where id={uid} and name='{mname}'")
                re=cr.fetchone()
                if re==None:
                    cr.execute(f"update users set name='{mname}' where name='{var1}'")
                    print('data is updated')
                else:
                        print('you cannot update to this name try agian')


        else:
            print('please chosse name or age')

    else:
        print('this name is not found add this name')
        add()





def my_app(com):
    if com=='a':
        add()
    elif com=='s':
        show()
    elif com=='u':
        update()


if inp in ['s','a','u','d','q']:
    my_app(inp)
else:
    print('this is not in commands')



save()





















