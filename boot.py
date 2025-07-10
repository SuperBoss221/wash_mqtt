import os
import machine

def check_file_exists(filename):
    try:
        os.stat(filename)
        return True
    except :
        return False

file_to_check = 'wifi_manager.txt'
if check_file_exists(file_to_check):
    os.remove('wifi_manager.py')
    os.rename(file_to_check, 'wifi_manager.py')
    print(f"UPDATE WIFI")

file_to_check = 'wash.txt'
if check_file_exists(file_to_check):
    os.remove('wash.py')
    os.rename(file_to_check, 'wash.py')
    print(f"UPDATE WASH")

file_to_check = 'main.txt'
if check_file_exists(file_to_check):
    os.remove('main.py')
    os.rename(file_to_check, 'main.py')
    print(f"UPDATE MAIN")
