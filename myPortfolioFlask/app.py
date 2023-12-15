from flask import Flask, jsonify, request, render_template, send_from_directory
import pymysql.cursors
from nanoid import generate
from sql import TodoDB
from sql import quizDB
from household import caculate 
    

DB = TodoDB()
DB2 = quizDB()

app = Flask(__name__,
            static_folder='./dist',
            template_folder='./dist',
            static_url_path=''
            )
@app.route('/')
def index():
    return render_template('index.html',name='index')

@app.route('/jsquiz')
def jsquiz():
    return send_from_directory('./dist2','index.html')

@app.route('/assets/<path:path>')
def static_files(path):
    return send_from_directory('dist2', 'assets/'+path)

@app.route('/todo', methods=['GET'])
def todo():
    data = DB.get_todo()
    return jsonify(data)

@app.route('/deletetodo', methods=['post'])
def deletetodo():
    id = request.json['id']
    print(id,'----------------')
    if id is not None:
        DB.delete_todo(id)
        return jsonify({'message': 'Data received successfully'}), 200
    else:
        return jsonify({'message': 'No data received'}), 400  # Bad Request

@app.route('/addtodo', methods=['post'])
def addtodo():
    content = request.json
    if not content['userid']:
        content['userid'] = generate(size=5)
    contentid = DB.add_todo(content)
    return jsonify({'message': 'Data received successfully','userid':content['userid'],'contentid':contentid}), 200

@app.route('/editTodo', methods=['post'])
def editTodo():
    editcontent = request.json
    print(editcontent)
    DB.edittodo(editcontent["id"],editcontent["content"])
    return "ok"


@app.route('/getUserTodo', methods=['post'])
def getUserTodo():
    userid = request.json['userid']
    userstodo = DB.getuserstodo(userid)
    print(userstodo,'------------')
    return jsonify(userstodo)

@app.route('/process', methods=['POST'])
def process_form():
    form_data = request.form 
    data = []
    for key, value in form_data.items():
        data.append(value)
    price = int(caculate(data))
    predictPrice = {
        "data":data,
        "price":price
    }
    return render_template('housePricePrediction.html',predictPrice=predictPrice)

@app.route('/predict')
def predict():
    return render_template('housePricePrediction.html',predictPrice={"data":"none"})  

@app.route('/quiz')
def getQuiz():
    amount = request.args.get('amount', default=None , type=int)
    listed = request.args.get('listed', default=None , type=bool)
    data = DB2.getQuestion(amount,listed)
    return jsonify(data)

@app.route('/fivequiz', methods=['POST'])
def fivequiz():
    data = request.get_json()
    previousQID = data['currentQuestionIds']
    data = DB2.getNewQuestion(previousQID)
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)