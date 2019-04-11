import numpy as np

def detecte_ouliers(f,df, r=1.5,  delete_outliers=False):
    """
        Removing outliers from the selected feature.
        Params:
            f: a string representing the name of the feature
            df: a DataFrame object representing the data
            r: a float representing the size of the cut_off
            delete_outliers: a boolean which let one choose whether or not
                to delete the outliers found
    """
    # a new DataFrame resulting from the outliers deletion
    new_df = None

    # the selected feature
    s = df[f]

    q25, q75 = np.percentile(s, 25), np.percentile(s, 75)
    s_iqr = q75 - q25
    s_cut_off = r*s_iqr
    s_lower, s_upper = q25 - s_cut_off, q75 + s_cut_off
    s_outliers = [x for x in s if x < s_lower or x > s_upper]
    if delete_outliers:
        new_df = df.drop(df[(s < s_lower) | (s > s_upper)].index)
    return s_outliers, new_df
