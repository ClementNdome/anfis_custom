import numpy as np
from skfuzzy import gaussmf, gbellmf, sigmf

class MemFuncs:
    funcDict = {'gaussmf': gaussmf, 'gbellmf': gbellmf, 'sigmf': sigmf}

    def __init__(self, MFList):
        self.MFList = MFList

    def evaluateMF(self, rowInput):
        if len(rowInput) != len(self.MFList):
            print("Number of variables does not match number of rule sets")
        return [[self.funcDict[self.MFList[i][k][0]](rowInput[i], **self.MFList[i][k][1]) 
                 for k in range(len(self.MFList[i]))] for i in range(len(rowInput))]

class GaussMF:
    def __init__(self, mean: float, std: float):
        self.mean = float(mean)
        self.std = float(std)

    def __call__(self, x):
        return np.exp(-((x - self.mean) ** 2) / (2 * (self.std ** 2)))

def make_gauss_mfs(num_inputs=None, num_mfs=None, centers=None, sigmas=None, mu=None, sigma=None):
    """
    Flexible Gaussian MF constructor.
    Supports both:
      - new style (centers, sigmas as lists of lists)
      - old style (mu, sigma single values)
    """
    if mu is not None and sigma is not None:
        return GaussMF(mean=mu, std=sigma)

    mfs = []
    for i in range(num_inputs):
        mfs_for_input = []
        for j in range(num_mfs):
            mf = GaussMF(mean=centers[i][j], std=sigmas[i][j])
            mfs_for_input.append(mf)
        mfs.append(mfs_for_input)
    return mfs
