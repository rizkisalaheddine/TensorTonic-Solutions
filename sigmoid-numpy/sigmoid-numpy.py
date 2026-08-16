import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    nom = np.ones_like(x)
    den = 1 + np.exp(-x)
    return nom/den