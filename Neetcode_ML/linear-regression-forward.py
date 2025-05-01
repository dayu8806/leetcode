# https://neetcode.io/problems/linear-regression-forward

# Your task is to implement linear regression, a statistical model that ends up being the foundation of neural networks.
# You can learn more from the Complete Explanation of Linear Regression or by reading the description below.
#
# Your must implement get_model_prediction() which returns a prediction value for each dataset value, and get_error() which calculates the error for given prediction data.

import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        prediction = np.matmul(X, weights)
        return np.round(prediction, 5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        res = 0
        for i in range(3):
            res += (model_prediction[i][0] - ground_truth[i][0]) ** 2
        return round(res / 3, 5)
