import csv
import random
from datetime import datetime

WORKOUT_DAY_INDEX = 0
WORKOUT_MUSCLE_GROUP_INDEX = 1
WORKOUT_INDEX = 2

def main():
    print("Workout Generator")
    print("Today is:", get_day())
    # print(get_workouts_for_day(day))    

def get_day():
    today = datetime.today()
    return today.strftime("%A")

def get_workouts_for_day(day):
    with open("workouts.csv", "rt") as dentists_file:
        reader = csv.reader(dentists_file)
        next(reader)
        for row_list in reader:
            day = row_list[WORKOUT_DAY_INDEX]
            muscle_group = row_list[WORKOUT_MUSCLE_GROUP_INDEX]
            workout = row_list[WORKOUT_INDEX]
            print(f"Day: {day}, Muscle group: {muscle_group}, Workout: {workout}")

# def generate_workout(workout_list, count):

# def display_workout(day, selected_workouts):

# get_workouts_for_day(day) – returns list of workouts based on the day
# generate_workout(workout_list, count) – randomly selects a given number of workouts
# display_workout(day, selected_workouts) – prints the final workout in a clean format
# main() – the main driver of the program

if __name__ == "__main__":
    main()