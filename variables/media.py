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
from PIL import Image

# Imports from your apps


__BASE_PATH = str(pathlib.Path(pathlib.Path(__file__).parent.parent.absolute()))
CAPTAIN_LOGO = Image.open(str(pathlib.Path(__BASE_PATH, 'media', 'captain logo_COLOR-01.ico')))
