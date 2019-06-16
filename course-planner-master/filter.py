import course_planner
import course_database

TIMESLOT_RATIO = 2
PROF_RATIO = 0.5


def get_best_solution(list_of_sol, pref_time, prof_pref):
    best_sol = None
    current = None
    for sol in list_of_sol:
        h_value = len(sol)*(TIMESLOT_RATIO + PROF_RATIO*prof_pref*6)
        for course in sol:
            for timeslot in pref_time:
                if sol[course][0][1] == timeslot[0] and sol[course][0][2] == timeslot[1]:
                    h_value -= TIMESLOT_RATIO
            h_value -= prof_pref*PROF_RATIO*course_planner.prof_rat[sol[course][0][3]]
        if current == None:
            best_sol = sol
            current = h_value
        elif h_value < current:
            best_sol = sol
            current = h_value
        print(h_value)
    return best_sol
