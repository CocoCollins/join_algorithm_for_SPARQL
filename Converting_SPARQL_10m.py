import rdflib
import pandas as pd

g = rdflib.Graph()
g.parse('watdiv.10M.nt', format = 'nt')

data = []
for sub, pro, obj in g:
    sub = str(sub).split('/')[-1]
    pro = str(pro).split('/')[-1]
    obj = str(obj).split('/')[-1]
    data.append([sub, pro, obj])
df2 = pd.DataFrame(data, columns = ['sub','pro','obj'])

# Here we also generate a dictionary to convert the string to integer
d1 = {}
curid = 0
for i in df2['sub']:
    if i not in d1:
        d1[i] = curid
        curid += 1
for j in df2['obj']:
    if j not in d1:
        d1[j] = curid
        curid += 1

df3 = pd.DataFrame()
df3['sub'] = df2['sub'].apply(lambda x:d1[x])
df3['pro'] = df2['pro']
df3['obj'] = df2['obj'].apply(lambda x:d1[x])

# Then we can generate 4 dataframes!
follows1 = df3[df3['pro'] == 'follows'][['sub','obj']].reset_index(drop = True)
friendOf1 = df3[df3['pro'] == 'friendOf'][['sub','obj']].reset_index(drop = True)
likes1 = df3[df3['pro'] == 'likes'][['sub','obj']].reset_index(drop = True)
hasReview1 = df3[df3['pro'] == 'rev#hasReview'][['sub','obj']].reset_index(drop = True)