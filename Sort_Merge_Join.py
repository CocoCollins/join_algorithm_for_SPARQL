def sort_merge_join(df1, df2):

    import pandas as pd
    
    # sort phase
    df1 = df1.sort_values(by = 'obj').reset_index(drop = True)
    df2 = df2.sort_values(by = 'sub').reset_index(drop = True)
    
    # merge phase
    i = 0
    j = 0
    data = []
    while i < len(df1) and j < len(df2):
        if df1.loc[i,'obj'] == df2.loc[j,'sub']:
            curj = j
            loop_flg = 0
            data.append(pd.concat([df1.iloc[i], df2.iloc[j]]))
            if curj != len(df2) - 1:
                while df1.loc[i,'obj'] == df2.loc[curj+1,'sub']:
                    loop_flg = 1 
                    data.append(pd.concat([df1.iloc[i], df2.iloc[curj+1]]))
                    curj += 1
                    if curj == len(df2) - 1:
                        break
            if loop_flg == 0:  # No loop
                i += 1
                j += 1
            else:
                i += 1
        elif df1.loc[i,'obj'] < df2.loc[j,'sub']:
            i += 1
        else:
            j += 1
    return pd.concat(data, axis = 1).transpose()

#sort_merge_join(follows, friendOf)