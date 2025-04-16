import csv
import random
from datetime import datetime

WORKOUT_DAY_INDEX = 0
WORKOUT_MUSCLE_GROUP_INDEX = 1
WORKOUT_INDEX = 2

def main():
    try:
        print("Workout Generator")
        day = get_day()
        today_workouts = get_workouts_for_day(day)

        if day == "Thursday":
            biceps_list = []
            triceps_list = []

            for g, w in today_workouts:
                if g.lower() == 'biceps':
                    biceps_list.append(w)
                elif g.lower() == 'triceps':
                    triceps_list.append(w)

            selected_biceps = random.sample(biceps_list, min(3, len(biceps_list)))
            selected_triceps = random.sample(triceps_list, min(3, len(triceps_list)))

            print("")
            print(f"Today is {day}.")
            print("Here is your Biceps and Triceps workout:")
            print("")

            counter = 1
            for workout in selected_biceps:
                print(f"{counter}: Biceps: {workout}")
                counter += 1
            for workout in selected_triceps:
                print(f"{counter}: Triceps: {workout}")
                counter += 1

        else:
            randomized = generate_workout(today_workouts, 6)
            display_workout(day, randomized)

    except FileNotFoundError as not_found_err:
        print("File not found:", not_found_err)

    except PermissionError as perm_err:
        print("Permission error:", perm_err)

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

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
    return random.sample(workout_list, count)

def display_workout(day, selected_workouts):
    print("")
    print(f"Today is {day}.")
    print("Here is a list of today's workouts:")
    print("")
    counter = 1
    for muscle_group, workout in selected_workouts:
        print(f"{counter}: {muscle_group}: {workout}")
        counter += 1

def generate_biceps_and_triceps(biceps_list, triceps_list):
    selected_biceps = random.sample(biceps_list, min(3, len(biceps_list)))
    selected_triceps = random.sample(triceps_list, min(3, len(triceps_list)))
    return selected_biceps, selected_triceps

if __name__ == "__main__":
    main()
