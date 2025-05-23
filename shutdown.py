import cv2
import mediapipe as mp
import os
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)  # usa webcam



shutdown_triggered_time = None

def is_middle_finger_up(hand_landmarks):
    # IDs dos dedos: 0 - pulso, 4 - polegar, 8 - indicador, 12 - médio, 16 - anelar, 20 - mindinho
    middle_tip = hand_landmarks.landmark[12]
    middle_pip = hand_landmarks.landmark[10]
    
    # Considera "levantado" se a ponta (tip) está mais acima (menor valor Y) que a junta (pip)
    is_up = middle_tip.y < middle_pip.y

    # Confirma se os outros dedos estão abaixados
    finger_ids = [8, 16, 20]
    folded = all(hand_landmarks.landmark[i].y > hand_landmarks.landmark[i - 2].y for i in finger_ids)

    return is_up and folded

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_middle_finger_up(hand_landmarks):
                if shutdown_triggered_time is None:
                    shutdown_triggered_time = time.time()
                    print("Gesto detectado. Aguardando confirmação por 1 segundos...")
                elif time.time() - shutdown_triggered_time > 1:
                    print("Desligando o PC...")
                    os.system("shutdown /s /t 1")  # Windows
                    # os.system("shutdown now")   # Linux/macOS
                    break
            else:
                shutdown_triggered_time = None

    cv2.imshow("Detecção de Gesto", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
