# read db and remove newlines from lines array
db = open('db.csv', 'r')
raw = db.readlines()
lines = []
for line in raw:
    line = str.replace(line, '\n', '')
    lines.append(line)

# field consts
student_id = 0
student_fname = 1
student_lname = 2
intervention_teacher = 3

'''
    populate dictionary:
    key: intervention_teacher
    value: [student_fname+student_lname] (array)
'''
dict = {}
for i in range(1, len(lines)):
    
    raw = lines[i]
    line = raw.split(',')
    student_name = line[student_fname] + ' ' + line[student_lname]
    teacher_email = line[intervention_teacher].lower()
    
    if teacher_email in dict:
        curr_arr = dict[teacher_email]
        curr_arr.append(student_name)
        dict[teacher_email] = curr_arr
    
    if teacher_email not in dict:
        dict[teacher_email] = [student_name]