import cv2
import mss
import time
import numpy
# HSV - диапазон тонов цвета, без понятия как задать диапазон, чсито наугад, если неугадать, не будет отслеживать и условие if dArea > 100 не отработает
upper_range = numpy.array([300, 220, 207])
lower_range = numpy.array([0, 163, 196])

with mss.mss() as sct:
    monitor = {"top": 840, "left": 390, "width": 215, "height": 200}

    while True:
        last_time = time.time()
        img = numpy.array(sct.grab(monitor))
        cv2.imshow("OpenCV/Numpy normal", img)
        # преобразуем RGB картинку в HSV модель
        hsv =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # применяем цветовой фильтр
        thresh = cv2.inRange(hsv, lower_range, upper_range)
        # вычисляем моменты изображения
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        # будем реагировать только на те моменты,
        # которые содержать больше 100 пикселей(надо переделать)
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
#            cv2.circle(img, (x, y), 10, (0, 255, 0), -1)
            cv2.circle(img, (x, y), 5, (0, 255, 0), 2)

        else:

            print("BANKY PIET")
            time.sleep(1)
        cv2.imshow('result', img)
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
