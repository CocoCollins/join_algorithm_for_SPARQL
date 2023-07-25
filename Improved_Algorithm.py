import pandas as pd
def partition(df, par_num, par_col):  # par_num: The number of partitions / par_col: which column as the reference 
    df['par'] = df[par_col].apply(hash) % par_num    
    return [df[df['par'] == i].drop('par', axis = 1) for i in range(par_num)]

def par_hash_join(df1, df2, par_num):   

    data = []
    for i in range(par_num):
        df1_par = partition(df1, par_num, 'obj')[i]
        df2_par = partition(df2, par_num, 'sub')[i]
        if df1_par.empty is False and df2_par.empty is False:
            data.append(hash_join(df1_par, df2_par))  # We can subsitude the hash_join to sort_merge_join here
    
    return pd.concat(data)

par_hash_join(follows, friendOf, 2)