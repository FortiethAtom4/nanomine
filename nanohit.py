import pyautogui, time, argparse, datetime, threading

parser = argparse.ArgumentParser("nanohit")
parser.add_argument("-d","--delay", default="30", help="Number of seconds for each hit cycle. Defaults to 30 seconds.")
parser.add_argument("-n","--num_hits", default="1",help="Number of times the player hits in each hit cycle. Defaults to 1.")
parser.add_argument("-i","--interval", default="1", help="Value in seconds to delay between individual hits. Defaults to 1 second.")
parser.add_argument("-t","--timer", default="0", help="Value in minutes. Script will stop once this time is exceeded. Defaults to 0 (no time limit).")

# globals
args = parser.parse_args()
hits: int = 0 # keeps track of total clicks
hit_ready: bool = True # flag to track when interval is up (i.e. time to hit)
time_up: bool = False # flag to check if time is up

try:
    float(args.timer)
except ValueError:
    print("Error: non-numeric value for timer")
    exit(1)

timer = float(args.timer)

# Threaded task to increment the timer and raise hit_ready and time_up flags
def track_time(delay):
    # Access globals
    global hits, hit_ready, timer, time_up

    print(f"Starting nanohit.py with hit delay {delay}s...")
    if timer > 0:
        print(f"Timer set to {timer} minutes.")

    start_time: datetime.datetime = datetime.datetime.now()
    
    num_intervals: int = 0
    while True:
        cur_time: datetime.datetime = datetime.datetime.now()
        time_elapsed = (cur_time-start_time).total_seconds()

        if timer > 0 and time_elapsed > timer * 60: # Time is up
            time_up = True
            return
        
        if (time_elapsed / delay) > num_intervals: # Sets hit_ready flag to True, allowing hits to occur
            num_intervals += 1
            hit_ready = True

        print(f"Total Hits: {hits} || Time Elapsed: {datetime.timedelta(seconds=time_elapsed)}",end="\r")
        time.sleep(0.1)



def nanohit():
    try:
        float(args.delay)
        float(args.interval)
    except ValueError:
        print("Error: non-numerical argument provided for a timer.")
        return
    
    try:
        int(args.num_hits)
    except ValueError:
        print("Error: non-integer value provided for number of hits.")
        return
        
    time_tracker_thread = threading.Thread(args=(float(args.delay),),target=track_time,daemon=True)

    
    print("Hits will begin in 5 seconds to allow for prep. Press Ctrl+C at any time to quit.")
    time.sleep(5)
    time_tracker_thread.start()
    global hits, hit_ready
    num_hits = int(args.num_hits)
    hit_interval = float(args.interval)

    # main loop
    while not time_up:
        if hit_ready:
            for i in range(num_hits):
                pyautogui.click(button="left")
                hits += 1
                time.sleep(hit_interval)
            hit_ready = False

nanohit()
print("\nTime is up, stopping program")