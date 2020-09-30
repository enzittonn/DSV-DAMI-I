#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : luis-eduardo@dsv.su.se
# Created Date: 2020/06/23
# =============================================================================
"""
Introduction to Python - Lab 0
Custom functions
"""
# =============================================================================
# Imports
# =============================================================================
import math
import numpy as np
# =============================================================================
# Main
# =============================================================================

def compare_age(my_age, your_age):
    """ Displays if both ages are equal or
    different
    """
    if (my_age > your_age):
        # Executed when the condition is True
        print("I am older than you")
    elif (my_age == your_age):
        print("We are both the same age")
    else:
        print("I am not older than you")


def calculate_mean_2D_array(input_array, axis=None):
    """
    This function uses numpy methods to calculate the 
    mean of a 2D numpy array according to the specified axis.

    Input:
        input_array: 2D numpy array
        axis: Defines how to perform the calculation of the mean
            axis=None (default) - Average all the values in the array
            axis=0 - running vertically downwards across rows
            axis=1 - running horizontally across columns
    Output:
        A single value (if axis=None) or an array containing
        the mean of the elements along the specified axis
    """

    # Local Variables
    result = None   # This variable will contain the final result

    # Help variables for the function
    nrows, ncols = input_array.shape # Extracts the size of the array
    N = nrows * ncols

    # Average over all the elements
    if axis == None:
        # Help variable to store cumulative sum
        cumsum = 0
        # Access each row from the array
        for i in range(nrows):
            # Access each value from the row
            for j in range(ncols):
                # Add to the cumulative sum
                cumsum += input_array[i,j]
        # Calculate total average
        result = cumsum / N

    # Average vertically downwards across rows
    elif axis == 0:
        # The result is a list, in which we will append respective values 
        result = []
        # Access each row from the array
        for j in range(ncols):
            # Sum ALL the elements from the column
            #   and divide by number of elements
            average = input_array[:,j].sum() / nrows
            # Append the value to the result
            result.append(average)
        # Convert from list to numpy array
        result = np.array(result)

    # Average horizontally across columns
    elif axis == 1:
        # The result is a list, in which we will append respective values 
        result = []
        # Access each row from the array
        for i in range(nrows):
            # Sum ALL the elements from the row
            #   and divide by number of elements
            average = input_array[i,:].sum() / ncols
            # Append the value to the result
            result.append(average)
        # Convert from list to numpy array
        result = np.array(result) # Convert from list to numpy array
    
    # Return the variable to the object that called this function
    return result