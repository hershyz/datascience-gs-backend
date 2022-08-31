import requests

valid_teacher_emails = ['julia.rachkovskiy@gcpsk12.org', 'elfi.funk@gcpsk12.org', 'jeff.burmester@gcpsk12.org', 'bradley.kastner@gcpsk12.org', 'hbagalkote@gmail.com'] # my email for test

def main():
    
    student_id = input('Enter your student ID: ')
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    intervention_teacher = input('Intervention teacher email: ').lower()
    
    if intervention_teacher not in valid_teacher_emails:
        print('Invalid intervention teacher email, valid ones are: ' + str(valid_teacher_emails))
        main()
    
    # send post request
    payload = {
        'student_id': student_id,
        'fname': fname,
        'lname': lname,
        'intervention_teacher': intervention_teacher
    }
    requests.post('http://127.0.0.1:5000/form_filled', json=payload)


main()