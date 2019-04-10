# Machine-learning-utilities
A module written in Python containing usual functions for machine learning projects using scikit-learn.

1-The preprocessing helper module contains helpers which can be used during the preprocessing step in a project
  * preprocessing_helper.py:
    - detecte_outliers: function for detecting/deleting(optionaly) outliers using interquartile method.
    
      -params:
        -f(str) the name feature in which you want to detect outliers.
        -df(pandas.DataFrame) the pandas dataframe representing your data.
        -delete_outliers(bool) whether or not delete the deteced outliers, default False.
             
      -return: the list of ouliers and the new dataframe(if delete_outliers is set to true)
   
   
2-The 
