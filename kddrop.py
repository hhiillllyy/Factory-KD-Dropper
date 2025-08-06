import pyautogui
import time
import random
import os
import threading

# Configuration
image_folder = "images"
num_steps = 6
delay_between_checks = 1
confidence = 0.7

# Jump control
jumping = False
jump_thread = None

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

def human_move_and_click(x, y):
    current_x, current_y = pyautogui.position()
    distance = ((x - current_x) ** 2 + (y - current_y) ** 2) ** 0.5
    duration = random.uniform(0.4, 0.8) + distance / 400
    pyautogui.moveTo(x, y, duration=duration)
    time.sleep(random.uniform(0.2, 0.4))
    pyautogui.click()
    time.sleep(random.uniform(0.3, 0.6))

def jump_randomly():
    while jumping:
        interval = random.uniform(1.5, 3.5)  # Slower spacebar jumping
        time.sleep(interval)
        pyautogui.press("space")
        # No logging of each press

def start_jumping():
    global jumping, jump_thread
    if not jumping:
        jumping = True
        jump_thread = threading.Thread(target=jump_randomly)
        jump_thread.start()
        log("Started jumping...")

def stop_jumping():
    global jumping, jump_thread
    if jumping:
        jumping = False
        if jump_thread:
            jump_thread.join()
        log("Stopped jumping.")

def wait_for_image_and_click(image_path, step):
    log("Waiting for next image...")
    while True:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if location:
                log(f"Found {os.path.basename(image_path)}")
                human_move_and_click(location.x, location.y)
                log("Clicked.")
                
                if step == 4:
                    start_jumping()
                elif step == 5:
                    stop_jumping()
                    
                break
        except:
            pass
        time.sleep(delay_between_checks)

def main():
    repeat = input("How many raids would you like to run? ")
    try:
        repeat = int(repeat)
    except ValueError:
        log("Invalid input, defaulting to 1 repetition.")
        repeat = 1

    for i in range(repeat):
        log(f"--- Starting sequence {i+1} ---")
        for step in range(1, num_steps + 1):
            image_path = os.path.join(image_folder, f"step{step}.png")
            if not os.path.exists(image_path):
                log(f"{os.path.basename(image_path)} not found, skipping.")
                continue

            wait_for_image_and_click(image_path, step)

    stop_jumping()
    log("✅ All sequences complete.")

if __name__ == "__main__":
    main()
