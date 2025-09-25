# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:41:58 2014

@author: tim.meggs
"""

from skfuzzy import gaussmf, gbellmf, sigmf

class MemFuncs:
    'Common base class for all employees'
    funcDict = {'gaussmf': gaussmf, 'gbellmf': gbellmf, 'sigmf': sigmf}


    def __init__(self, MFList):
        self.MFList = MFList

    def evaluateMF(self, rowInput):
        if len(rowInput) != len(self.MFList):
            print("Number of variables does not match number of rule sets")

        return [[self.funcDict[self.MFList[i][k][0]](rowInput[i],**self.MFList[i][k][1]) for k in range(len(self.MFList[i]))] for i in range(len(rowInput))]
    

    import torch

class GaussMF(torch.nn.Module):
    def __init__(self, mean: float, std: float):
        super().__init__()
        self.mean = torch.nn.Parameter(torch.tensor(float(mean)))
        self.std = torch.nn.Parameter(torch.tensor(float(std)))

    def forward(self, x):
        return torch.exp(-((x - self.mean) ** 2) / (2 * (self.std ** 2)))


def make_gauss_mfs(num_inputs=None, num_mfs=None, centers=None, sigmas=None, mu=None, sigma=None):
    """
    Flexible Gaussian MF constructor.
    Supports both:
      - new style (centers, sigmas as lists of lists)
      - old style (mu, sigma single values)
    """
    if mu is not None and sigma is not None:
        # old-style single Gaussian MF
        return GaussMF(mean=mu, std=sigma)

    # new-style: full MF grid
    mfs = []
    for i in range(num_inputs):
        mfs_for_input = []
        for j in range(num_mfs):
            mf = GaussMF(mean=centers[i][j], std=sigmas[i][j])
            mfs_for_input.append(mf)
        mfs.append(mfs_for_input)
    return mfs

