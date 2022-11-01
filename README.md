# LeetGains
Python Tkinter GUI for a Weight Training Exercise App

A. How to REQUEST Data from the microservice
  1. Daysrv.py - Utilize Daysrv.py as a listener by running the program.
  2. app.py - Run program which will write "run" to day-service.txt file.
  3. Daysrv.py - Listener will see "run" on day-service.txt file and fetch the current date time and write it to txt file.
  4. day-service.txt - Now contains current date and time.
  5. app.py - Writes current date and time from txt file into Python Tkinter GUI.
  
  #  Example from app.py
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
    
    #  Example from Daysrv.py
    if __name__ == '__main__':
    while True:
        time.sleep(5.0)

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

B. How to Receive Data from the microservice
  1. app.py - Utilize date and time from day-service.txt by writing from file directly into pack of Tkinter application.
  2. app.py - Data can then be modified as needed to fit design specifications.

  #  Example from app.py
  with open("day-service.txt", "r") as f:
    Label(ws, text=f.read()).pack()
    
C. UML Sequence Diagram
![Screenshot 2022-10-31 192938](https://user-images.githubusercontent.com/77022804/199146991-ba2da5d4-6e08-4308-b6bc-7d72ebe3f309.jpg)
