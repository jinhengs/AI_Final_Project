  #Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.
from course_planner import *
from course_database import *
RATIO = 0.1
import random

'''
This file will contain the MRV variable ordering heuristic to be used within
bt_search.

var_ordering == a function with the following template
    ord_type(csp)
        ==> returns Variable 

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    ord_type returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
'''


def ord_mrv(csp):
    '''
    ord_mrv(csp):
    A var_ordering function that takes CSP object csp and returns Variable object var, 
    according to the Minimum Remaining Values (MRV) heuristic as covered in lecture.  
    MRV returns the variable with the most constrained current domain 
    (i.e., the variable with the fewest legal values).
    '''
    #IMPLEMENT
    md = -1
    mv = None
    for v in csp.get_all_unasgn_vars():
    	if md < 0:
    		md = v.cur_domain_size()
    		mv = v
    	elif v.cur_domain_size() < md:
    		md = v.cur_domain_size()
    		mv = v
    return mv

#First attempt at creating an efficient way of predicting how variables will be expanded
#Similar to the final version of heuristics, but this tries to predict the future
#Since the results are not known, the order of values for variables are taken into consideration
#for predicting the future.
#The final heuristic function does not take order into account since it knows all the results
def ord_weighted(listx):
	'''
	:param list of var:
	:return variable:
	 greedy heuristic that returns the variable with the lowest heuristic value.
	 idealy trading performance for optimal schedule based on preferences
	'''
	mv = None
	current = None
	for v in listx:
		#add timeslot h_val
		h_value = ((v.cur_domain_size()+1)*(v.cur_domain_size()))/2
		#add professor rating h_val
		h_value += h_val*RATIO*PROF_PREF*6
		temp = v.cur_domain();
		for i in range(len(temp)):
			for timeslot in PREF_TIME:
				if temp[i][0][1] == timeslot[0] and temp[i][0][2] == timeslot[1]:
					h_value = h_value - len(temp) + i
			h_value -= (1-(i/len(temp)))*prof_rat[temp[i][0][3]]*RATIO*PROF_PREF
		if current == None:
			mv = v
			current = h_value
		elif h_value < current:
			mv = v
			current = h_value
	return mv


