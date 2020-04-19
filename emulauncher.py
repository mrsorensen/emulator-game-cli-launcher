import os
from os.path import expanduser
import sys
from glob import glob
import time

# USER CONFIG
# -----------

# Path to the folder with your games
PATH = '~/PSX'
# Which emulator to use (Supports Mednafen and experimental EPSXE)
EMULATOR = 'Mednafen'


# END OF CONFIG
# -------------

RESTORE='\033[0m'
RED='\033[00;31m'
GREEN='\033[00;32m'
YELLOW='\033[00;33m'
BLUE='\033[00;34m'
PURPLE='\033[00;35m'
CYAN='\033[00;36m'
LIGHTGRAY='\033[00;37m'

# Get list of .cue files from PATH
result = [y for x in os.walk(expanduser(PATH)) for y in glob(os.path.join(x[0], '*.cue'))]

# Exit script if no .cue files found
if len(result) == 0:
    print(RED + 'No games found in ' + YELLOW + expanduser(PATH) + RESTORE)
    print(GREEN + 'Try to change the path to your game folder in pspy.py' + RESTORE)
    sys.exit(0)

# Prepare list of games
games = []

# Fill list of games
for r in result:
    game = []
    game.append([])
    game.append([])
    game.append([])
    # Append number for game
    game[0].append(result.index(r)+1)
    # Append path to game
    game[1].append(r)
    # Append name of game
    game[2].append(os.path.splitext(os.path.basename(r))[0])
    # Append game to games list
    games.append(game)


while True:
    try:
        # Print list of game names with numbers
        os.system('clear')
        for g in games:
            print(GREEN, g[0][0],') ', YELLOW, g[2][0], sep='')

        # Count number of games
        gamesAmount = len(games)

        # Let user pick which numbered game to play
        print(CYAN + '--------------------------------------' + RESTORE)
        dla = input(RED + 'Which game do you want to play? (1-' + str(gamesAmount) + '): ' + RESTORE)

        # Check if user input is int
        try:
            v = int(dla)
        # Error if user input is not int
        except:
            os.system('clear')
            print(RED + 'Only numbers accepted!' + RESTORE)
            print(CYAN + '----------------------' + RESTORE)
            time.sleep(1)
        # Continue if int
        else:
            # Make sure user picks a int that is within the range of the games list
            if int(dla) >= 1 and int(dla) <= gamesAmount:
                # Launch game
                print('Launching', games[int(dla)-1][2][0], '...')
                play = games[int(dla)-1][1][0].replace(' ', '\\ ').replace('(', '\(').replace(')', '\)').replace('\'', '\\\'')
                if EMULATOR.lower() == 'mednafen':
                    os.system('mednafen ' + play)
                elif EMULATOR.lower() == 'epsxe':
                    os.system('epsxe -loadiso ' + play + ' -nogui')
                else:
                    print(EMULATOR.lower() + ' not available yet')
            # Error if user picks int out of range
            else:
                os.system('clear')
                print(RED + 'Input out of range' + RESTORE)
                print(CYAN + '------------------' + RESTORE)
                time.sleep(1)
    # Exit script on ctrl+c with message
    except KeyboardInterrupt:
        print()
        print(PURPLE + 'Exiting...' + RESTORE)
        sys.exit(0)
