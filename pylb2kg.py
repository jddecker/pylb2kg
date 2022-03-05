import keyboard
import pyautogui

def lb2kg():
    lb = pyautogui.prompt(title="pylb2kg", text="How many pounds would you like to convert to kg?")

    # check if can convert to float. if not then exit function
    try:
        lb = float(lb)
    except ValueError:
        pyautogui.alert("Input must be a number")
        return
    
    kg = round(lb / 2.20462262)
    keyboard.write(f"{kg}")
    return

print("pylb2kg")
print("Input pounds and get a rounded to the nearest whole number for kgs typed where your cursor was last located")
print("*** Hotkeys ***")
print("To open dialog for input press: ctrl + alt + p")
print("To quit this program press: ctrl + alt + q")
print("Running...")

# keyboard actions
keyboard.add_hotkey("ctrl+alt+p", lb2kg)
keyboard.wait("ctrl+alt+q")  # this will allow the script to run to the end of the file

print("Exiting...")
