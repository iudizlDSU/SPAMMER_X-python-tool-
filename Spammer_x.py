
import pyautogui as pg
import time
import os

def banner():
    os.system("title SPAMMER X / by ANONYMOUS ")
    os.system("cls")
    os.system("color 2")
    print("""
     ____  ____   _    __  __ __  __ _____ ____      __  __
    / ___||  _ \ / \  |  \/  |  \/  | ____|  _ \     \ \/ /
    \___ \| |_) / _ \ | |\/| | |\/| |  _| | |_) |     \  / 
     ___) |  __/ ___ \| |  | | |  | | |___|  _ <      /  \ 
    |____/|_| /_/   \_\_|  |_|_|  |_|_____|_| \_\    /_/\_\
                                                        
""")
    print("By ANONYMOUS.")
    print("Type '/help' to reveal commands.\n")
    

def prog_int():
    commands = ["/help", "spam", "/exit"]
    pg.FAILSAFE = True
    while True:
        u_i = input("->: ")
        if u_i not in commands:
            print(f"ERROR: invalid command: '{u_i}'")
            continue    
        if u_i == "/help":
            print(f"Commands: {commands}")
        elif u_i == "/exit":
            os.system("color 4")
            print("EXITING SPAMMER X...")
            time.sleep(1)
            break
        elif u_i == "spam":
            msg = input("Enter spam message: ")
            print(f"Spam message is: '{msg}'")
            c = input("Confirm?(y/n): ")
            if c == "y":
                print("Hover your mouse to top left corner to abort.")
                print("choose target to spam.")
                time.sleep(1)
                print("begining spam in 6")
                time.sleep(0.5)
                print("begining spam in 5")
                time.sleep(0.5)
                print("begining spam in 4")
                time.sleep(0.5)
                print("begining spam in 3")
                time.sleep(0.5)
                print("begining spam in 2")
                time.sleep(0.5)
                print("begining spam in 1")
                time.sleep(0.5)
                while True:
                        pg.write(msg)
                        pg.press('ENTER')
            else:
                os.system("color 4")
                print("CANCELING...")
                time.sleep(1)
                break
banner()
prog_int()
    
    
