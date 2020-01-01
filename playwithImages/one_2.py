import cv2

cap = cv2.VideoCapture(0)
#my = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('one.avi',my,20.0,(640,480))

while(True):
    ret, frame = cap.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #out.write(frame)

    cv2.imshow('king',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

# to save add additional lines ; uncomment all.
