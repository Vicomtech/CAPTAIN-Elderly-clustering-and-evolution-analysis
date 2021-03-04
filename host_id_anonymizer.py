import random
import numpy as np
import pandas as pd


def __generate_random_mapping(user_id_list, out_id_tag='user'):
    user_id_set_anonymous = [f'{out_id_tag}_{index}' for index in range(len(user_id_list))]
    for _ in range(5):
        random.shuffle(user_id_set_anonymous)
    return dict(zip(user_id_list, user_id_set_anonymous))


def __anonymize_file(df, output_path, user_id_convertion_map, user_id_column_name='User ID'):
    # Modify the user id values
    df[user_id_column_name] = df[user_id_column_name].str.upper()
    # df[user_id_column_name].replace(to_replace=user_id_convertion_map, inplace=True)
    df[user_id_column_name] = df[user_id_column_name].apply(lambda x: user_id_convertion_map.get(x, np.nan))
    df = df[df[user_id_column_name] == df[user_id_column_name]]
    # shuffle the file rows
    df = df.sort_values(user_id_column_name)
    # reset the index of the table
    df.index = range(len(df))
    df.to_csv(output_path)


def main():
    df_first_assessment = pd.read_csv("data/df_first_assessment.csv")
    user_id_list = [a.upper() for a in list(set(df_first_assessment['User ID'].values))]
    id_conversion_map = __generate_random_mapping(user_id_list=user_id_list, out_id_tag='user')

    __anonymize_file(df=df_first_assessment, output_path='data/df_first_assessment_anonymous.csv',
                     user_id_column_name='User ID', user_id_convertion_map=id_conversion_map)
    __anonymize_file(df=pd.read_csv("data/df_second_assessment.csv"),
                     output_path='data/df_second_assessment_anonymous.csv',
                     user_id_column_name='User ID', user_id_convertion_map=id_conversion_map)
    __anonymize_file(df=pd.read_csv("data/numeric_joined.csv", index_col=0),
                     output_path='data/df_progression_anonymous.csv',
                     user_id_column_name='User ID', user_id_convertion_map=id_conversion_map)


if __name__ == "__main__":
    main()
