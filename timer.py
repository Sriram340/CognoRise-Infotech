import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\n')
        time.sleep(1)
        t=t-1

    print("Time's Up!")
t = int(input("Enter the numer of seconds: "))
countdown(t)
