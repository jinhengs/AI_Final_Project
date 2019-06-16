from course_database import *
from course_planner_csp import *
from propagators import *
from orderings import *
from filter import *

COURSES = []
SUMMER = False
YEARS = 0
UNAVBL = []
PREF_TIME = []
PROF_PREF = 1
curr_dat = dat
SOL = []

if __name__ == "__main__":
	yrs = input("How many long do you plan on going to school(years):")
	YEARS = int(yrs)
	
	print("")
	
	smr = input("Do you plan on taking summer courses(y/n):")
	SUMMER = (smr == 'y')
	
	print("")
	
	print("Enter each course you plan on taking one at a time. Enter 'done' when finished:")
	inp = ""
	while(inp != 'done'):
		inp = input("")
		if (inp in dat.keys()):
			if inp in COURSES:
				print("You have already entered this course")
			elif set(dat[inp][3]).intersection(set(COURSES)) != set():
				print("You cannot take " + inp + " with any of these courses:")
				print(dat[inp][3])
			else:
				COURSES.append(inp)
		elif(inp != 'done'):
			print("Course not in database")
		elif inp == 'done':
			if len(COURSES) < 2:
				print("Too few courses. Please add more")
				inp = ""
	
	print("What times are you unavailable Enter 'done' when finished:")
	print("(FORMAT : M,T,W,J,F = Mon, Tues, Wed, Thur, Fri")
	print("		M,D,E,N = Morning, Day, Evening, Night")
	print(" Example: I am unavailble Monday Morning -> 'MM')")
	inp = ""
	while(inp != 'done'):
		inp = input("")
		if (inp[0] in ["M", "T", "W", "J", "F"] and inp[1] in ["M","D","E","N"]):
			UNAVBL.append(inp)
		elif(inp != 'done'):
			print("invalid input")
	print("What are your preferred timeslots? Enter 'done' when finished:")
	print("(FORMAT : M,T,W,J,F = Mon, Tues, Wed, Thur, Fri")
	print("		M,D,E,N = Morning, Day, Evening, Night")
	print(" Example: I prefer to take classes on Tuesday Evenings -> 'TE')")
	inp2 = ""
	while(inp2 != 'done'):
		inp2 = input("")
		if (inp2[0] in ["M", "T", "W", "J", "F"] and inp2[1] in ["M","D","E","N"]):
			PREF_TIME.append(inp2)
		elif(inp2 != 'done'):
			print("invalid input")
	PROF_PREF = input("Rate the importance of the quality of professors from 1-5\n1 being not important and 5 being very important: ")
	PROF_PREF = int(PROF_PREF)
	soln = dict()
	while soln != None:
		csp, var_array = course_planner_csp(COURSES, SUMMER, YEARS, UNAVBL, curr_dat)
		solver = BT(csp)
		soln = solver.bt_search(prop_GAC)
		if soln != None:
			print(soln)
			SOL.append(soln)
			for course in soln.keys():
				curr_dat[course][2].remove(soln[course])
	sol = get_best_solution(SOL, PREF_TIME, PROF_PREF)
	print("best solution\n")
	print(sol)

		
