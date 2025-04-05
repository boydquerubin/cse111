import csv
import random
from datetime import datetime, timedelta

current_date_and_time = datetime.today()

WORKOUT_DAY_INDEX = 0
WORKOUT_MUSCLE_GROUP_INDEX = 1
WORKOUT_INDEX = 2

def main():
    print("Workout Generator")
    # print(f"{current_date_and_time:%c}")
    with open("workouts.csv", "rt") as dentists_file:
        reader = csv.reader(dentists_file)
        next(reader)
        for row_list in reader:
            print(row_list)

# def get_day():

if __name__ == "__main__":
    main()