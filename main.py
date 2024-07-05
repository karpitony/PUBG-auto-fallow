import pyautogui
import keyboard
import time
time.sleep(2)

def check_and_click():
    print('f5')
    while True:
        try:
        time.sleep(0.1)

        # start.png 이미지 찾기
        pyautogui.locateOnScreen('start.PNG', confidence=0.5)
        print('stawwwwrt location')

        time.sleep(0.1)
        # 'm' 키 누르기
        pyautogui.keyDown('m')
        time.sleep(0.1)
        pyautogui.keyUp('m')
        print('m')
        # fallow.png 이미지 찾아서 클릭
        fallow_location = pyautogui.locateOnScreen('fallow.PNG', confidence=0.5)

        pyautogui.click(fallow_location)

        break


        # 0.1초 대기
        time.sleep(0.1)


# F5 키 누를 때 함수 실행
keyboard.add_hotkey('f5', check_and_click)

# 프로그램 실행 상태 유지
keyboard.wait()