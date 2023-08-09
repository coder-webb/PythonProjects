"""
---Prompt---
Given integer inputs seed, how_many, and max_num, generate a list of how_many unique random integers from 0 to max_num (inclusive).

Complete function unique_random_ints(how_many, max_num):
Generate a list of how_many random integers from 0 to max_num (inclusive).
When a random number exists in the list, a new random number must be generated; use a global variable, retries, to count the number of times an existing number is generated.
Return the list.
Complete __main__:
Initialize the random module with the seed value.
Call unique_random_ints() to get a list of random integers.
Output the list of random integers and the value of retries, according to the output format shown in the example below.
"""
import random

def unique_random_ints(how_many, max_num):
    '''Returns a list of unique random numbers and the amount of times a number had to be recalculated in order to be random'''
    i = 0
    rand_ints = []
    retries = 0
    while i != how_many:
        test_num = random.randint(0, max_num)
        if test_num in rand_ints: # If the randomly generated number already exists in the list, don't add it to the list
            retries += 1
        else: # If the random number does not exist in the list, append it
            rand_ints.append(test_num)
            i += 1
    return rand_ints, retries # Return the list of random integers and the amount of retries needed


if __name__ == '__main__':
    random.seed(int(input('Enter a seed value:\n'))) # Set the seed
    how_many = int(input('Enter how many unique numbers should show:\n'))
    max_num = int(input('Enter the highest number you want to show:\n'))
    
    results = unique_random_ints(how_many, max_num)
    rand_list = results[0]
    retries = results[1]
    
    print(' '.join(map(str, rand_list)), f'retries = {retries}')