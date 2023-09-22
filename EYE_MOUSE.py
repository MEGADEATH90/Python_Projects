import cv2
import mediapipe as mp
import mediapipe.python.solution_base
import pyautogui

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)

cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)  # vertical = 1
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    process_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmarks_points = process_image.multi_face_landmarks
    # print(all_face_landmarks_points)
    if all_face_landmarks_points:
        one_face_landmark_points = all_face_landmarks_points[0].landmark
        for id, landmark_points in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_points.x * window_w)
            y = int(landmark_points.y * window_h)
            if id == 1:
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)
                pyautogui.moveTo(mouse_x, mouse_y)
            cv2.circle(image, (x, y), 3, (0, 0, 255))

        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_points in left_eye:
            x = int(landmark_points.x * window_w)
            y = int(landmark_points.y * window_h)
            cv2.circle(image, (x, y), 3, (255, 0, 255))

        if (left_eye[0].y - left_eye[1].y) < 0.01:
            # pyautogui.click()
            # pyautogui.sleep(2)
            # print("clicked")
            mouse_x = int(screen_w / window_w * x)
            mouse_y = int(screen_h / window_h * y)
            pyautogui.scroll(mouse_x, mouse_y)
            print("scroll")
            pyautogui.sleep(2)

            pyautogui.doubleClick()
            print("doubleclick")
            pyautogui.sleep(2)

            pyautogui.leftClick()
            print("leftclick")
            pyautogui.sleep(2)

            pyautogui.dragRel()
            print("drag")
            pyautogui.sleep(2)

    cv2.imshow("Eye controller mouse", image)
    key = cv2.waitKey(1)
    if key == "q":
        break
cam.release()
cv2.destroyAllWindows()

# Left Eye:
#
# 145: Left pupil
# 159: Top-left corner of the left eye
# Right Eye:
#
# 374: Right pupil
# 386: Top-right corner of the right eye
