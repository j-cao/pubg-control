import pyautogui as gui
import time

# Functions 
# gui.press('w')
# gui.typewrite('test_text)
# gui.typewrite(["enter"])


################################################# 
# click start button
#################################################
gui.click(x=305, y=1342)
gui.click()

#################################################
# wait to load in-game lobby
#################################################
time.sleep(20)


#################################################
# infinite loop
#################################################
artbitrary_num = int(1000)
def run_and_punch(artbitrary_num):
    while artbitrary_num > 1: # CV condition here later
        
        # run + move forward
        gui.keyDown('shift')
        gui.keyDown('w')

        # crouch spam
        gui.press('c', presses=5)
        gui.click(clicks=5)
        gui.press('space', presses=5)


        time.sleep(0.25)


        break


run_and_punch(artbitrary_num)





# # infinite loop original
# artbitrary_num = int(1000)
# def run_and_punch(artbitrary_num):
#     while artbitrary_num > 1:
#         print("GUI POSITION: " + str(gui.position()))
#         break


# run_and_punch(artbitrary_num)


# while loop

# x = 1
# y = 3

# def run_and_punch_test(x, y):
#     while x < 6:
#         print(gui.position())
#         print("GUI POSITION " + str(x))
        
#         if x == y:
#             break
#         x+= 1

# run_and_punch_test(x, y)