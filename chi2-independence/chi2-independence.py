import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C)
    N = np.sum(C)
    E = np.ones(C.shape, dtype=float)
    for i in range(len(C)):
        for j in range(len(C[i])):
            Ri = np.sum(C[i])
            Cj = np.sum(np.transpose(C)[j])
            E[i][j] = Ri*Cj / N
            
    chi_square = np.sum(((C-E)**2)/E)
    return (chi_square,E)