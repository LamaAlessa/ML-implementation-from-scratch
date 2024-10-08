import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class LinearRgression():
    def __init__(self,learning_rate, iterations):
        self.learning_rate = learning_rate 
        self.iterations = iterations

    
    def fit(self, X,y):
        self.m , self.n = X.shape
        self.W = np.zeros(self.n)
        self.b = 0 
        self.X = X
        self.y = y

        for i in range(self.iterations):
            self.update_weights()
        return self
    

    def update_weights(self):
        Y_pred = self.predict(self.X)

        # calculate gradients
        dw = -(2*(self.X.T).dot(self.y  - Y_pred))/self.m
        db = - 2 * np.sum(self.y - Y_pred)/self.m
        #update the wights
        self.W = self.W - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
        return self
    
    def predict(self, X):
        return X.dot(self.W) + self.b
    
            