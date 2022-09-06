# read db and remove newlines from lines array
db = open('db.csv', 'r')
raw = db.readlines()
lines = []
for line in raw:
    line = str.replace(line, '\n', '')
    lines.append(line)