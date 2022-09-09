console.log('script loaded');

function clickFunction() {
    
    var email = document.getElementById("intervention_teacher").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/get_students", false);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        'gcps_email': email
    }));
    raw = xhr.responseText;

    if (raw.responseText == 'no students signed up') {
        document.write("<strong>Guided Study List for " + email + ":</strong><br>")
        document.write('no students signed up')
        return
    } 

    raw = raw.replace('[', '');
    raw = raw.replace(']', '');
    raw = raw.replace(/[']/g, '') // regex
    
    document.write("<strong>Guided Study List for " + email + ":</strong><br>")
    const names = raw.split(', ');
    for (var i = 0; i < names.length; i++) {

        var name_raw = names[i].split(" ");
        var fname = name_raw[0];
        var lname = name_raw[1];
        var present_link = '<a href="http://127.0.0.1:5000/' + fname + '_' + lname + '_present">Present</a>';
        var absent_link = '<a href="http://127.0.0.1:5000/' + fname + '_' + lname + '_absent">Absent</a>';
        var wrong_location_link = '<a href="http://127.0.0.1:5000/' + fname + '_' + lname + '_wronglocation">I did not request this student</a>';

        document.write(names[i] + ' - ' + present_link + ', ' + absent_link + ', ' + wrong_location_link + "<br>");
    }
}