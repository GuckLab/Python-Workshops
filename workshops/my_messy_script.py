


import os, sys, random
import numpy
def make_list():
	lst1 = [8, 9, 5]
	lst2 = [7, 2, 3]
	return lst2



def multiply_list():
  rand_num = random.randint()
  lst = make_list()
  lst_multiply = [i*rand_num for i in lst]
  return lst_multiply
print(lst_multiply)