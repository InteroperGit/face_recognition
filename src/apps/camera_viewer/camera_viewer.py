import cv2

rtsp_url = "rtsp://admin:admin@192.168.1.10:554/stream"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
	print("Не удалось открыть видеопоток")
	exit()

while True:
	ret, frame = cap.read()

	if ret:
		cv2.imshow("RTSP Stream", frame)

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
	else:
		print("Ошибка получения кадров")
		break

cap.release()
cv2.destroyAllWindows()