import pandas as pd
import os
from numpy import percentile
from numpy import nanmean
from numpy import nanstd
from variables.data_paths import PATH_TO_DF_FIRST_ASSESSMENT
from variables.data_paths import PATH_TO_DF_FIRST_ASSESSMENT_CALCULATED
from variables.data_paths import PATH_TO_DF_PROGRESSION_CALCULATED
from variables.data_paths import PATH_TO_DF_SECOND_ASSESSMENT
from variables.data_paths import PATH_TO_DF_SECOND_ASSESSMENT_CALCULATED
from variables.parameters import FEATURES
from variables.parameters import TOTAL_STATICS

"""
Chache method does not work as if we change any parameter that is originated with a function with cache, it does not
like it. So that, I make the calculations once and save those in "calculated" folder, which works as cache. When
production, only this folder will be used and the except scripts will be in excess.

"""


def check_folder_create_if_needed():
    path = './data/calculated'
    if not os.path.isdir(path):
        os.mkdir(path)


def read_df_first_assessment():
    return pd.read_csv(PATH_TO_DF_FIRST_ASSESSMENT)


def read_df_second_assessment():
    return pd.read_csv(PATH_TO_DF_SECOND_ASSESSMENT)


def read_df_progression():
    df_progression_reduced = pd.read_csv(PATH_TO_DF_PROGRESSION_CALCULATED)
    return df_progression_reduced


def read_df_first_assessment_normalized():
    try:
        df_normal = pd.read_csv(PATH_TO_DF_FIRST_ASSESSMENT_CALCULATED, index_col=0)
    except FileNotFoundError:
        df_normal = __calculate_df_first_assessment_normalized()
        check_folder_create_if_needed()
        df_normal.to_csv(PATH_TO_DF_FIRST_ASSESSMENT_CALCULATED)
    return df_normal


def read_df_second_assessment_processed():
    try:
        df_normal = pd.read_csv(PATH_TO_DF_SECOND_ASSESSMENT_CALCULATED, index_col=0)
    except FileNotFoundError:
        df_normal = __process_df_second_assessment()
        check_folder_create_if_needed()
        df_normal.to_csv(PATH_TO_DF_SECOND_ASSESSMENT_CALCULATED)
    return df_normal


def __process_df_second_assessment():
    df_second_assessment = pd.read_csv(PATH_TO_DF_SECOND_ASSESSMENT, index_col=0)
    df_second_assessment['Evaluation date'] = pd.to_datetime(
        df_second_assessment['assessment_date'],
        format='%d/%m/%Y'
    )
    df_second_assessment = df_second_assessment.fillna(df_second_assessment.mean(numeric_only=True))
    return df_second_assessment


def extract_numeric_features_from_df(df):
    return [x for x in FEATURES if df[x].dtype == 'int64' or df[x].dtype == 'float64']


def get_mean_std_without_outliers(vec, range_iqr=1.5):
    """
    Returns the mean and std of each column to normalize it. It estimate these without taking into
    account the outlier values.
    https://gist.github.com/joseph-allen/14d72af86689c99e1e225e5771ce1600
    :param vec: it is the numeric vector, the column
    :param range_iqr: by default 1.5, it is a range to detect the outliers
    :return: mean and std
    """
    q1 = percentile(vec, 25)
    q3 = percentile(vec, 75)
    iqr = (q3 - q1) * range_iqr
    condition = [q1 - iqr <= v <= q3 + iqr for v in vec]
    return nanmean(vec.where(condition)), nanstd(vec.where(condition))


def normalize_without_outliers_column(column):
    mean_, std_ = get_mean_std_without_outliers(column.copy())
    return [(x - mean_)/std_ for x in list(column)]


def normalize_without_outliers(df_numeric):
    df_numeric = df_numeric.fillna(df_numeric.mean())
    return df_numeric.apply(lambda col: normalize_without_outliers_column(col), axis=0)


def __calculate_df_first_assessment_normalized():
    df = read_df_first_assessment()
    numeric = extract_numeric_features_from_df(df=df)
    df_normal = df[FEATURES]
    df_normal[numeric] = normalize_without_outliers(df[numeric])
    return df_normal.fillna(0)


def get_df_unified():
    columns = TOTAL_STATICS + ['Evaluation date start', 'Evaluation date end']
    for ass in FEATURES:
        columns = columns + [ass + ' start', ass + ' end', ass + ' diff']
    return pd.DataFrame(columns=columns)


def get_df_differences():
    return pd.DataFrame(
        columns=['User ID', 'Evaluation date start', 'Evaluation date end'] + FEATURES + ['Cluster']
    )
