import pandas as pd
import numpy as np
import scipy.stats as st
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score


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


from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error, mean_squared_error, r2_score
          

# Create function to store metrics reports from model predictions
import pandas as pd

def class_error_metrics_report_m(model_1_name: str, y_test_1: list, y_test_pred_1: list, model_2_name: str = None, y_test_2: list = None, y_test_pred_2: list = None) -> pd.DataFrame:
    '''
    Function: Calculate the various error metrics for a given set of y_test and y_test_pred splits 
    and organises them into a DataFrame for easier visualization
    Inputs: model name: str, y_test: list, y_test_pred: list for two models (2nd optional) to be compared
    Outputs: DataFrame with metrics columns
    '''
    # Model 1 metrics
    error_metrics = {
        'Model Name': [model_1_name],
        'Accuracy': [accuracy_score(y_test_1, y_test_pred_1)],
        'Precision': [precision_score(y_test_1, y_test_pred_1, zero_division=0)],
        'Recall': [recall_score(y_test_1, y_test_pred_1)],
        'F1': [f1_score(y_test_1, y_test_pred_1)],
        'Kappa': [cohen_kappa_score(y_test_1, y_test_pred_1)]
    }

    # Model 2 Metrics if provided
    if model_2_name is not None:
        # Calculate metrics for model 2
        error_metrics['Model Name'].append(model_2_name)
        error_metrics['Accuracy'].append(accuracy_score(y_test_2, y_test_pred_2))
        error_metrics['Precision'].append(precision_score(y_test_2, y_test_pred_2, zero_division=0))
        error_metrics['Recall'].append(recall_score(y_test_2, y_test_pred_2))
        error_metrics['F1'].append(f1_score(y_test_2, y_test_pred_2))
        error_metrics['Kappa'].append(cohen_kappa_score(y_test_2, y_test_pred_2))

    # Create the report DataFrame
    report = pd.DataFrame(error_metrics)
    return report

if __name__ == "__main__":
			normaltest_mult_col()
			ttest_ind_2()
			col_skewness()
			class_error_metrics_report_m()
            