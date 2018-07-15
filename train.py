from sklearn import tree
import csv
import pickle
X = []
y = []
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        X.append(row[0])
        l = [row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27]]
        y.append(l)
#print (y)

clf = tree.DecisionTreeClassifier()

clf = clf.fit(y,X)

filename = 'flag_model.pkl'
pickle.dump(clf, open(filename, 'wb'))
