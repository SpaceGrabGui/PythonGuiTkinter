import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
from threading import Timer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import win32gui,win32con
import os
#import schedule
#StDoorOpen
def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        process_code(barcodeData)#get the URL from Camera and  press the shutter button
def process_code(barcodeData):
    print("cancel timer")
  #  myTimer.cancel()
    i = 0
    while i < 2:
        print("processing code for " + str(i) + " seconds")
        i += 1
        time.sleep(1)
    print(str(barcodeData) + " is processed")
    driver = webdriver.Chrome(r"C:\Users\IPCCTRL\Documents\chromedriver_win32\chromedriver")
    if str(barcodeData).__contains__("StartDooropen") :
        b = driver.get(str("https://blynk.cloud/dashboard/83389/global/filter/502861/organization/83389/devices/277853/dashboard"))
        driver.maximize_window()
        time.sleep(3)
        if str(barcodeData) == "StartDooropen":
            email = "takahashi-r@ichiharapower.jp"
            door = '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/section/main/section/aside/div/div/div[5]/a/div/div[3]'
        else:
            email = "nakai-t@ichiharapower.jp"
            door = '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/aside/div/div/div[4]'

        try:
            username = driver.find_element_by_id("email")
            username.send_keys(email)
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password.send_keys("Ipc_1503")
            #  driver.find_element_by_name("ログイン").click()

            PressLogInButton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/form/div[5]/div/div/div/button'))

            )
            PressLogInButton.click()
            time.sleep(3)

            try:
                closeAd = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]'))

                )
                closeAd.click()
            except:
                print("no Advertisment")
            time.sleep(3)





 # Spot Shutter Open
            selectSpotShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                door))

            )
            selectSpotShutter.click()

            openSpotShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            openSpotShutter.click()
            time.sleep(10)
            #to reset the open button back to original state
            openSpotShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            openSpotShutter.click()
            # spot shutter close timer
            time.sleep(65)  # seconds
            closeSpotShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            closeSpotShutter.click()
            time.sleep(10)
            closeSpotShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            closeSpotShutter.click()
            time.sleep(2)

        except:
            print("shutter error")


    elif  str(barcodeData).__contains__("GtDoorOpen"):
        b = driver.get(
            str("https://blynk.cloud/dashboard/83386/global/filter/502832/organization/83386/devices/277834/dashboard"))
        driver.maximize_window()
        time.sleep(3)
        email = "nakai-t@ichiharapower.jp"
        door = '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/aside/div/div/div[4]'
        try:
            username = driver.find_element_by_id("email")
            username.send_keys(email)
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password.send_keys("Ipc_1503")
            #  driver.find_element_by_name("ログイン").click()

            PressLoginButton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/form/div[5]/div/div/div/button'))

            )
            PressLoginButton.click()
            time.sleep(3)
            try:
                closeAd = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]'))

                )
                closeAd.click()
            except:
                print("no Advertisment")
            time.sleep(3)

            # GT Shutter Open

            selectGTshutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/section/main/section/aside/div/div/div[5]/a[2]/div/div[3]'))

            )
            selectGTshutter.click()

            # GtShutterbeOpenTimer
            # seconds
            # Press GTdoor open Button
            openGtShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            openGtShutter.click()
            time.sleep(10)
            # Press GTdoor Button  again to reset the open Button
            openGtShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            time.sleep(2)
            openGtShutter.click()
            # Gt Boiler shutter close
            SelectGtBoilerDoor = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/section/main/section/aside/div/div/div[5]/a[1]/div/div[3]'))

            )
            SelectGtBoilerDoor.click()

            PressGtBoilerClose = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))

            )
            PressGtBoilerClose.click()
            time.sleep(10)
            #Press GTdoor Button  again to reset the close Button
            PressGtBoilerClose = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))

            )
            PressGtBoilerClose.click()


            SelectGtshutterOffice = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/section/main/section/aside/div/div/div[5]/a[2]/div/div[3]'))

            )
            SelectGtshutterOffice.click()




            #Press Gt shutter close button after 2 mins
            # GT shutter Closer Timer
            time.sleep(125)  # seconds
            closeGTshutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            closeGTshutter.click()
            time.sleep(10)
            # Press GTdoor Button  again to reset the open Button
            closeGTshutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            closeGTshutter.click()
            time.sleep(2)

        except:
            print("GT error ")
 #'''This is for ST Shutter'''
    #NOTE: In line 252 please type "StDoorOpen"  inside the  contains bracket  to test the ST shutter

        ''' elif str(barcodeData).__contains__(""):#StDoorOpen
        b = driver.get(
            str("https://blynk.cloud/dashboard/83389/global/filter/502861/organization/83389/devices/277853/dashboard"))
        driver.maximize_window()
        time.sleep(3)

        email = "takahashi-r@ichiharapower.jp"


        try:
            username = driver.find_element_by_id("email")
            username.send_keys(email)
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password.send_keys("Ipc_1503")
            #  driver.find_element_by_name("ログイン").click()

            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/form/div[5]/div/div/div/button'))

            )                               
            password.click()
            time.sleep(3)

            try:
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]'))

                )
                password.click()
            except:
                print("no Advertisment")
            time.sleep(3)

            # ST Shutter Open

            SelectSTShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div/div[1]/div[3]/div/div[2]/section/section/main/section/aside/div/div/div[5]/a/div/div[3]'))

            )
            SelectSTShutter.click()
            #press open button
            OpenStShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            OpenStShutter.click()
            time.sleep(10)
            #reset the open button
            OpenStShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH1"]/div/div[2]/div/button'))
            )
            OpenStShutter.click()
            # spot shutter close timer
            time.sleep(65)  # seconds
            #press the close button
            CloseSTShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            CloseSTShutter.click()
            time.sleep(10)
            #reset the close button
            CloseSTShutter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="WEB_SWITCH3"]/div/div[2]/div/button'))
            )
            CloseSTShutter.click()
            time.sleep(2)
        except:
            print("StShutter Close error")'''


            # /html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]


#this is used for select mission and press Data capture button
    identifyElement = "Mission"
    identifyElement2 = "Datacapture"
    if str(barcodeData).__contains__(identifyElement) or str(barcodeData).__contains__(identifyElement2):
        b = driver.get(("https://192.168.10.166/control_room"))
        driver.maximize_window()
        time.sleep(3)
        try:
            username = driver.find_element_by_id("details-button")
            username.click()
            time.sleep(1)
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "proceed-link"))
            )
            password.click()

            #  driver.find_element_by_name("ログイン").click()

            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section/form/div[1]/div[2]/div[1]/div[2]/input'))

            )
            password.send_keys("admin")
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section/form/div[1]/div[2]/div[3]/div[2]/input'))

            )
            password.send_keys("qsk2pxe5qmq4")

            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section/form/div[2]/div[2]/div[2]/button'))
            )
            password.click()

            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="home"]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/a'))
            )
            password.click()

            # obtain parent window handle
            # parent = driver.window_handles[0]
            # obtain browser tab window
            # chld = driver.window_handles[1]
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(10)
        except:
            print("error")
        if str(barcodeData).__contains__(identifyElement):

            try:
                #  press the play mission button
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div/div[3]/div[1]'))
                )
                password.click()
                #  select the required mission
                if str(barcodeData).__contains__("Mission1"):
                    missionSelection = '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/div[9]'
                elif str(barcodeData).__contains__("Mission2"):
                    missionSelection = '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/div[10]'
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         missionSelection))
                )
                password.click()
                time.sleep(2)
                # Press the mission confirm Button
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[2]/div/div/div[2]/button'))
                    # //*[@id="root"]/div/div/div/div/div/div[2]/div/div/div[2]/button
                )
                password.click()
                time.sleep(5)
            except:
                print("d")
        else:
           #This is used for press Datacapture button depends on number of times
            emp_str = ""
            for m in str(barcodeData):
                if m.isdigit():
                    emp_str = emp_str + m
            print("Find numbers from string:", emp_str)

            for i in range(0, int(emp_str)):
                time.sleep(1)
                print(i)


def time_out_exit() :
    print("No QR Code Found")
    os._exit(0)()
    #cv2.destroyWindow()

#scan the qrcode by camera
def open_scanner():
  #  myTimer.start()
    #add cv2.CAP_DSHOW on windows while developing, remove on RBPI
    #cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        #cv2.imshow('My Title', frame)
        code = cv2.waitKey(1)
        if code == ord('q'):

            exit()

globals()['myTimer'] = Timer(10.0, time_out_exit)
if __name__ == '__main__':
    open_scanner()




