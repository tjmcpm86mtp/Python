import cv2
from tkinter import Tk

app = Tk()
app.title('デスクトップアプリ')
app.geometry('300x300')
# app.mainloop()q

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

app.mainloop()
print("Finished!")
