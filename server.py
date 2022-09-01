from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def default():
    return 'backend works'

@app.route('/form_filled', methods=['POST'])
def form_filled():
    data = request.json
    print(data['student_id'])
    print(data['fname'])
    print(data['lname'])
    print(data['intervention_teacher'])
    return 'res ok'

if __name__ == "__main__":
    app.run()