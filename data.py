import datetime
import MySQLdb

# connecting database
DataBase = MySQLdb.connect(
    host='sql12.freemysqlhosting.net',
    user='sql12626663',
    password='aNEqHJYXsu',
    database='sql12626663'
)

# for accses in database
data = DataBase.cursor()
# var app
tables_name = ['twitter', 'tiktok', 'instagram', 'playstion', 'facebook']
###############################################################################
u_username: str = None
u_password:str = None
u_email:str = None
u_epassword:str = None
u_date:int = None
table_return = [u_username, u_password, u_email, u_epassword, u_date]
###############################################################################
APP = None
# save and commit in database
def save():
    DataBase.commit()
    DataBase.close()
class Data:
    class Table:
        # Create a new table in data base
        def new_table(TableName:str, Acction:str):
            data.execute(f"CREATE IF NOT EXISTS {TableName} {Acction}")
        # Delete databases
        def del_Table(Tablename):
            pass
    class User:
        # add a new user in database:
        def new_user(username:str, password:str, email:str, epassword:str, year:int):
            time = datetime.datetime.now()
            condtion = 'Inactive'
            data.execute(
                f"INSERT INTO {APP} (username, password, email, ebassword, year, condtion, adate)\
                VALUES ('{username}','{password}','{email}','{epassword}','{year}','{condtion}','{time})"
            )
            save()
        # information user from database
        def info_user(username):
            data.execute(f"SELECT * FROM {APP} WHERE username='{username}'")
            ret = data.fetchall()
            for rolls in ret:
                table_return[0] = rolls[0]
                table_return[1] = rolls[1]
                table_return[2] = rolls[2]
                table_return[3] = rolls[3]
                table_return[4] = rolls[4]
                table_return[5] = rolls[5]
                table_return[7] = rolls[7]
                table_return[8] = rolls[8]
                table_return[9] = rolls[9]
            save()
        def update_user():
            pass
        def del_user(table, data):
            pass
class acction:
    class sell:
        def selluser(id, username):
            pass
          