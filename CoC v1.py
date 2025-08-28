from humancursor import SystemCursor
import pyautogui, random, time, keyboard

pyautogui.FAILSAFE = False
cursor = SystemCursor()
num = 0.0

def generateRandomNumberandSleep(min_val=0.0, max_val=2.0):
    global num
    num = round(random.uniform(min_val, max_val), 2)
    time.sleep(num)

def locateOnScreen(path):
    location = None
    while location is None:
        try:
            location = pyautogui.locateOnScreen(path, confidence=0.75)
        except pyautogui.ImageNotFoundException:
            # wait a short time and retry
            time.sleep(0.1)
            continue

    center = pyautogui.center(location)
    x, y = center.x, center.y
    return x, y

def doMovements(path):
    x, y = locateOnScreen(path) #locate x,y
    generateRandomNumberandSleep() #just to be same and avoid bot detection
    cursor.move_to([x+num+10, y-num-10]) #go to location in 'human-like' manner
    generateRandomNumberandSleep() #again safety net
    pyautogui.click() 

def clickAttack():
    doMovements(r"pics\attack.png")

def clickFindNow():
    doMovements(r"pics\findnow.png")

def checkIfBattleIsReady():
    _ = locateOnScreen(r"pics\swapicon.png")

def positionSelfToDeploy():
    start_position = pyautogui.position()
    generateRandomNumberandSleep()
    cursor.move_to([1925, 1157])
    generateRandomNumberandSleep()
    cursor.drag_and_drop(start_position, [0, 0])
    generateRandomNumberandSleep()

def deployTroops():
    generateRandomNumberandSleep()
    cursor.move_to([761 - num, 1056 + num + 16])

    keyboard.press_and_release('q')
    generateRandomNumberandSleep()
    pyautogui.click()
    generateRandomNumberandSleep()

    keyboard.press_and_release('1')
    generateRandomNumberandSleep()
    pyautogui.mouseDown(button='left')
    keyboard.press_and_release('2')
    generateRandomNumberandSleep()
    pyautogui.mouseDown(button='left')
    keyboard.press_and_release('3')
    generateRandomNumberandSleep()
    pyautogui.mouseDown(button='left')
    keyboard.press_and_release('4')
    generateRandomNumberandSleep()
    pyautogui.mouseDown(button='left')
    keyboard.press_and_release('5')
    generateRandomNumberandSleep()
    pyautogui.mouseDown(button='left')

    time.sleep(2.5)
    pyautogui.mouseUp(button='left')
    time.sleep(1.5)

    keyboard.press_and_release('1')
    generateRandomNumberandSleep()
    keyboard.press_and_release('2')
    generateRandomNumberandSleep()
    keyboard.press_and_release('3')
    generateRandomNumberandSleep()
    keyboard.press_and_release('4')
    generateRandomNumberandSleep()
    keyboard.press_and_release('5')
    generateRandomNumberandSleep()
    keyboard.press_and_release('6')
    generateRandomNumberandSleep()

def detectIfLostOrNextArea():
    location = None
    secondPhase = False

    while True: #infinite loop until we eventually see 'Return Home', then return
        if not secondPhase:
            try:
                location = pyautogui.locateOnScreen(r"pics/swapicon.png", confidence=0.75)
            except pyautogui.ImageNotFoundException:
                # wait a short time and retry
                time.sleep(0.1)

            if location is not None: #means we are in the next battle
                positionSelfToDeploy()
                deployTroops()
                secondPhase = True
                location = None
        
        try:
            location = pyautogui.locateOnScreen(r"pics/returnhome.png", confidence=0.75)
        except pyautogui.ImageNotFoundException:
            # wait a short time and retry
            time.sleep(0.1)

        if location is not None: #means we lost
            doMovements(r"pics/returnhome.png")
            return

def main():
    while True:
        clickAttack()
        clickFindNow()
        checkIfBattleIsReady()
        positionSelfToDeploy()
        deployTroops()
        detectIfLostOrNextArea()
        generateRandomNumberandSleep()

time.sleep(2)
main()