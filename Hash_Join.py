def hash_join(df1, df2):
    
    import pandas as pd
    if len(df1) <= len(df2):

        # Hashing phase
        # df1 is small, and df2 is large
        # hash_table = {row['obj']:row for _,row in df1.iterrows()}

        hash_table = {}
        for _,row in df1.iterrows():
            if row['obj'] not in hash_table:
                hash_table[row['obj']] = []
                hash_table[row['obj']].append(row)
            else:
                hash_table[row['obj']].append(row)

        # Probing phase
        data = []
        for _,row in df2.iterrows():
            if row['sub'] in hash_table:
                df1_sel = hash_table[row['sub']]
                df2_sel = row
                # data.append(pd.concat([df1_sel, df2_sel]))
                for i1 in df1_sel:
                    data.append(pd.concat([i1, df2_sel]))


    else:
        
        # Hashing phase
        # df1 is large, and df2 is small
        # hash_table = {row['sub']:row for _,row in df2.iterrows()}
        hash_table = {}
        for _,row in df2.iterrows():
            if row['sub'] not in hash_table:
                hash_table[row['sub']] = []
                hash_table[row['sub']].append(row)
            else:
                hash_table[row['sub']].append(row)

        # Probing phase
        data = []
        for _,row in df1.iterrows():
            if row['obj'] in hash_table:
                df1_sel = row
                df2_sel = hash_table[row['obj']]
                # data.append(pd.concat([df1_sel, df2_sel]))
                for i2 in df2_sel:
                    data.append(pd.concat([df1_sel, i2]))

    return pd.concat(data, axis = 1).transpose()


# hash_join(follows,friendOf)