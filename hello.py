from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

rocket_frames = [
r"""
               /\
              /  \
             /____\
             |    |
             |NASA|
             |    |
            /| || |\
           /_|_||_|_\
              /||\
             /_||_\
            /_/  \_\
""",
r"""
               /\
              /  \
             /____\
             |    |
             |NASA|
             |    |
            /| || |\
           /_|_||_|_\
              /||\
             /_||_\
            /_/  \_\
             **  **
""",
r"""
               /\
              /  \
             /____\
             |    |
             |NASA|
             |    |
            /| || |\
           /_|_||_|_\
              /||\
             /_||_\
            /_/  \_\
            ****** 
""",
]

print("\n🚀 Launching Rocket...\n")

for i in range(6):
    clear()
    print("\n" * (5 - i))  # ทำให้จรวดลอยขึ้น
    print(rocket_frames[i % len(rocket_frames)])
    sleep(0.3)

print("\n✨ Mission Complete! ✨")