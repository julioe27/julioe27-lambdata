import pandas

def enlarge(n):
    return 100*n

 # it's important to not have global junk when using your function

def df_nulls(df):
    return df.loc[:,df.isna().any()]