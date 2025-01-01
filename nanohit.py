import pyautogui, time, argparse

parser = argparse.ArgumentParser("nanohit")
parser.add_argument("-d","--delay",help="Number of seconds to delay between hits. Defaults to 30 seconds.")

args = parser.parse_args()

def nanohit():
    if args.delay != None:
        try:
            float(args.delay)
        except ValueError:
            print("Error: non-numerical argument provided.")
            return

    delay: float = float(args.delay) if args.delay != None else 30

    time.sleep(5)
    while True:
        pyautogui.click(button="left")
        time.sleep(1)
        pyautogui.click(button="left")
        time.sleep(delay)

nanohit()