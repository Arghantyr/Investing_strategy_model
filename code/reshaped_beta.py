"""
Given 3 constants:
-  left_limit:
    beginning of the beta distribution
-  xmax:
    x value for maximum value of the beta distritubion
-  right_limit:
    end of the beta distribution
    
and parameter 'a' of the beta distribution, reshapes the distribution such that the xmax is fixed.
"""


def var_b(a, xmax, left_limit, right_limit):
    scale = right_limit - left_limit
    var_b = 1 + (a - 1) * (scale + loc - xmax) / (xmax - loc)

    return var_b

def choose_1:
    """
    Given parameters of the beta distribution returns 1 randomly chosen variable.
    """
    return choice

def choose_n:
    """
    Given parameters of the beta distribution returns n randomly chosen variables.
    """
    return n_choices
