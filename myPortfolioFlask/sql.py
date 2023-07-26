import pymysql.cursors
import json
from datetime import datetime

with open('./mysqlPassword.json') as f:
    data = json.load(f)
password = data['password']


class TodoDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password=password,
            database='portfolio',
            cursorclass=pymysql.cursors.DictCursor)

    def get_todo(self):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
            sql = "SELECT DATE_FORMAT(due_date, '%c/%d') AS date, done, task, id from todo"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    def delete_todo(self, id):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
            sql = f"DELETE FROM todo WHERE id = {id};"
            cursor.execute(sql)
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Todo was deleted successfully.")
            else:
                print("No todo found with that id.")
    def add_todo(self, content):
        self.connection.ping(reconnect=True)
        timestamp  = datetime.strptime(content['createtime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        content['createtime'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        with self.connection.cursor() as cursor:
            sql = f"INSERT INTO todo (task, due_date, done, user_id) VALUES ('{content['content']}', '{content['createtime']}', true,'{content['userid']}');"
            cursor.execute(sql)
            self.connection.commit()
            return  cursor.lastrowid
    def getuserstodo(self, userid):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
            sql = f"select id from todo where user_id = '{userid}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
    def edittodo(self, todoId,todoContent):
        self.connection.ping(reconnect=True)
        print(todoId,todoContent)
        with self.connection.cursor() as cursor:
            sql = f"UPDATE todo SET task = '{todoContent}' where id = {todoId}"
            cursor.execute(sql)
            return "ok"


