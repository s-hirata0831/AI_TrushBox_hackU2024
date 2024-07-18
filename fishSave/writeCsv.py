import csv

def resetCsv():
    l = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    with open('fishSave/state.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(l)

def readCsv(r,c):
    with open('fishSave/state.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    value = rows[r][c]
    return value