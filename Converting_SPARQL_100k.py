import pandas as pd

df = pd.read_csv('100k.txt', sep = '\t', header = None)
df[2] = df[2].str.rstrip('.').str.rstrip()
df[['01', '02']] = df[0].str.split(':', expand = True)
df[['11', '12']] = df[1].str.split(':', expand = True)
df[['21', '22']] = df[2].str.split(':', expand = True)
df = df[['02', '12', '22']]
df = df.rename(columns = {'02':'sub', '12':'pro', '22':'obj'})

# first, we can make a dictionary to convert the string to integer
d = {}
curid = 0
for i in df['sub']:
    if i not in d:
        d[i] = curid
        curid += 1
for j in df['obj']:
    if j not in d:
        d[j] = curid
        curid += 1

# Next we can generate a new dataframe
df1 = pd.DataFrame()
df1['sub'] = df['sub'].apply(lambda x:d[x])
df1['pro'] = df['pro']
df1['obj'] = df['obj'].apply(lambda x:d[x])

# Then we can generate 4 dataframes!
follows = df1[df1['pro'] == 'follows'][['sub','obj']].reset_index(drop = True)
friendOf = df1[df1['pro'] == 'friendOf'][['sub','obj']].reset_index(drop = True)
likes = df1[df1['pro'] == 'likes'][['sub','obj']].reset_index(drop = True)
hasReview = df1[df1['pro'] == 'hasReview'][['sub','obj']].reset_index(drop = True)