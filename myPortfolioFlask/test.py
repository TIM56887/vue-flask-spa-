from sql import quizDB
import pickle
DB2 = quizDB()

with open('questionData.pkl', 'rb') as file:
    questionData = pickle.load(file)

del questionData[22]
for i in questionData:
    DB2.addQuestion(i)

