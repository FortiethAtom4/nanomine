import pyautogui, time, argparse

parser = argparse.ArgumentParser("nanomine")
parser.add_argument("pickaxe",choices=["wood","stone","iron","gold","diamond","netherite"],help="Pickaxe type")
parser.add_argument("-s","--slots",choices=[f"{i}" for i in range(1,10)],help="number of picks available")
args = parser.parse_args()
# keep track of picks
pick_durability: int = 0
mine_duration: float = 0
match args.pickaxe:
    case "wood":
        pick_durability = 59
        mine_duration = 1.75
    case "stone":
        pick_durability = 131
        mine_duration = 0.9
    case "iron":
        pick_durability = 250
        mine_duration = 0.6
    case "gold":
        pick_durability = 32
        mine_duration = 0.4
    case "diamond":
        pick_durability = 1561
        mine_duration = 0.5
    case "netherite":
        pick_durability = 2031
        mine_duration = 0.5

# slot 
slots: int = int(args.slots) if args.slots != None else 1

print("Script started, waiting 5 seconds to allow for prep...")
time.sleep(5)
# conditions: player looking at cobblestone in generator, pickaxe in slots 1-9 (unless otherwise specified)
for i in range (slots):
    print(f"Mining with slot {i}")
    for i in range(pick_durability):
        pyautogui.mouseDown(button="left")
        time.sleep(mine_duration)
        pyautogui.mouseUp()
        time.sleep(2)
    # switch slots
    print("Pickaxe used up, switching slots...")
    pyautogui.scroll(-1)

print("Script complete")