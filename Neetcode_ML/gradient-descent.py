# https://neetcode.io/problems/gradient-descent

# Your task is to minimize the function via Gradient Descent: f(x)=x^2
#
# Gradient Descent is an optimization technique widely used in machine learning for training models.
# It is crucial for minimizing the cost or loss function and finding the optimal parameters of a model.
#
# For the above function the minimizer is clearly x = 0, but you must implement an iterative approximation algorithm, through gradient descent.

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init
        res = init
        for i in range(iterations):
            res = res - learning_rate * 2 * res
        return round(res, 5)