import sqlite3 as s
db=s.connect("app.db")
cr=db.cursor()
uid=1
cr.execute("CREATE TABLE if not exists users(name TEXT,age INTEGER,id INTEGER)")
def save():
    db.commit()
    db.close()
def main():
    my_msg="""
s => show
a => add
u => update
d => delete
q => quit
enter : """
    inp=input(my_msg).strip().lower()



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
        rename=cr.fetchone()

        cr.execute(f"SELECT age FROM users where id={uid} and name='{var1}'")
        re2=cr.fetchone()
        if rename==None:
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



    def delete():
        var1=input("enter your name : ")
        cr.execute(f"SELECT name FROM users where id={uid} and name='{var1}'")
        re2=cr.fetchone()
        if re2==None:
            print('this name is not found add this')
        else:
            var=input('Your account will delete y,n:')
            if var in ['n','y']:
                if var=='y':
                    cr.execute(f"DELETE from users where name='{var1}'")
                    print('your account is deleted')
                else:
                    print('good decetion')
            else:
                print("plese chosse y or n")


    def my_app(com):
        if com=='a':
            add()
        elif com=='s':
            show()
        elif com=='u':
            update()
        elif com=='d':
            delete()
        else:
            return False



    if inp in ['s','a','u','d','q']:
        my_app(inp)
    else:
        print('this is not in commands')
        main()

main()


save()