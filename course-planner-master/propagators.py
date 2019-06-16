#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.
from orderings import *

'''This file will contain different constraint propagators to be used within 
   bt_search.

   propagator == a function with the following template
      propagator(csp, newVar=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

      newVar (newly instaniated variable) is an optional argument.
      if newVar is not None:
          then newVar is the most
           recently assigned variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of variable values pairs are all of the values
      the propagator pruned (using the variable's prune_value method). 
      bt_search NEEDS to know this in order to correctly restore these 
      values when it undoes a variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been 
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newVar = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated 
        constraints) 
        we do nothing...return true, []

        for forward checking (where we only check constraints with one
        remaining variable)
        we look for unary constraints of the csp (constraints whose scope 
        contains only one variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newVar = a variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned variable left

         for gac we initialize the GAC queue with all constraints containing V.
   '''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no 
    propagation at all. Just check fully instantiated constraints'''
    
    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with 
       only one uninstantiated variable. Remember to keep 
       track of all pruned variable,value pairs and return '''
    #IMPLEMENT
    pruned_vals = []
    if newVar is not None:
        iter_list = csp.get_cons_with_var(newVar)
    else:
        iter_list = csp.get_all_cons()
    for c in iter_list:
	    if c.get_n_unasgn() == 1:
	    	v = c.get_unasgn_vars()[0]
	    	for d in v.cur_domain():
	    		if not c.has_support(v, d):
	    			v.prune_value(d)
	    			pruned_vals.append((v, d))
	    	if v.cur_domain_size() == 0:
	    		return False, pruned_vals
    return True, pruned_vals

def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce 
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''
    #IMPLEMENT
    pruned_vals = []
    if newVar is None:
    	GACQueue = csp.get_all_cons()
    else:
    	GACQueue = csp.get_cons_with_var(newVar)
    
    while GACQueue != []:
    	c = GACQueue.pop(0)
    	for v in c.get_scope():
    		for d in v.cur_domain():
    			if not c.has_support(v, d):
    			    v.prune_value(d)
    			    pruned_vals.append((v, d))
    			    if v.cur_domain_size() == 0:
    			    	return False, pruned_vals
    			    else:
    			    	other_cons = csp.get_cons_with_var(v)
    			    	other_cons.remove(c)
    			    	for con in other_cons:
    			    		if con not in GACQueue:
    			    			GACQueue.append(con)
    return True, pruned_vals

#Slightly modified version of GAC prop that chooses next variable to expand based on heuristic function
#instead of looping for the next one
def prop_GAC_2(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''
    # IMPLEMENT
    pruned_vals = []
    if newVar is None:
        GACQueue = csp.get_all_cons()
    else:
        GACQueue = csp.get_cons_with_var(newVar)

    while GACQueue != []:
        c = GACQueue.pop(0)
        temp = c.get_scope()
        while len(temp) != 0:
            v = ord_weighted(temp)
            temp.remove(v)
            for d in v.cur_domain():
                if not c.has_support(v, d):
                    v.prune_value(d)
                    pruned_vals.append((v, d))
                    if v.cur_domain_size() == 0:
                        return False, pruned_vals
                    else:
                        other_cons = csp.get_cons_with_var(v)
                        other_cons.remove(c)
                        for con in other_cons:
                            if con not in GACQueue:
                                GACQueue.append(con)
    return True, pruned_vals
