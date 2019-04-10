import numpy as np

def detecte_ouliers(f,df, delete_outliers=False):
    new_df = None
    s = df[f]
    q25, q75 = np.percentile(s, 25), np.percentile(s, 75)
    s_iqr = q75 - q25
    s_cut_off = 1.5*s_iqr
    s_lower, s_upper = q25 - s_cut_off, q75 + s_cut_off
    s_outliers = [x for x in s if x < s_lower or x > s_upper]
    if delete_outliers:
        new_df = df.drop(df[(s < s_lower) | (s > s_upper)].index)
    return s_outliers, new_df
