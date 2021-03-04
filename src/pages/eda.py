# -*- coding: utf-8 -*-
"""
    smARt-cOAch (AROA): Stratification Tool (AROA-STRT)

    @description: Enables non-experts to build clusters of similar users and understand their evolution
    @author: Jon Kerexeta - Vicomtech Foundation, Basque Research and Technology Alliance (BRTA)
    @author: Andoni Beristain Iraola - Vicomtech Foundation, Basque Research and Technology Alliance (BRTA)
    @author: Roberto Álvarez Sánchez - Vicomtech Foundation, Basque Research and Technology Alliance (BRTA)
    @version: 0.1
"""

# Stdlib imports

from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Third-party app imports
import streamlit as st
from pandas import isnull as pd_isnull
import plotly.figure_factory as ff

# Imports from your apps
from src.data.get_data import read_df_first_assessment
from src.data.get_data import read_df_second_assessment
from variables.strings import DATA_DISTRIBUTION_INFO
from variables.strings import DATA_DISTRIBUTION_SUB_HEADER
from variables.strings import HINT_USER_INPUT
from variables.strings import MAIN_DESCRIPTION
from variables.strings import MAIN_INFO
from variables.strings import MAIN_TOTAL
from variables.strings import MISSING_RATE
from variables.strings import PAGE_EDA
from variables.strings import PAPER_INFO
from variables.strings import TEXT_MISSING_VALUES
from variables.strings import DATA_DISTRIBUTION_DESCRIPTION


def write():
    """
    # Streamlit documentation https://docs.streamlit.io/en/latest/api.html
    :return:
    """
    feature_categories = OrderedDict()
    feature_categories['Physical'] = ['foot_up_and_go', 'chair_sit_and_reach', 'chair_stand', 'back_scratch',
                                      'arm_curl', 'two_minute_step']
    feature_categories['Cognitive'] = ['MAI', 'MSC', 'MOCA']
    feature_categories['Nutritional'] = ['MNA_mini']

    st.title(PAGE_EDA)
    if st.learning_mode:
        st.write(MAIN_DESCRIPTION)
    if False:
        st.info(PAPER_INFO)
    # Dataset
    st.subheader(HINT_USER_INPUT)

    df = read_df_first_assessment()
    df = df[[col for col in df.columns if col not in ['User ID', 'assessment_date', 'dataset_source']]]
    df_is_nan = pd_isnull(df)
    df_without_nan = df.fillna(df.mean())

    df_2 = read_df_second_assessment()
    df_2 = df_2[[col for col in df_2.columns if col not in ['User ID', 'assessment_date', 'dataset_source']]]
    df_2_is_nan = pd_isnull(df_2)
    df_2_without_nan = df_2.fillna(df_2.mean())

    st.write(MAIN_TOTAL.format(df_without_nan.shape[0]))
    st.write(MISSING_RATE.format(float(df_is_nan.sum().sum())/df_is_nan.count().count(),
                                 float(df_2_is_nan.sum().sum())/df_2_is_nan.count().count()))

    if st.learning_mode:
        st.warning(TEXT_MISSING_VALUES)

    st.subheader(DATA_DISTRIBUTION_SUB_HEADER)

    if st.learning_mode:
        st.write(DATA_DISTRIBUTION_DESCRIPTION)
        st.info(DATA_DISTRIBUTION_INFO)

    # n_charts_per_row = 3
    for dimension_name, feat_name_list in feature_categories.items():
        with st.beta_expander(label=dimension_name, expanded=False):
            for feature in feat_name_list:
                first_feature = list(df_without_nan[feature])
                second_feature = list(df_2_without_nan[feature])
                # Group data together
                hist_data = [first_feature, second_feature]
                group_labels = ['First assessment', 'Second assessment']
                # Create distplot with custom bin_size
                fig = ff.create_distplot(
                    hist_data,
                    group_labels,
                    bin_size=[.1, .25, .5]
                )
                fig.update_layout(
                    title=f"{dimension_name}: {feature}",
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                    )
                )
                # Plot!
                st.plotly_chart(fig, use_container_width=True)

    # st.dataframe(df_without_nan.style.apply(__highlight_nan_imputation, bool_dataframe=df_is_nan, color='red',
    #                                         axis=None))
    if st.learning_mode:
        st.text("")
    st.write(MAIN_INFO)


@st.cache
def __highlight_nan_imputation(data, bool_dataframe, color='yellow'):
    """
    highlight the maximum in a Series or DataFrame
    :param data:
    :param bool_dataframe:
    :param color:
    :return:
    """
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        return [attr if v else '' for v in bool_dataframe]
    else:  # from .apply(axis=None)
        return pd.DataFrame(np.where(bool_dataframe, attr, ''),
                            index=data.index, columns=data.columns)


def __plot_histograms(column_list, data_first, data_second):
    num_bins = 20
    num_features = len(column_list)

    fig, ax = plt.subplots(nrows=1, ncols=num_features, figsize=(6, 2)) if num_features > 1 else \
        plt.subplots(figsize=(6, 2))
    for index in range(num_features):
        try:
            elem = ax[index] if num_features > 1 else ax
            elem.hist(data_first[column_list[index]].values, bins=num_bins, color='green', stacked=True,
                      label='1st assessment',
                      alpha=0.5)
            elem.hist(data_second[column_list[index]].values, bins=num_bins, color='red', stacked=True,
                      label='2nd assessment',
                      alpha=0.5)
            # elem.legend(prop={'size': 7})
            elem.set_title(column_list[index].replace('_', ' '), size=9)
        except Exception:
            pass
    return fig
