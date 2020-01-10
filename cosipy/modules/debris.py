import numpy as np
from constants import *
import sys

def snowPresence(GRID):

    if debris_method == 'DouglasEtAl16':
        debrisFactor = method_Douglas()

    else:
        print('Debris parameterisation ', debris_method, ' not available, using default')
        debrisFactor = method_Douglas()

    return debrisFactor


def method_Douglas(GRID,evdiff):
    # evdiff is "s-i", i.e. number of days since last snowfall - see para below equation 4 in Oerlemans & Knap 1998. hours_since_sowfall is passed to it in cosipy_core.
    # Check if snow or ice
    ### Change this to check if debris is > 3cm. The lines below check the GRID dataset which is created in init.py
    ### Can we include another debris_init or additional lines in the inin script to produce a GRID_DEBRIS?
    if (GRID.get_node_density(0) <= snow_ice_threshold):
        # Get current snowheight from layer height
        ### Change this to Get current debris thickness
        idx = (next((i for i, x in enumerate(GRID.get_density()) if x >= snow_ice_threshold), None))
        h = np.sum(GRID.get_height()[0:idx])

        # Thickness dependant reduction factor as shown in Douglas et al. 2016.
        fDebris = np.exp(melt_reduction_coefficient * debrisThickness)

    else:
        # If no snow cover then set debris factor to 1, i.e. no change to melt rate.
        fDebris = 1

    return fDebris

### OTHER CHANGES ELSEWHERE IN MODEL.
### constants.py - line 12 new method added for debrs module.
###
