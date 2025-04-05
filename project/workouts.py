import csv
import random
from datetime import datetime, timedelta

current_date_and_time = datetime.now()

def main():
    print("Workout Generator")
    print(f"{current_date_and_time:%c}")

if __name__ == "__main__":
    main()