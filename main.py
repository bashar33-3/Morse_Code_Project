import pandas as pd
import time
import pygame


data = pd.read_csv('morse_code.csv')


def get_code(word : str):
    morse_code = []
    ### make a list out of the word 
    word_list = [letter.upper() for letter in word]
    for letter in word_list:
        if letter in data.Character.values:
            code = data[data.Character==letter]["Morse_Code"].values.item()
            morse_code.append(code)
        else:
            if len(morse_code) > 0 and morse_code[-1] == "/":
                morse_code.pop(-1)
            else:
                pass
    return " ".join(morse_code)

def get_text(code : str):
    text = []
    morse_code_list = code.split(" ")
    
    for lcode in morse_code_list:
        if lcode in data.Morse_Code.values:
            letter = data[data.Morse_Code==lcode]["Character"].values.item()
            text.append(letter)
        else:
            if len(text) > 0 and text[-1] == " ":
                text.pop(-1)
            else:
                pass
    return "".join(text)

def play_morse_code(morse_code):
    pygame.mixer.init()
    frequency = 440  # Set the frequency of the tone (440 Hz is standard)
    duration_short = 400  # Duration of short beep in milliseconds
    duration_long = 900  # Duration of long beep in milliseconds
    volume = 0.5  # Set the volume (0.0 to 1.0)

    for char in morse_code:
        if char == '.':
            pygame.mixer.Sound.play(pygame.mixer.Sound("sound/short_beep.wav"))
            time.sleep(duration_short / 1000)
        elif char == '-':
            pygame.mixer.Sound.play(pygame.mixer.Sound("sound/long_beep.wav"))
            time.sleep(duration_long / 1000)
        elif char == ' ' or char == '/':
            time.sleep(duration_short / 1000)  # Pause between letters

def main():
    is_on = True
    while is_on:
        morse_or_text = input("To convert Morse code to text (Enter 'M2T'), or text to Morse code (Enter 'T2M'), to Generate Morse code sound (Enter 'S'), to Quit (Enter 'Q')? ").upper()
        if morse_or_text == "M2T":
            message    = input("What is your Morse Code? ")
            text = get_text(message)
            print(f"Text: {text}")
        elif morse_or_text == "T2M":
            message    = input("What is your text message? ")
            morse_code = get_code(message)
            print(f"Morse Code: {morse_code}")
            
            play_sound = False
            while not play_sound:
                play_code = input("Do you want to play the code sound (Y or N)? ").upper()
                if play_code == "Y":
                    play_morse_code(morse_code)
                    play_sound = True
                elif play_code == "N":
                    main()
                else:
                    play_sound=False

        elif morse_or_text == "Q":
            is_on = False

        elif morse_or_text == "S":
            mcode = input("Enter Morse Code only use ('.' and '-'): ")
            play_morse_code(mcode)
    


if __name__ == "__main__":
    main()