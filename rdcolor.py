
def RGB_ColorPicker():
    r = (0, 255)
    g = (0, 255)
    b = (0, 255)
    ColorPick = f"Your Random color is ({r}, {g}, {b})"
    return ColorPick

def NewColorPrompt():
    ColorPick = RGB_ColorPicker()
    print(ColorPick)
    print("Would you like a new color? (y/n)")
    Option = input()
    if Option == "y":
        NewColorPrompt()
    else:
        print("Thanks for using the color picker. Happy creating!")

def main():
    while True:
        NewColorPrompt()
        Option = input("Would you like a new color? (y/n)").strip().lower()
        if Option == "n":
            break

if __name__ == "__main__":
    main()
