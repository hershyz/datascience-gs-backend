console.log('script loaded');

function clickFunction() {
    
    var email = document.getElementById("email").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/get_students", false);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        'gcps_email': email
    }));
    raw = xhr.responseText;
    raw = raw.replace('[', '');
    raw = raw.replace(']', '');
    raw = raw.replace(/[']/g, '') // regex
    
    document.write("<strong>Guided Study List for " + email + ":</strong><br>")
    const names = raw.split(', ');
    for (var i = 0; i < names.length; i++) {
        document.write(names[i] + "<br>");
    }
}