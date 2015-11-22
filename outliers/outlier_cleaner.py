#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    old_len = len(predictions)
    del_len = int(round(old_len * 0.1))

    error = (predictions - net_worths)**2
    cleaned_data = zip(ages, net_worths, error)

    cleaned_data = sorted(cleaned_data, key=lambda x:x[2][0], reverse=True)

    
    return cleaned_data[del_len:]

