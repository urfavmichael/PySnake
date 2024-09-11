import os
import sys
import subprocess

def main():
    game_file_path = "game_files/game.py"
    
    if os.path.exists(game_file_path):
        subprocess.run(["python3", game_file_path])
    else:
        print("The file \"game.py\" is missing, please refer to https://github.com/urfavmichael/Snake_Game to reinstall the program.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()