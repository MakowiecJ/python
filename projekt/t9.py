import tkinter as tk

class MobilePhone(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.title("Mobile Phone")
        self.geometry("400x700")

        # Create a label to display the screen
        self.screen = tk.Label(self, text="", font=("Arial", 20))
        self.screen.pack()

        # Create a frame to hold the keypad buttons
        self.keypad_frame = tk.Frame(self)
        self.keypad_frame.pack()

        # Create the keypad buttons
        self.keypad_buttons = []
        for i in range(1, 10):
            button = tk.Button(self.keypad_frame, text=str(i), command=lambda i=i: self.add_digit(i), height=5, width=3)
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
            self.keypad_buttons.append(button)
        tk.Button(self.keypad_frame, text="*", command=self.add_star, height=3, width=3).grid(row=3, column=0)
        tk.Button(self.keypad_frame, text="0", command=lambda: self.add_digit(0), height=3, width=3).grid(row=3, column=1)
        tk.Button(self.keypad_frame, text="#", command=self.add_pound, height=3, width=3).grid(row=3, column=2)

        # Create a button to clear the screen
        self.clear_button = tk.Button(self, text="Clear", command=self.clear_screen, height=3, width=3)
        self.clear_button.pack()

    def add_digit(self, digit):
        # Update the screen with the new digit
        self.screen.config(text=self.screen.cget("text") + str(digit))

    def add_star(self):
        # Update the screen with the star character
        self.screen.config(text=self.screen.cget("text") + "*")

    def add_pound(self):
        # Update the screen with the pound character
        self.screen.config(text=self.screen.cget("text") + "#")

    def clear_screen(self):
        # Clear the screen
        self.screen.config(text="")

# Create and run the mobile phone GUI
app = MobilePhone()
app.mainloop()
