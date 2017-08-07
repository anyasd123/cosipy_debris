#!/usr/bin/python

import numpy as np
from constants import *


def updateAlbedo(GRID, evdiff):
    """ This methods updates the albedo """

    # Check if snow or ice
    if (GRID.get_rho_node(0) <= snowIceThres):
    
        # Get current snowheight from layer height 
        idx = (next((i for i, x in enumerate(GRID.get_rho()) if x >= snowIceThres), None) )
        h = np.sum(GRID.get_hlayer()[0:idx])
    
        # Surface albedo according to Oerlemans & Knap 1998, JGR)
        alphaSnow = alphaFirn + (alphaFreshSnow - alphaFirn) * \
                np.exp((-evdiff)/(tscale*24.0))
        alphaMod = alphaSnow + (alphaIce - alphaSnow) * \
                np.exp((-1.0*h)/(depscale/100.0))
    
    else:
    
        # If no snow cover than set albedo to ice albedo
        alphaMod = alphaIce


    return alphaMod


### idea; have a deeper look if it would by worthwhile; albedo decay like (Brock et al. 2000)
### Schmidt et al 2017 >doi:10.5194/tc-2017-67, 2017 use the same albedo parameterisation from Oerlemans and Knap 1998 with a slight updated implementation of considering the surface temperature?