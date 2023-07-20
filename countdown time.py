import time
def countdown(t):
    while t>0:
        print(t)
        t=t-1
        time.sleep(1)
    print("Time's up")
print("How many seconds to count down? Enter an Integer=")
seconds=input()
while not seconds.isdigit():
    print("That  integer number! please enter an integer")
    seconds=input()
seconds=int(seconds)
countdown(seconds)