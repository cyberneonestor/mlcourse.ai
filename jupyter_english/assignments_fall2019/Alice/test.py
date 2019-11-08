import pickle
pkl = r'D:/Programming/DS/mlcourse/course/jupyter_english/assignments_fall2019/Alice/site_dic.pkl'
data = []
with open(pkl, 'rb') as f:
    data = pickle.load(f)
for r in data:
    print(r)