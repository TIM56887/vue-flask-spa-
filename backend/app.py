from flask import Flask, jsonify, request, render_template, send_from_directory
import pymysql.cursors
from nanoid import generate
from sql import quizDB
from sql import commentDB
from household.household import caculate 
    
DB2 = quizDB()
DB_comment = commentDB()

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

@app.route('/sendcomment', methods=['POST'])
def sendcomment():
    data = request.json
    DB_comment.add_comment(data)
    return 'ok'

@app.route('/getcomment', methods=['GET'])
def getcomment():
    data = DB_comment.get_comment()
    
    return jsonify(data)
@app.route('/updatecomment', methods=['POST'])
def updatecomment():
    data = request.json
    DB_comment.update_comment(data)
    return 'ok'

@app.route('/deletecomment', methods=['POST'])
def deletecomment():
    id = request.json
    print(id)
    DB_comment.delete_comment(id['commentId'])
    return 'ok'
    

    
if __name__ == '__main__':
    app.run(debug=True)