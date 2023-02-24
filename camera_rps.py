import cv2
from keras.models import load_model
import numpy as np
import time
import random

def get_machine_output():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    max_time = 3
    start_time = time.time()

    while (time.time() - start_time) < max_time: 
    # while True:     
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        # print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    print(prediction, 'prediction')
    return prediction

def get_prediction():
    predictions = get_machine_output()
    highest_index = np.argmax(predictions)
    if highest_index == 0:
        return 'Rock'
    elif highest_index == 1:
        return 'Paper'
    elif highest_index == 2:
        return 'Scissors'
    else:
        return None
    
def get_winner():
    ''' return -1 if user lost, 0 if tied, 1 if won'''
    user_choice = get_prediction()
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    print(f'you have chosen: {user_choice}, computer has chosen: {computer_choice}')
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'paper'):
        print("You lost")
        return -1
    elif computer_choice == user_choice:
        print("It is a tie!")
        return 0
    else:
        print("You won!")
        return 1

def game():
    """ Repeat game until a player wins three times """
    computer_wins = 0
    user_wins = 0
    # while (user_wins < 3) or (computer_wins < 3):
    while True:
        print(f'current score for user: {user_wins}, computer: {computer_wins}')
        score = get_winner()
        if score == 1:
            user_wins += 1
        elif score == -1:
            computer_wins += 1
        # break when either score reached 3
        if user_wins == 3:
            break
        if computer_wins == 3:
            break

# print(f'You chose {get_prediction()}')
game()