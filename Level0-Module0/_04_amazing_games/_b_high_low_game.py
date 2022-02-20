from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(0, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for x in range(10):
        # 4. Ask the user to guess a number using a pop-up window, and save their response
        userResponse = simpledialog.askinteger(None, prompt = "Guess a number from 0-100.")
        # 5. If the guess is correct
        if userResponse == random_num:
            # 6. Win. Use 'sys.exit(0)' to end the program
            messagebox.showinfo(None, message = "Winner!")
            sys.exit(0)
        # 7. if the guess is high
        elif userResponse > random_num:
            # 8. Tell them it's too high
            messagebox.showinfo(None, message="Too high")
        # 9. Else if the guess is low
        elif userResponse < random_num:
            # 10. Tell them it's too low
            messagebox.showinfo(None, message="Too low")
    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(title= "Loser", message="You lost!")
    window.mainloop()
