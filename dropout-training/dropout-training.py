import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    
    out = x.copy()
    #dp = np.ones_like(x)
    if rng != None : 
        vals = rng.random(np.shape(x))
    else : 
        vals = np.random.random(np.shape(x))
    #print(vals)
    #print(vals >= p)
    mask = 1/(1-p) * (vals >= p)
    #print(mask)
    out = np.multiply(out,mask)
    #print(out)
    #dp = 1/1-p * (out != 0)
    return (out,mask)