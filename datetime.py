import datetime as day
import time

if __name__ == '__main__':
    while True:
        f = open("day-service.txt", "r")
        line = f.readline()
        f.close()

        # if file is empty
        if not line:
            continue

        # if date is needed
        if line == "run\n":
            print("Fetching day...")
            cur = day.datetime.now()
            f = open("day-service.txt", "w")
            f.write(f"{cur}")
            f.close()
            print("Date updated")