import schedule
import time

def job():
    attendance = open('attendance.csv', 'w')
    db = open('db.csv', 'w')
    attendance.write('fname,lname,status' + '\n')
    db.write('student_id,fname,lname,intervention_teacher' + '\n')

schedule.every().day.at("12:00").do(job)