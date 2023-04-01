import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

      
        self.result = tk.StringVar()
        self.result.set("0")
        self.result_label = tk.Label(self.root, textvariable=self.result, font=("Arial", 16), width=14, anchor="e", bg="white")
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text=self.buttons[i][j], width=3, height=1, font=("Arial", 14),
                                   command=lambda x=self.buttons[i][j]: self.button_click(x))
                button.grid(row=i+1, column=j)

        self.clear_button = tk.Button(self.root, text="C", width=3, height=1, font=("Arial", 14),
                                      command=lambda: self.button_click("C"))
        self.clear_button.grid(row=5, column=0)

    def button_click(self, key):
        if key == "C":
            # Clear the result
            self.result.set("0")
        elif key == "=":
            # Evaluate the expression and display the result
            try:
                result = eval(self.result.get())
                self.result.set(str(result))
            except:
                self.result.set("Error")
        else:
            if self.result.get() == "0":
                # Replace the initial 0 with the button press
                self.result.set(key)
            else:
                # Append the button press to the current result
                self.result.set(self.result.get() + key)

# Create the Tkinter window and the calculator
root = tk.Tk()
calculator = Calculator(root)

# Run the Tkinter event loop
root.mainloop()
