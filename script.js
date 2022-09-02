console.log('script loaded');

function clickFunction() {

    // get form fields
    student_id = document.getElementById('student_id').value;
    fname = document.getElementById('fname').value;
    lname = document.getElementById('lname').value;
    intervention_teacher = document.getElementById('intervention_teacher').value;

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