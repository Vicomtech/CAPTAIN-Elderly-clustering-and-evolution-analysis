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

# Third-party app imports

# Imports from your apps


# https://gist.github.com/rxaviers/7360908  -> Markdown emojis

MAIN_TITLE = "Older adult population analysis in CAPTAIN"

MAIN_DESCRIPTION = """
The purpose of this app is to analyze the older adult population in the CAPTAIN system using interactive visualization
techniques. It allows non-expert users to create clusters, visualize their patterns and follow up the evolution of those
clusters after the stratification. It also allows final users to customize the relevance of every parameter or group
(nutrition, social, physical, and cognitive).
"""

MAIN_INFO = """
It is expected that thanks to these visualizations the carer will be able to:
- Identify useful characteristics to group the older adults in order to propose new personalized coaching plans
(plugins)
- Identify action patterns followed by older adults with positives and negative outcomes in the period.
- Identify relationships between actions in certain coaching domain with positive or negative effect in the outcome of
another coaching dimension.

All these findings will support the validation and refinement of SMART goal plans as well as support the design of new
plans.
"""

PAGE_EDA = "Step 1: Review assessment data"

# TODO: Once the paper is accepted fill this information with link and its information
PAPER_INFO = """
An exhaustive report has been made explaining the functioning and characteristics of this web-tool. In addition,
 a **usability test** has been carried out in which we have analysed its capabilities and shortcomings.
  All this has been submitted to a journal (**under revision**):
- **Article**: [Web-tool to elderly clustering and evolution analysis] (https://www.mdpi.com/journal/ijerph/special_issues/active_healthy_aging)
 (Currently this is the link to the special issue, if accepted the link to the article will be added.)
- **Special issue**: [Active Healthy Aging](https://www.mdpi.com/journal/ijerph/special_issues/active_healthy_aging)
- **Journal**: [MDPI](https://www.mdpi.com/)
"""

PAGE_CLUSTER = "Step 2: Group users and study evolution"

SECTION_CLUSTER = "## 2.A Group users"
SECTION_IMPROVEMENT = "## 2.B Study evolution"

SIDE_BAR_INFO = """
        This tool uses T7.3 data, pretending to be data collected by the CAPTAIN system in two ways: a) automatically
        during a period, b) through carer mediated assessment during the setup step and periodically for follow up.
        """

HINT_USER_INPUT = "Older adult assessment variables"

DATA_DISTRIBUTION_SUB_HEADER = "Variable distribution grouped by the different coaching dimensions " \
                               "(Physical, Cognitive and Nutritional)"

DATA_DISTRIBUTION_DESCRIPTION = """
The next charts show the histograms of all the assessment variables for the first and second assessment process.
It provides an overview of the population status, as well as a sense of its evolution during the period.
"""

DATA_DISTRIBUTION_INFO = """
:bulb:  To view the charts click on the coaching dimension you want to inspect.
All the charts show the data distribution in the first **(blue color)** and second **(orange color)** assessment.
"""


DENDROGRAM_SUBSECTION = """
### 2.A.1 Older adult group design based on dendrogram chart
"""

DENDROGRAM_CAPTION = """
This chart shows how similar older adults are among themselves based on the selected features and how they are grouped
based on the number of groups selected. Each color represents one group of older adults.
"""

FEATURE_RELEVANCE_INFO = """
:bulb:  Use the sliders below to choose the relevance of each dimension for user grouping. expand each **+** sign to
individually set the relevance of each feature on each dimension
"""

DENDROGRAM_INFO = """
:bulb:  Use the slider below to choose the distinction you want among the older adult groups. It will move the
horizontal black line up and down to cut the dendrogram and define the grouping.
"""

DENDROGRAM_WARNING = """
:warning: Due to readability reasons, the maximum allowed number of groups is 10, so if you choose a distinction level
too low, the dendrogram might not be depicted.
"""

TEXT_CLUSTER_DESCRIPTION = """
    The goal of this step is to select a user similarity criteria on the left panel and a number of groups to create,
    in order to group similar older adults, using preliminary assessment data.
"""

TEXT_CLUSTER_TIP = """
    :bulb:  For example, if we want to group older adults only based on _physical_ status, we can reduce the relevance
    of the rest of dimensions to zero. Or if we want to go into higher detail, we could, for example, increase the
    relevance of _chair_sit_and_reach_ variable.

    To select the relevance of each coaching dimension or variable, use the slider bars in the left panel.

    Then, you can check the characteristics of each group in the _Group statistics review_ section
"""

GROUP_STATISTICS_SUBSECTION = """
### 2.A.2 Group characteristics review
"""

TEXT_RADAR_CHART = """
In the next radar chart, each older adult group is represented by the mean for each feature, in order to compare them
and see the characteristics of each group.

It is also possible to select which features to view and also which groups to visualize, clicking on the groups to hide
"""

TEXT_PIE_CHART = """
The next pie chart shows the amount of older adults per group based on the selected features and number of groups.
It is linked to the dendrogram chart.
"""

TEXT_SLIDER_DENDROGRAM = """
Next we have a Dendrogram. This visualization represent the vicinity among the patients.
According the distance we have defined (the weights), the nearest patient between them are near in the bottom.
As we scroll up the tree, the next nearest patients/patients groups will be joined in the nodes.
"""

TEXT_SECOND_ASSESSMENT = """
The purpose of this step is to check the evolution of each of the selected groups from the preliminary assessment
to the final assessment. The outcomes are rated between high worsening to high improvement. For each of the older
adults in a group the visualizations permit comparing outcomes on each dimension with the amount of activities
carried out in certain coaching dimension
"""

TEXT_DIFFERENCE = """
In the next dataframe, we have the difference of the second assessment with the first. This way we have a way to
check if the users have improved or not after the follow up. In the final columns we have a general value that
makes a weighted sum to estimate if there have been any improvement or worsening in globally.
"""


TEXT_PARALLEL_COORDINATE = """
### 2.B.1 Summary of individual older adult outcomes using parallel coordinate

In this chart we represent the improvement/worsening of each patient. Each patient is represent with a line, colored
by its group color, and in the vertical axis there is a representation of the comparison between the preliminary and
final assessments. Those with high values in the vertical axis represent improvement in the period and low values
worsening.
"""

PROGRESSION_SUB_SECTION = """
### 2.B.2 Older adult evolution per group and relationship with activities carried out
"""
TEXT_PROGRESSION = """
Compare the daily activity on certain coaching dimension with the positive or negative evolution of the
assessment (between initial and final assessment) in the same or other coaching dimension.
"""

TIP_PROGRESSION = """
- **Vertical axis** represents the amount of activity for the selected dimension.
- **Horizontal axis** represents time in days.
- **Colour** represents whether the patient improved or not in the period, green representing high improvement and red
high worsening with intermediate colors.
"""

TEXT_PROGRESSION_2 = """
The next three configurable parameters represent:
- **Older adult group to show**: It will show only the patients of the selected group. These is done to see the
effects of different activity patterns for similar older adults.
- **Activities done in selected dimension (vertical axis)**: Show activities carried out during the period only for this
 dimension
- **Assessment dimension outcome (color)**: Select which assessment dimension outcome to review. Color goes from green
(high improvement) to red (high worsening). This is a comparison between the final and preliminary assessments related
to the selected field, same as parallel coordinate.
"""

TEXT_PROGRESSION_CLUSTER = "Older adult group"
TEXT_PROGRESSION_FOLLOW_UP = "Coaching dimension for activities done (vertical axis)"
TEXT_PROGRESSION_IMPROVE = "Coaching dimension for outcome review (color)"
TEXT_MISSING_VALUES = ":warning: All **missing values** have been replaced by the **average** of the variable"
MAIN_TOTAL = "This dataset contains data from **{}** older adults who underwent to two assessments spaced in time."
MISSING_RATE = "There is a **{:.1f}%** missing value rate for the first assessment and a **{:.1f}%** missing value " \
               "rate for the second assessment"
