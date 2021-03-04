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

FEATURES = [
    "chair_stand",
    "arm_curl",
    "two_minute_step",
    "chair_sit_and_reach",
    "back_scratch",
    "foot_up_and_go",
    "MOCA",
    "MSC",
    "MAI",
    "MNA_mini",
]

ASSESSMENTS = FEATURES

GLOBAL_FIELDS = {
    # 'Clinical data': [
    # ],
    'Physical': [
        "chair_stand",
        "arm_curl",
        "two_minute_step",
        "chair_sit_and_reach",
        "back_scratch",
        "foot_up_and_go",
    ],
    'Cognitive': [
        "MOCA",
        "MSC",
        "MAI"
    ],
    'Nutritional': [
        'MNA_mini'
    ]
}


TOTAL_STATICS = [
    'User ID'
    # 'Gender',
    # 'Year of birth',
    # 'Education years',
    # 'Marital Status',
    # 'Live with',
    # 'Kind of support',
    # 'Medical condition'
]

MAIN_COLS = \
    [
        'Physical',
        'Cognitive',
        'Nutritional'
    ]


CLUSTER_COLORS = [
    "#B061FF",
    "#61ffff",
    'orchid',
    'lightsalmon',
    'tomato',
    'khaki',
    'palegreen',
    'skyblue',
    'mediumorchid',
    'indianred',
    'darkturquoise'
]

CLUSTER_BRANCH_DEFAULT_COLOR = "#808080"   # Unclustered gray

dictionary_columns = {
    'Weight': 'weight',
    'Height': 'height',
    'Chair Stand': 'chair_stand',
    'Arm Curl': 'arm_curl',
    'Two Minute Step': 'two_minute_step',
    'Chair Sit and Reach 1': 'chair_sit_and_reach1',
    'Chair Sit and Reach 2': 'chair_sit_and_reach2',
    'Chair Sit and Reach': 'chair_sit_and_reach',
    'Back Scratch 1': 'back_scratch_1',
    'Back Scratch 2': 'back_scratch_2',
    'Back Scratch': 'back_scratch',
    'Foot Up And Go 1': 'foot_up_and_go_1',
    'Foot Up And Go 2': 'foot_up_and_go_2',
    'Foot Up And Go': 'foot_up_and_go',
    'MoCA': "MOCA",
    'MSC - A': "MSC",
    'MAI': 'MAI',
    'Declarative Knowledge': "declarative_knowledge",
    'Procedural Knowledge': "procedural_knowledge",
    'Conditional Knowledge': "conditional_knowledge",
    'Planning': "planning",
    'Information Management Strategies': "Information_Management_Strategies",
    'Comprehension Monitoring': "Comprehension_Monitoring",
    'Debugging Strategies': "Debugging_Strategies",
    'Evaluation': "Evaluation",
    'MNA mini': "MNA_mini"
}

dictionary_columns_inv = {v: k for k, v in dictionary_columns.items()}
