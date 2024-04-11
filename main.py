import pandas as pd

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


def main():
    is_on = True
    while is_on:
        morse_or_text = input("Do you want to convert Morse code to text (Enter 'M2T') or text to Morse code (Enter 'T2M'), to Quit (Enter 'Q')? ").upper()
        if morse_or_text == "M2T":
            message    = input("What is your Morse Code? ")
            text = get_text(message)
            print(f"Text: {text}")
        elif morse_or_text == "T2M":
            message    = input("What is your text message? ")
            morse_code = get_code(message)
            print(f"Morse Code: {morse_code}")
        elif morse_or_text == "Q":
            is_on = False
        else:
            main()
    


if __name__ == "__main__":
    main()