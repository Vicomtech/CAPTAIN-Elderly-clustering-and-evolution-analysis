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


def day_from_beginning(df, user, date):
    min_date = df[df['User ID'] == user]['datetime'].min()
    return (date - min_date).days


def define_color(val, max_=10, min_=-10, center_color_in_0='Progressive'):
    if center_color_in_0 == 'Progressive':
        middle_value = (max_ + min_)/2
    else:
        middle_value = 0
    if val >= middle_value:
        if val >= max_:
            return 'rgb(0, 255, 100)'
        else:
            val_extrapolated = int(255 * (max_ - val)/max_)
            return 'rgb({}, 255,100)'.format(val_extrapolated)
    else:
        if val <= min_:
            return 'rgb(255, 0, 100)'
        else:
            val_extrapolated = int(255 * (abs((min_ + val)/min_)))
            return 'rgb(255, {}, 100)'.format(val_extrapolated)
