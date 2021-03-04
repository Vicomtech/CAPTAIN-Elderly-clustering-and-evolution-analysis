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

all_weights = {
    'Physical': {
        'Chair Stand': 1,
        'Arm Curl': 1,
        'Two Minute Step': 1,
        'Chair Sit and Reach 1': 1,
        'Chair Sit and Reach 2': 1,
        'Back Scratch 1': 1,
        'Back Scratch 2': 1,
        'Foot Up And Go 1': 1,
        'Foot Up And Go 2': 1,
        'MoCA': 0,
        'MSC - A': 0,
        'MAI': 0,
        'Declarative Knowledge': 0,
        'Procedural Knowledge': 0,
        'Conditional Knowledge': 0,
        'Planning': 0,
        'Information Management Strategies': 0,
        'Comprehension Monitoring': 0,
        'Debugging Strategies': 0,
        'Evaluation': 0,
        'MNA mini': 0
    },
    'Cognitive': {
        'Chair Stand': 0,
        'Arm Curl': 0,
        'Two Minute Step': 0,
        'Chair Sit and Reach 1': 0,
        'Chair Sit and Reach 2': 0,
        'Back Scratch 1': 0,
        'Back Scratch 2': 0,
        'Foot Up And Go 1': 0,
        'Foot Up And Go 2': 0,
        'MoCA': 1,
        'MSC - A': 1,
        'MAI': 1,
        'Declarative Knowledge': 0,
        'Procedural Knowledge': 0,
        'Conditional Knowledge': 0,
        'Planning': 0,
        'Information Management Strategies': 0,
        'Comprehension Monitoring': 0,
        'Debugging Strategies': 0,
        'Evaluation': 0,
        'MNA mini': 0
    },
    'Nutritional': {
        'Chair Stand': 0,
        'Arm Curl': 0,
        'Two Minute Step': 0,
        'Chair Sit and Reach 1': 0,
        'Chair Sit and Reach 2': 0,
        'Back Scratch 1': 0,
        'Back Scratch 2': 0,
        'Foot Up And Go 1': 0,
        'Foot Up And Go 2': 0,
        'MoCA': 0,
        'MSC - A': 0,
        'MAI': 0,
        'Declarative Knowledge': 0,
        'Procedural Knowledge': 0,
        'Conditional Knowledge': 0,
        'Planning': 0,
        'Information Management Strategies': 0,
        'Comprehension Monitoring': 0,
        'Debugging Strategies': 0,
        'Evaluation': 0,
        'MNA mini': 1
    },
    'Manual': None
}

MAI = {
    'declarative_knowledge': 8,
    'procedural_knowledge': 4,
    'conditional_knowledge': 5,
    'planning': 7,
    'Information_Management_Strategies': 10,
    'Comprehension_Monitoring': 7,
    'Debugging_Strategies': 5,
    'Evaluation': 6
}

PHYSICAL = [
    ['How much light physical activity have you performed? [Morning (6am - 12pm)]', 1],
    ['How much light physical activity have you performed? [Afternoon (12pm - 6pm)]', 1],
    ['How much light physical activity have you performed? [Evening (6pm - 12am)]', 1],
    ['How much moderate physical activity have you performed? [Morning (6am - 12pm)]', 2],
    ['How much moderate physical activity have you performed? [Afternoon (12pm - 6pm)]', 2],
    ['How much moderate physical activity have you performed? [Evening (6pm - 12am)]', 2],
    ['How much vigorous physical activity have you performed? [Morning (6am - 12pm)]', 3],
    ['How much vigorous physical activity have you performed? [Afternoon (12pm - 6pm)]', 3],
    ['How much vigorous physical activity have you performed? [Evening (6pm - 12am)]', 3]
]

COGNITIVE = [
    ['Have you been outside your house?', 1],
    ['Have you eaten one or more meals outside of home?', 1],
    ['Have you been to a shop?', 1],
    ['Have you prepared your own food at least once?', 1],
    ['Have you practiced an artistic pastime?', 1],
    ['Have you read anything?', 1],
    ]

SOCIAL = [
    ['How many people have you ... ? (Excluding the interviewer, if any) [...met?]', 3],
    ['How many people have you ... ? (Excluding the interviewer, if any) [...talked on the phone with?]', 2],
    ['How many people have you ... ? (Excluding the interviewer, if any) [...texted?]', 1],
    ['Have you been outside your house?', 2],
    ['Have you been to a shop?', 2],
    ['Consider the social interactions you had, what would you prefer?', 2]
]

NUTRITIONAL = [
    ['Have you eaten one or more meals outside of home?', 1],
    ['Have you prepared your own food at least once?', 1],
    ['How many times have you added sugar to anything you have eaten?', -1],
    ['How many times have you added salt to anything you have eaten or drunk?', -2],
    ['How much water did you have? (Please note that soft drinks, juices, and alcoholic drinks do not qualify). ', 2],
    ['How many units of alcohol did you have?', -2],
    ['How many times did you eat something during the day?', 1],
    ['How satisfied were you when you stopped eating?', 3],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Vegetables and Fruits (1/3)]', 2],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[ Dairy Products (1/8)]', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Bread, Cereals and Potatoes (1/3)]', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Oils (1/12)]', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Meat, Fish and Eggs (1/8)]', 2],
    ['What have you eaten?.1', 3],
    ['How satisfied were you when you stopped eating?.1', 3],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Vegetables and Fruits (1/3)].1', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Dairy Products (1/8)]', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Bread, Cereals and Potatoes (1/3)].1', -2],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Oils (1/12)].1', -1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Meat, Fish and Eggs (1/8)].1', 2],
    ['What have you eaten?.2', 3],
    ['How satisfied were you when you stopped eating?.2', 3],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Vegetables and Fruits (1/3)].2', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Dairy Products (1/8)].1', 1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Bread, Cereals (1/3)]', -2],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Oils (1/12)].2', -1],
    ['Did you have more or less of each of the food groups shown in the picture below? '
     '[Meat, Fish and Eggs (1/8)].2', 2]
]


GLOBAL_FIELDS_PROGRESSION = {
    'Physical': PHYSICAL,
    'Cognitive': COGNITIVE,
    'Social': SOCIAL,
    'Nutritional': NUTRITIONAL
}
