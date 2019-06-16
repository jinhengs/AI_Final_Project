from cspbase import *
from course_database import *

course_vars = []

def course_planner_csp(courses, summer, years, times, in_dat):
	'''
	'''
	cdat = dict(in_dat)
	# Create variables for each course and add it to the CSP

	for course in courses:
		dom = cdat[course][2]
		course_vars.append(Variable(course, dom))
	
	course_planner_csp = CSP("course-planner", course_vars)
	
	# Add constraint for # of course per semester
	cons = Constraint("5 Courses per Semester", course_vars)
	cons.change_func(1)
	course_planner_csp.add_constraint(cons)
	
	# Add constraint for time conlflicts
	cons = Constraint("No time conflict", course_vars)
	cons.change_func(2)
	course_planner_csp.add_constraint(cons)
	
	# Add constraints for the total number of years
	for var in course_vars:
		cons = Constraint("Max Years in School", [var])
		dom = cdat[var.name][2]
		valid_vals = []
		for element in dom:
			if element[0][0] <= years * 3:
				valid_vals.append((element,))
		cons.add_satisfying_tuples(valid_vals)
		course_planner_csp.add_constraint(cons)
	
	# Add constraints if no summer courses allowed
	if not summer:
		for var in course_vars:
			cons = Constraint("No Summer", [var])
			dom = cdat[var.name][2]
			valid_vals = []
			for element in dom:
				if element[0][0] % 3 !=  0:
					valid_vals.append((element,))
			cons.add_satisfying_tuples(valid_vals)
			course_planner_csp.add_constraint(cons)
	
	# Add constraints for prereqs, co-reqs
	for course in courses:
		prereqs = cdat[course][0]
		coreqs = cdat[course][1]
		dom = cdat[course][2]
		c_var = find_var(course)
		if len(prereqs) > 0:
			for prereq in prereqs:
				if not prereq in courses:
					print("You need to take " + prereq + " in order to take " + course)
					exit()

				p_var = find_var(prereq)
				cons = Constraint("PreReq", [c_var, p_var])
				######
				valid_vals = []
				for element in dom:
					for section in cdat[prereq][2]:
						if element[0][0] > section[0][0]:
							valid_vals.append((element, section))
				cons.add_satisfying_tuples(valid_vals)			
				######
				course_planner_csp.add_constraint(cons)
		if len(coreqs) > 0:
			for coreq in coreqs:
				if not coreq in courses:
					print("You need to take " + coreq + " with " + course)
					exit()
				co_var = find_var(coreq)
				cons = Constraint("CoReq", [c_var, co_var])
				######
				valid_vals = []
				for element in dom:
					for section in cdat[coreq][2]:
						if element[0][0] == section[0][0]:
							valid_vals.append((element, section))
				cons.add_satisfying_tuples(valid_vals)			
				######
				course_planner_csp.add_constraint(cons)
	
	# Add time constraints
	for time in times:
		for var in course_vars:
			cons = Constraint("Custom", [var])
			dom = cdat[var.name][2]
			valid_vals = []
			for element in dom:
				if element[0][1] != time[0] or element[0][2] != time[1]:
					valid_vals.append((element,))
			cons.add_satisfying_tuples(valid_vals)
			course_planner_csp.add_constraint(cons)
	
	return course_planner_csp, course_vars

def find_var(course):
	for var in course_vars:
		if var.name == course:
			return var
	return -1
