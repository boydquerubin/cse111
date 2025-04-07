import csv
import random
from datetime import datetime

WORKOUT_DAY_INDEX = 0
WORKOUT_MUSCLE_GROUP_INDEX = 1
WORKOUT_INDEX = 2

def main():
    print("Workout Generator")
    day = get_day()
    today_workouts = get_workouts_for_day(day)
    randomized = generate_workout(today_workouts, 6)
    display_workout(day, randomized)

def get_day():
    today = datetime.today()
    return today.strftime("%A")

def get_workouts_for_day(day):
    with open("workouts.csv", "rt") as workouts_file:
        reader = csv.reader(workouts_file)
        next(reader)
        workouts_for_today = []

        for row_list in reader:
            workout_day = row_list[WORKOUT_DAY_INDEX]
            muscle_group = row_list[WORKOUT_MUSCLE_GROUP_INDEX]
            workout = row_list[WORKOUT_INDEX]

            if workout_day == day:
                workouts_for_today.append((muscle_group, workout))

        return workouts_for_today

def generate_workout(workout_list, count):
    if count > len(workout_list):
        count = len(workout_list)

    workouts_randomized = random.sample(workout_list, count)
    return workouts_randomized

def display_workout(day, selected_workouts):
    print("")
    print(f"Today is {day}.")
    print(f"Here is a list of {day}'s workouts:")
    print("")
    counter = 1
    for muscle_group, workout in selected_workouts:
        print(f"{counter}: {muscle_group}: {workout}")
        counter += 1

if __name__ == "__main__":
    main()