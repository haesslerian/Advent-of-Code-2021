from typing import Match
import Utils
file = Utils.InjestData("./Day 2/directions.txt")
def format_instr(i):
    values = i.split(" ")
    if len(values) != 2:
        raise AttributeError("Wrong number of values for path instruction!")
    return (values[0], int(values[1]))
course_plan = [format_instr(i) for i in file.readlines()]
#(Horizontal Position, Depth, Aim)
current_location = [0,0,0]
def Navigate1(course):
    print(course)
    match course[0]:
        case 'forward':
            current_location[0] += course[1]
            return
        case 'down':
            current_location[1] += course[1]
            return
        case 'up':
            current_location[1] -= course[1]
            return
        case _:
            raise ValueError("Unknown Instruction!")
def Navigate2(course):
    print(course)
    match course[0]:
        case 'forward':
            current_location[0] += course[1]
            current_location[1] += current_location[2] * course[1]
            return
        case 'down':
            current_location[2] += course[1]
            return
        case 'up':
            current_location[2] -= course[1]
            return
        case _:
            raise ValueError("Unknown Instruction!")
for instr in course_plan:
    Navigate2(instr)
print(current_location)
print(current_location[0] * current_location[1])