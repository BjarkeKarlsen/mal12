import numpy as np

def checkArraySizeCoantainsElements(X):
    assert X.shape[0]>=0 
    if not X.ndim==1:
        raise Exception("Array size needs to bigger than 1 dimision")

def checkArraySize(X):
    assert X.shape[0]>=0 and X.shape[1]==0
    if not X.ndim==1:
        raise Exception("Array size needs to bigger than 1 dimision")

def L1(X):
    checkArraySizeCoantainsElements(X)
    return sum((Xi**2)**0.5 for Xi in X) 


def L2(X):
    checkArraySizeCoantainsElements(X)
    sum = 0
    for i in range(X.size): 
        sum = sum + X[i] * X[i] 
    return sum**(1/2)

def L2Dot(X):
    return np.sqrt(np.dot(X,X))

# import os
# def GetOS():
#     return dir if os.name == 'nt' else ls

# # The Normal Equation p.134
# def GetOptiomalWeights(X, y):
#     X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Concatenate a column of ones to X
#     w = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
#     return w