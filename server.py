from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return 'backend works'

@app.route('/form_filled', methods=['POST'])
def form_filled():
    
    data = request.json
    print('recieved: ' + str(data)) # test

    student_id = str(data['student_id'])
    fname = str(data['fname'])
    lname = str(data['lname'])
    intervention_teacher = str(data['intervention_teacher'])
    f = open('db.csv', 'a')
    f.write(student_id + ',' + fname + ',' + lname + ',' + intervention_teacher + '\n')
    f.close()
    
    return 'res ok'

if __name__ == "__main__":
    app.run()