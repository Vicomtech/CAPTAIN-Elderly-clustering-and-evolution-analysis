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
import numpy as np

# Third-party app imports

# Imports from your apps


def dist_2_variables(var_1, var_2, weigth):
    assert var_1.__class__ == var_2.__class__
    class_ = var_1.__class__
    if isinstance(var_1, int) or isinstance(var_1, float):
        dist_aux = abs(var_1 - var_2)
    elif isinstance(var_1, str):
        if var_1 == var_2:
            dist_aux = 0
        else:
            dist_aux = 1
    else:
        print(class_)
        dist_aux = 0  # just in case if it is date or whatever
    return weigth * dist_aux


def distance(vec_1, vec_2, weights):
    # assert len(vec_1) == len(vec_2) == len(weights)
    dist = []
    for i in range(len(vec_1)):
        d = dist_2_variables(
            var_1=vec_1[i],
            var_2=vec_2[i],
            weigth=weights[i]
        )
        dist.append(d)
    return np.mean(dist)
