import time

# Date Display Micro Service - Self
while True:
    f = open("day-service.txt", "w")
    f.write("run\n")
    f.close()
    time.sleep(10.0)
    while True:
        time.sleep(5.0)
        # check if file has been changed
        f = open("day-service.txt", "r")
        line = f.readline()
        f.close()
        break
    break
