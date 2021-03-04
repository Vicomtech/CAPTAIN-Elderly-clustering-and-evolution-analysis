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
import pathlib

# Third-party app imports

# Imports from your apps
__BASE_PATH = str(pathlib.Path(pathlib.Path(__file__).parent.parent.absolute()))
PATH_TO_DF_PROGRESSION_CALCULATED = str(pathlib.Path(__BASE_PATH, "data/calculated/df_progression_processed.csv"))
PATH_TO_DF_FIRST_ASSESSMENT = str(pathlib.Path(__BASE_PATH, 'data/df_first_assessment_anonymous.csv'))
PATH_TO_DF_FIRST_ASSESSMENT_CALCULATED = str(pathlib.Path(__BASE_PATH,
                                                          "data/calculated/df_first_assessment_normalized.csv"))
PATH_TO_DF_SECOND_ASSESSMENT = str(pathlib.Path(__BASE_PATH, 'data/df_second_assessment_anonymous.csv'))
PATH_TO_DF_SECOND_ASSESSMENT_CALCULATED = str(pathlib.Path(__BASE_PATH, "data/calculated/df_second_assessment.csv"))
