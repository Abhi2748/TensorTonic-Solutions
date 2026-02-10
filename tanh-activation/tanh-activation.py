import numpy as np
import math 

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    posex = np.exp(x)
    negex = np.exp(-x)
    return (posex-negex)/(posex+negex)
