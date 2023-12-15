import pymysql.cursors
import json
from datetime import datetime

with open('./mysqlPassword.json') as f:
    data = json.load(f)
password = data['password']
class commentDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password=password,
            database='LineComment',
            cursorclass=pymysql.cursors.DictCursor)
        
    def add_comment(self, content):
        self.connection.ping(reconnect=True)
        # timestamp  = datetime.strptime(content['createtime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        # content['createtime'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        with self.connection.cursor() as cursor:
            sql = f"INSERT INTO comment (userId, displayName, pictureUrl, commentDate, commentText) VALUES ('{content['userId']}', '{content['displayName']}', '{content['pictureUrl']}', '{content['commentDate']}', '{content['commentText']}');"
            cursor.execute(sql)
            self.connection.commit()
            return  cursor.lastrowid
        
    def get_comment(self):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
            sql = "SELECT * from comment"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


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

class quizDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password=password,
            database='codeQuiz',
            cursorclass=pymysql.cursors.DictCursor)
    def getQuestion(self,amount,listed=False):    
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
                if listed:
                    sql = f"select * from questions ORDER BY question_id LIMIT {amount};"
                else:
                    sql = f"select * from questions ORDER BY RAND() LIMIT {amount};"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
    
    def addQuestion(self,question):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
            sql = f"INSERT INTO questions (question, question_code, option1, option2, option3, option4, answer, question_type, explanation) VALUES ('{question['question']}', '{question['code']}', '{question['option'][0]}', '{question['option'][1]}', '{question['option'][2]}', '{question['option'][3]}', '{question['answer']}', '{question['type']}', '{question['explanation']}' );" 
            cursor.execute(sql)
            self.connection.commit()
            return cursor.lastrowid
        
    def getNewQuestion(self,previosQID):
        self.connection.ping(reconnect=True)
        with self.connection.cursor() as cursor:
                sql = "SELECT * FROM questions WHERE question_id NOT IN (%s) LIMIT 5"
                in_p = ', '.join(list(map(lambda x: '%s', previosQID)))
                sql = sql % in_p
                cursor.execute(sql, previosQID)
                result = cursor.fetchall()
                return result
    def deleteQuestion(self,questionID):
        pass

    def editQuestion(self,newValue):
        pass
