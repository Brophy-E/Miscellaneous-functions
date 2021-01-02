#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:51:56 2019

@author: Brophy-E

If you have the results of the true vs. predicted scores saved to an array you can use this code to
create a confusion matrix and save the figure to your files.

You may have the true (y_test) vs predicted (y_pred) and should use sklearns confusion matrix:
    >>> from sklearn.metrics import confusion_matrix
    >>> confusion_matrix(y_true, y_pred)
    
My code is only to help if you have your scores in an array or forma that doesnt work with the above sklearn function
"""
import matplotlib.pyplot as plt
import numpy as np

# An example array of scores - hard coded anything is NOT recommended!!
array = [[97.41,0,0,2.59,0,0],[0,94.87,0,5.13,0,0],[0,0,100,0,0,0],[0,3.03,0,96.97,0,0],[1.27,0,0,0,98.73,0],[0,0,0,0,0,100]] 

#stores array as numpy matrix
matrix = np.matrix(array) 

plt.figure()
plt.imshow(matrix, interpolation='none', cmap='Blues')

plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# You should rename '1' - '6' your class names
plt.xticks([0,1,2,3,4,5],['1','2','3','4','5','6'])
plt.yticks([0,1,2,3,4,5],['1','2','3','4','5','6'])

plt.axis('on')
plt.title('Confusion Matrix Results')


cbar = plt.colorbar(fraction= 0.046, pad=0.04)
cbar.set_label('', rotation=270, labelpad=30, fontsize=12)
for i in range(len(array[0])):
   for j in range(len(array[0])):
     if i==j:
       text = plt.text(j, i, matrix[i, j],
                      ha="center", va="center", color="1")
     else:
       text = plt.text(j, i, matrix[i, j],
                      ha="center", va="center", color="0")

# Save in whatever format works for you. PDF is my usual go-to but formats the 
# image a bit differently, I would recommend svg just for this one.
       
#plt.savefig('./confusion_matrix.pdf', format='pdf')
plt.show()