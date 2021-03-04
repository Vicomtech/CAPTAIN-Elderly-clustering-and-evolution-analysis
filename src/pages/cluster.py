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
import copy
import numpy as np

# Third-party app imports
from scipy.cluster.hierarchy import cut_tree
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Imports from your apps
from src.data.get_data import read_df_progression
from src.data.get_data import read_df_second_assessment_processed
from utils.aux_functions import define_color
from variables.parameters import ASSESSMENTS
from variables.parameters import dictionary_columns_inv
from variables.parameters import FEATURES
from variables.parameters import MAIN_COLS
from variables.parameters import TOTAL_STATICS
from variables.strings import TEXT_PARALLEL_COORDINATE
from variables.strings import PROGRESSION_SUB_SECTION
from variables.strings import TEXT_PROGRESSION
from variables.strings import TIP_PROGRESSION
from variables.strings import TEXT_PROGRESSION_2
from variables.strings import TEXT_PROGRESSION_CLUSTER
from variables.strings import TEXT_PROGRESSION_FOLLOW_UP
from variables.strings import TEXT_PROGRESSION_IMPROVE
from variables.strings import TEXT_SECOND_ASSESSMENT
from variables.weights import GLOBAL_FIELDS_PROGRESSION
from variables.weights import all_weights
from src.data.get_data import read_df_first_assessment
from src.data.get_data import read_df_first_assessment_normalized
# from src.data.get_data import extract_numeric_features_from_df
from utils.distances import distance
from variables.parameters import CLUSTER_BRANCH_DEFAULT_COLOR
from variables.parameters import CLUSTER_COLORS
from variables.parameters import GLOBAL_FIELDS
from variables.strings import DENDROGRAM_CAPTION
from variables.strings import DENDROGRAM_SUBSECTION
from variables.strings import DENDROGRAM_INFO
from variables.strings import DENDROGRAM_WARNING
from variables.strings import GROUP_STATISTICS_SUBSECTION
from variables.strings import TEXT_CLUSTER_DESCRIPTION
from variables.strings import TEXT_CLUSTER_TIP
from variables.strings import TEXT_PIE_CHART
from variables.strings import TEXT_RADAR_CHART
from variables.strings import SECTION_CLUSTER
from variables.strings import SECTION_IMPROVEMENT
from variables.strings import PAGE_CLUSTER
from variables.strings import FEATURE_RELEVANCE_INFO


def write():
    # LOAD DATA
    # get first assessment
    df_first_assessment = read_df_first_assessment()
    # get first assessment normalized
    df_first_assessment_normalized = read_df_first_assessment_normalized()

    # Evolution data
    df_progression_reduced = read_df_progression()
    df_second_assessment = read_df_second_assessment_processed()
    df_first_assessment['Evaluation date'] = pd.to_datetime(df_first_assessment['assessment_date'], format='%d/%m/%Y')

    # Cluster analysis
    st.title(PAGE_CLUSTER)
    st.write(SECTION_CLUSTER)

    if st.learning_mode:
        st.write(TEXT_CLUSTER_DESCRIPTION)
        st.info(TEXT_CLUSTER_TIP)
        st.write(DENDROGRAM_SUBSECTION)
        st.write(DENDROGRAM_CAPTION)
        st.info(FEATURE_RELEVANCE_INFO)

    clustering_feature_relevance_map = {
        "Very Low": 0,
        "Low": 0.5,
        "Medium": 1,
        "High": 1.5,
        "Very High": 2
    }
    default_values = __populate_clustering_category_sliders(weight_map=clustering_feature_relevance_map)
    weights, weights_difference = __populate_clustering_features_sliders(default_values=default_values,
                                                                         weight_map=clustering_feature_relevance_map)

    dendrogram_column_layout = st.beta_columns(2)

    linked, max_distance = __agglomerative_clustering(df_normal=df_first_assessment_normalized, weights=weights)
    default_dissimilarity = float(round(max_distance * 0.9, 2))
    if st.learning_mode:
        st.info(DENDROGRAM_INFO)
        st.warning(DENDROGRAM_WARNING)
        selected_distance = st.slider("Choose group distinction level", 0.00, max_distance + 0.01,
                                      default_dissimilarity)
    else:
        with dendrogram_column_layout[0]:
            selected_distance = st.slider("Choose group distinction level", 0.00, max_distance + 0.01,
                                          default_dissimilarity)

    # Dendogram
    tree_cut = cut_tree(linked, height=selected_distance)
    k = len(np.unique(tree_cut))
    if st.learning_mode:
        st.write(
            f"You have categorized the older adult population into **{k} {'group' if k==1 else 'groups'}** using the "
            f"**{selected_distance:.2f} value** in the slider above"
        )
        st.write("")
    else:
        with dendrogram_column_layout[0]:
            st.write(f"**{k} {'group' if k==1 else 'groups'}** using **{selected_distance:.2f} level**")

    if k > 10:
        st.error("**:no_entry: Too many clusters (>10), please choose a higher distinction level.**")
    else:

        label_list = df_first_assessment['User ID'].to_list()

        fig_dendrogram, ax_cluster = plt.subplots()
        ax_cluster.set_ylabel('Dissimilarity')
        fig_dendrogram.figsize = (10, 7)
        __create_dendogram(linked=linked, tree_cut=tree_cut, label_list=label_list, selected_distance=selected_distance)

        if st.learning_mode:
            st.pyplot(fig_dendrogram)
        else:
            with dendrogram_column_layout[0]:
                st.pyplot(fig_dendrogram)

        if st.learning_mode:
            st.write(GROUP_STATISTICS_SUBSECTION)

        cluster_list = ['Group ' + str(x[0]) for x in tree_cut]
        clusters_names = ['Group ' + str(i) for i in range(k)]
        df_first_assessment['clusters'] = cluster_list
        df_first_assessment_normalized['clusters'] = cluster_list
        # Pie Chart
        if st.learning_mode:
            st.write(TEXT_PIE_CHART)
        fig_pie = __create_pie_chart(cluster_list, clusters_names, k=k)
        if st.learning_mode:
            st.plotly_chart(fig_pie)
        else:
            with dendrogram_column_layout[1]:
                st.plotly_chart(fig_pie)

        # Radar Chart
        if st.learning_mode:
            st.write(TEXT_RADAR_CHART)

        # agree_radar = st.checkbox('I want to choose which dimensions/variables to visualize')
        # if agree_radar:
        _all_dimension_names = list(GLOBAL_FIELDS.keys())
        variables_to_show_radar = []
        for variable_to_show in st.multiselect(
                label='',  # Select which dimension features to see
                options=_all_dimension_names, default=_all_dimension_names):
            variables_to_show_radar += GLOBAL_FIELDS[variable_to_show]

        if len(variables_to_show_radar) > 2:
            fig_radar = __create_radar_chart(df_normal=df_first_assessment_normalized,
                                             variables_to_show_radar=variables_to_show_radar)
            st.plotly_chart(fig_radar, use_container_width=True)

        # IMPROVEMENT

        # Second assessment
        st.write(SECTION_IMPROVEMENT)
        if st.learning_mode:
            st.write(TEXT_SECOND_ASSESSMENT)

        # Improvement

        # Parallel coordinates
        if st.learning_mode:
            st.write(TEXT_PARALLEL_COORDINATE)

        df_differences = __build_df_differences(
            df=df_first_assessment,
            df_second_assessment=df_second_assessment,
            weights_difference=weights_difference
        )

        fig_parallel = __create_parallel_coordinates(df_differences, k)
        st.plotly_chart(fig_parallel, use_container_width=True)

        # Progression
        if st.learning_mode:
            st.write(PROGRESSION_SUB_SECTION)
            st.write(TEXT_PROGRESSION)
            st.info(TIP_PROGRESSION)
            st.write(TEXT_PROGRESSION_2)

        param_col_layout_top = st.beta_columns(3)
        param_col_layout_bottom = st.beta_columns(2)
        with param_col_layout_top[0]:
            select_cluster = st.selectbox(
                TEXT_PROGRESSION_CLUSTER,
                list(df_differences['Cluster'].unique()) + ['All']
            )
        with param_col_layout_bottom[0]:
            variable_to_show = st.selectbox(TEXT_PROGRESSION_FOLLOW_UP,
                                            list(GLOBAL_FIELDS_PROGRESSION.keys()))
        with param_col_layout_bottom[1]:
            variable_to_color = st.selectbox(TEXT_PROGRESSION_IMPROVE,
                                             list(GLOBAL_FIELDS.keys()))

        with param_col_layout_top[2]:
            group_by = st.selectbox("How to group close days",
                                    ['mean', 'max', 'min', 'No grouping']
                                    )
        with param_col_layout_top[1]:
            n_days = st.selectbox("Number of days to group",
                                  [1, 3, 5, 7, 9], 3)

        # center_color_in_0 = st.selectbox("I want to centre the color in 0 or progressive",
        #                                  ['In 0', 'Progressive'], 0)

        center_color_in_0 = 'In 0'
        df_progression_cluster_reduced = __adapt_df_progression(df_differences, df_progression_reduced, select_cluster)
        fig_progression_reduced = __create_progress_line_chart(
            df_differences,
            df_progression_cluster_reduced,
            variable_to_color,
            variable_to_show,
            by=group_by,
            n_days=n_days,
            center_color_in_0=center_color_in_0
        )
        st.plotly_chart(fig_progression_reduced, use_container_width=True)


def __agglomerative_clustering(df_normal, weights):
    distance_matrix = pdist(df_normal, metric=distance, weights=weights)
    linked = linkage(distance_matrix, method='average')
    distances = list()
    for link in linked:
        distances.append(link[2])
    return linked, max(distances)


def __create_dendogram(linked, tree_cut, label_list, selected_distance):
    d_leaf_colors = {}
    for i in range(len(tree_cut)):
        d_leaf_colors[label_list[i]] = CLUSTER_COLORS[tree_cut[i][0]]
    # next is same as on the link
    # https://stackoverflow.com/questions/38153829/custom-cluster-colors-of-scipy-dendrogram-in-python-link-color-func
    link_cols = {}
    for i, i12 in enumerate(linked[:, :2].astype(int)):
        c1, c2 = (link_cols[x] if x > len(linked) else d_leaf_colors[label_list[x]]
                  for x in i12)
        link_cols[i + 1 + len(linked)] = c1 if c1 == c2 else CLUSTER_BRANCH_DEFAULT_COLOR

    return __fancy_dendrogram(
        linked,
        max_d=selected_distance,
        no_labels=True,
        link_color_func=lambda x: link_cols[x]
    )


def __fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    ddata = dendrogram(*args, **kwargs)
    if max_d:
        plt.axhline(y=max_d, c='k')
    return ddata


def __create_pie_chart(cluster_list, clusters_names, k):
    cluster_counts = [cluster_list.count(cluster_name) for cluster_name in clusters_names]
    cluster_colors = [CLUSTER_COLORS[i] for i in range(k)]
    trace = go.Pie(labels=clusters_names, values=cluster_counts)
    data = [trace]
    fig_pie = go.Figure(data=data)
    fig_pie.update_traces(marker=dict(colors=cluster_colors))
    return fig_pie


def __create_radar_chart(df_normal, variables_to_show_radar):
    df_radar = pd.DataFrame(df_normal[variables_to_show_radar + ['clusters']].groupby(['clusters']).mean()).transpose()
    # st.write(df_radar)
    min_radar = df_radar.min().min()
    max_radar = df_radar.max().max()

    max_limit = max_radar + (max_radar - min_radar) * 0.2
    min_limit = min_radar - (max_radar - min_radar) * 0.2

    categories = df_radar.index.tolist()

    fig_radar = go.Figure()

    for radar_clust in list(df_radar.columns.tolist()):
        fig_radar.add_trace(go.Scatterpolar(
            r=list(df_radar[radar_clust]),
            theta=categories,
            fill='toself',
            name=radar_clust,
            fillcolor=CLUSTER_COLORS[int(radar_clust[-1])],
            marker_color=CLUSTER_COLORS[int(radar_clust[-1])],
            opacity=0.6
        ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[min_limit, max_limit]
            )),
        showlegend=True
    )
    return fig_radar


def __adapt_df_progression(df_differences, df_progression, select_cluster):
    if select_cluster in list(df_differences['Cluster']):
        ids_to_show_progression = df_differences[df_differences['Cluster'] == select_cluster]['User ID'].unique()
    else:
        ids_to_show_progression = df_differences['User ID'].unique()
    df_progression_cluster = df_progression[
        df_progression['User ID'].apply(lambda x: x in list(ids_to_show_progression))]
    return df_progression_cluster


def __extract_by(group_vals, by):
    if by == 'mean':
        return np.nanmean(group_vals)
    elif by == 'max':
        return np.nanmax(group_vals)
    elif by == 'min':
        return np.nanmin(group_vals)
    else:
        return group_vals[len(group_vals)//2]


def __group_values_among_near_days(ordered_values, by='mean', n_days=3):
    grouped_vals = list()
    for i in range(len(ordered_values)):
        days_before = n_days//2
        group_vals = list()
        for j in range(n_days):
            loc = i - days_before + j
            if 0 <= loc < len(ordered_values):
                group_vals.append(ordered_values[loc])
        grouped_vals.append(__extract_by(group_vals, by))
    return grouped_vals


def __create_progress_line_chart(df_differences, df_progression_cluster, variable_to_color, variable_to_show,
                                 by, n_days, center_color_in_0):
    fig_progression = go.Figure()
    max_ = np.percentile(list(df_differences[variable_to_color]), 90)
    min_ = np.percentile(list(df_differences[variable_to_color]), 10)
    for user in list(df_progression_cluster['User ID'].unique()):
        df_user_progression = df_progression_cluster[df_progression_cluster['User ID'] == user].sort_values(
            'goal_day')
        val = df_differences[df_differences['User ID'] == user][variable_to_color].iloc[0]
        fig_progression.add_trace(
            go.Scatter(
                x=df_user_progression['goal_day'],
                y=__group_values_among_near_days(df_user_progression[variable_to_show].to_list(), by=by, n_days=n_days),
                line_color=define_color(val, max_=max_, min_=min_, center_color_in_0=center_color_in_0),
                name=user,
            )
        )
    fig_progression.update_layout(
        title="Progression",
        xaxis_title='Days since the beginning of the programme',
        yaxis_title=str(variable_to_show) + ' effort level',
        legend_title="Users in group"
    )
    return fig_progression


def __create_parallel_coordinates(df_differences, k):
    fig_parallel = go.Figure(data=go.Parcoords(
        line=dict(color=df_differences['Cluster'],
                  colorscale=[CLUSTER_COLORS[i] for i in range(k)]
                  ),
        dimensions=list([
            dict(range=[df_differences[col].min(), df_differences[col].max()],
                 label=col, values=df_differences[col]) for col in MAIN_COLS])
    )
    )
    fig_parallel.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    return fig_parallel


def __build_df_differences(df, df_second_assessment, weights_difference):
    columns = TOTAL_STATICS + ['Evaluation date start', 'Evaluation date end']
    for ass in FEATURES:
        columns = columns + [ass + ' start', ass + ' end', ass + ' diff']
    df_unified = pd.DataFrame(columns=columns)
    df_differences = \
        pd.DataFrame(
            columns=['User ID', 'Evaluation date start', 'Evaluation date end'] + FEATURES + ['Cluster']
        )
    for user in df_second_assessment['User ID'].unique().tolist():
        # df_user = df_second_assessment[df_second_assessment['User ID'] == user]
        # df_before = df_user[df_user['Evaluation date'] == df_user['Evaluation date'].min()]
        # df_after = df_user[df_user['Evaluation date'] == df_user['Evaluation date'].max()]
        df_before = df[df['User ID'] == user]
        df_after = df_second_assessment[df_second_assessment['User ID'] == user]
        instancia = \
            list(df_before[TOTAL_STATICS].iloc[0]) + \
            [df_before['Evaluation date'].iloc[0]] + \
            [df_after['Evaluation date'].iloc[0]]
        instancia_solo_diferencia = [user, df_before['Evaluation date'].iloc[0],
                                     df_after['Evaluation date'].iloc[0]]
        for ass in FEATURES:
            instancia = \
                instancia + \
                [df_before[ass].iloc[0]] + \
                [df_after[ass].iloc[0]] + \
                [df_after[ass].iloc[0] - df_before[ass].iloc[0]]
            instancia_solo_diferencia = instancia_solo_diferencia + [df_after[ass].iloc[0] - df_before[ass].iloc[0]]
        clst = df['clusters'][df['User ID'] == user]

        instancia_solo_diferencia = instancia_solo_diferencia + [int(clst.iloc[0][-1])]
        df_unified.loc[len(df_unified)] = instancia
        df_differences.loc[len(df_differences)] = instancia_solo_diferencia

    df_differences['Physical'] = 0
    df_differences['Cognitive'] = 0
    df_differences['Nutritional'] = 0
    df_differences['Manual'] = 0

    all_weights['Manual'] = weights_difference

    for col in MAIN_COLS:
        for i in range(len(ASSESSMENTS)):
            w = all_weights.get(col).get(dictionary_columns_inv.get(ASSESSMENTS[i]), 0)
            assm = copy.copy(df_differences[ASSESSMENTS[i]])
            assm = assm.fillna(0)
            df_differences[col] += assm * w

    return df_differences


def __populate_clustering_category_sliders(weight_map):
    default_values = dict()
    default_options = list(weight_map.keys())
    default_option = default_options[
        int((len(default_options) - 1) / 2)
    ]
    index = 0
    category_relevance_columns = st.beta_columns(len(GLOBAL_FIELDS.keys()))
    for category, features in GLOBAL_FIELDS.items():
        with category_relevance_columns[index]:
            st.subheader(category)
            weight = st.select_slider(
                "",
                options=default_options,
                value=default_option,
                key=index
            )
            with st.beta_expander(label='', expanded=False):
                for feature in features:
                    default_values[feature] = st.select_slider(
                        feature,
                        options=default_options,
                        value=weight)
        index += 1

    return default_values


def __populate_clustering_features_sliders(default_values, weight_map):
    weights = list()
    weights_difference = dict()
    for feature in FEATURES:
        # next is to go on, but this function originally was to add weights one by one, now it is not usefull but for
        # for format things I am maintaining it
        aux = default_values.get(feature, 1.0)
        weights.append(weight_map[aux])
        if feature in ASSESSMENTS:
            weights_difference[feature] = weight_map[aux]
    return weights, weights_difference
