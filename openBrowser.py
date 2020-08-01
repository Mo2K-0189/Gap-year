import pyautogui
import time
import webbrowser

pyautogui.moveTo(700,1060)
pyautogui.doubleClick()
url='htttps://www.google.com'
webbrowser.open(url)

pyautogui.moveTo(755,526)
pyautogui.click()

time.sleep(3)
pyautogui.write('thailand')
pyautogui.press('enter')
#######
def SearchTH(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')
        
    pyautogui.press('backspace')
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word+'.png')

Search ('singapore')
Search ('USA')
Search ('china')








