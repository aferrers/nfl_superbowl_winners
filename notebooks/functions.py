import pandas as pd
import numpy as np
import scipy.stats as st


# define function: checking degree of normal distribution for numerical columns to consider 
# when looking for significant difference between various population means

def normaltest_mult_col(df: pd.DataFrame) -> str:
    '''
    This function, normaltest_mult_col(df), performs a normality test on each numerical column in a DataFrame df. 
    It selects numerical columns, performs a normality test on each, and prints the results. 
    Input: DataFrame 
    Output: string.
    
    '''
    df_num = df.select_dtypes(np.number)

    for col in df_num.columns:
        statistic, pvalue = st.normaltest(df_num[col])
        if pvalue >0.975:
            print(f'{col}:', statistic, (pvalue))
        elif pvalue < 0.025:
            print(f'{col}:', statistic, (pvalue))
    print('/n')

    
# Function for looking for significant difference between two populations' means. 
def ttest_ind_2(df1: pd.DataFrame, y: str, y_val, y_val2, random_state: int, significance_level: float=0.05):
    """
    Function: Split dataframes based on input in y column (binary) and compare statistical difference between each numerical column of split dataframe. 
    This is is done in order to identify potential X candidates for a logistic regression model to predict y outcomes. 
    Inputs: dataframe, name of y column, potential y value 1, potential y value 2, random state for scipy.stats.ttest_ind()
    Outputs: List of column names from dataframe that fall into the rejection zones and can be stated have means which are significantly different 
    from one another across y_value split
    """
    df1_num = df1.loc[df1[y] == y_val].select_dtypes(np.number)
    df2_num = df1.loc[df1[y] == y_val2].select_dtypes(np.number)
    for col in df1_num.columns:
        stat, pval = st.ttest_ind(df1_num[col], df2_num[col], axis=0, random_state=random_state)
        if pval > 1-(significance_level/2):
            print(col, stat, pval)
        elif pval < (significance_level/2):
            print(col, stat, pval)
            
            
# define function to check selected columns'. skewness

def col_skewness(df, columns):
    for col in columns:
        skewness = df[col].skew()
        if (skewness < 0.5 and skewness > -0.5):
            print(f'{col} skewness, close to symmetrical: ',skewness)
        elif (skewness > 0.5):
            print(f'{col} skewness, positive skewed: ',skewness)
        else:
            print(f'{col} skewness, negative skewed: ',skewness)