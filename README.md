# nanomine

## IN-GAME PREP

Set up a simple cobblestone generator. Under the spot where the cobblestone block forms, place a hopper facing a chest. The hopper will collect the blocks you mine.
Be sure that the area you will be AFK mining in is free of hostile mobs. 
[Simple cobblestone generator](https://minecraft.wiki/w/Tutorial:Cobblestone_farming). You do NOT need to make anything crazy complicated like the designs further down the page; it just needs to produce a block of cobblestone for you to mine with a hopper to collect it.

## CODE PREP

You will need Python 3 in order to run this script. [Get Python here](https://www.python.org/downloads/)
- NOTE: Be sure to check the box which says "add to PATH".

These instructions will use Git to clone the repository to your computer. [Get Git here](https://git-scm.com/downloads)

1. Click the green Code button on this page and copy the given link. 
2. Open Command Prompt.
3. Using Command Prompt, navigate to a folder on your computer where you want to put the code. This can be done using `cd [folder name]`. 
    - You can see a list of folders you can cd into using `dir`. 
    - If you want to move "back" in the folder list, use `cd ..`.
    - You can also make a new directory on the fly using `mkdir [directory name]`.
4. Once you're in the desired folder, type `git clone [link]`, where `[link]` is the link you copied from this page. 
    - If you've done this correctly, if you type `dir` you should see a new folder called "nanomine."
5. `cd` into the new folder.
6. Type the following commands:
    ```
    python -m venv venv
    cd venv/Scripts
    activate
    cd ../..
    pip install -r requirements.txt
    ```
    
    These commands will create a local environment and install the script's dependencies. The installation should be quick and will not affect the rest of your computer. If you ever want to uninstall these dependencies, simply delete the folder called `venv`.

The code is now ready to run.

NOTE: If you close this Command Prompt window and want to use the script again later, you will need to `cd` back to this folder and type lines 2-4 of the above commands again in order to reactivate the environment.

## USAGE

Place the pickaxes you want to AFK mine with in your hotbar. The script can use up to a maximum of 9 pickaxes, one for each slot in the hotbar. Then run the code by typing:

`python nanomine.py [-s {1,2,3,4,5,6,7,8,9}] {wood,stone,iron,gold,diamond,netherite}`

The script will give you 5 seconds to switch tabs back to the game before starting.

Some examples to explain how to use the script:

- 1 stone pickaxe: `python nanomine.py stone`
- 3 iron pickaxes in your hotbar: `python nanomine.py iron -s 3`
- 9 netherite pickaxes in the hotbar: `python nanomine.py netherite -s 9` (note: why would you do this)

You can type `python nanomine.py -h` to see the script's options listed out for you if you forget.

NOTE: the script does NOT take into account pickaxes with enchantments (e.g. Efficiency, Unbreaking), nor does it take into account pickaxes of multiple types (e.g. you have 3 iron and 4 stone pickaxes). For the sake of using this script, I recommend using unused and unenchanted stone or iron pickaxes, or any level of pick that you are willing to expend solely on mining cobblestone. 


