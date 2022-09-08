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

    student_id = str(data['student_id'])
    fname = str(data['fname'])
    lname = str(data['lname'])
    intervention_teacher = str(data['intervention_teacher'])
    f = open('db.csv', 'a')
    f.write(student_id + ',' + fname + ',' + lname + ',' + intervention_teacher + '\n')
    f.close()
    
    return 'res ok'

@app.route('/get_students', methods=['POST'])
def get_students():

    data = request.json
    gcps_email = str(data['gcps_email']).lower()
    students = []
    student_fname = 1
    student_lname = 2
    intervention_teacher = 3

    db = open('db.csv', 'r')
    raw = db.readlines()
    lines = []
    for line in raw:
        line = str.replace(line, '\n', '')
        lines.append(line)

    for i in range(1, len(lines)):
        raw = lines[i]
        line = raw.split(',')
        if line[intervention_teacher] == gcps_email:
            student_full_name = line[student_fname] + ' ' + line[student_lname]
            students.append(student_full_name)

    if len(students) == 0:
        return "no students signed up"

    return str(students)

@app.route('/<var_url>')
def parameter(var_url):
    
    # format: fname_lname_status
    '''
        statuses:
        present
        absent
        not required
    '''

    raw_arr = var_url.split('_')
    print('DEBUG: ' + str(raw_arr) + ' ' + str(len(raw_arr)))
    fname = raw_arr[0]
    lname = raw_arr[1]
    status = raw_arr[2]

    attendance = open('attendance.csv', 'a')
    attendance.write(fname + ',' + lname + ',' + status + '\n')
    return fname + ' ' + lname + ' marked as ' + status



# run
if __name__ == "__main__":
    app.run()