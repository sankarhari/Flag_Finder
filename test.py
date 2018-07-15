import pickle

f = open('flag_model.pkl','r')
clf = pickle.load(f)
f.close()

prediction = clf.predict([['4', '2', '753', '6', '10', '5', '3', '0', '4', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']])

print prediction

