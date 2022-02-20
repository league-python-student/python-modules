from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    bDay = simpledialog.askstring(title = "Birthday", prompt = "Enter your Birthday in this format Month/Day (eg. mm/dd).")

    if bDay == "02/20":
        messagebox.showinfo(message="Happy Birthday!")
    else:
        messagebox.showinfo(message="Happy UnBirthday!")

