from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdrawal()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    random_number = random.randint(0, 3)
    # 2. Print your variable to the console
    print(random_number)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring(None, prompt = "Enter something awesome.")
    # 4. If your variable is  0
    if random_number == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(message = awesome + "is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    elif
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
