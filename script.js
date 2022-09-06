console.log('script loaded');

const emails = ["hbagalkote@gmail.com", "testemail1@gmail.com", "testemail2@gmail.com", "testemail3@gmail.com"];

function clickFunction() {

    // get form fields
    student_id = document.getElementById('student_id').value;
    fname = document.getElementById('fname').value;
    lname = document.getElementById('lname').value;
    intervention_teacher = document.getElementById('intervention_teacher').value;

    // check to see email exists within list
    intervention_teacher = intervention_teacher.toLowerCase();
    if (!emails.includes(intervention_teacher)) {
        alert("Invalid teacher email, valid emails: " + emails);
        return;
    }

    // send post request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/form_filled", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        'student_id': student_id,
        'fname': fname,
        'lname': lname,
        'intervention_teacher': intervention_teacher
    }));
}