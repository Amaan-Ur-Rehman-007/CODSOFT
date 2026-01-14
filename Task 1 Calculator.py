import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display Screen
        input_frame = self.create_display()
        input_frame.pack(side=tk.TOP)

        # Buttons
        btns_frame = self.create_buttons()
        btns_frame.pack()

    def create_display(self):
        frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_field = tk.Entry(frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        return frame

    def create_buttons(self):
        frame = tk.Frame(self.root, width=312, height=322.5, bg="grey")
        
        # Row 1
        self.create_btn(frame, "C", 1, 0, 3, lambda: self.btn_clear(), "#ffcccc")
        self.create_btn(frame, "/", 1, 3, 1, lambda: self.btn_click("/"))

        # Row 2
        self.create_btn(frame, "7", 2, 0, 1, lambda: self.btn_click(7))
        self.create_btn(frame, "8", 2, 1, 1, lambda: self.btn_click(8))
        self.create_btn(frame, "9", 2, 2, 1, lambda: self.btn_click(9))
        self.create_btn(frame, "*", 2, 3, 1, lambda: self.btn_click("*"))

        # Row 3
        self.create_btn(frame, "4", 3, 0, 1, lambda: self.btn_click(4))
        self.create_btn(frame, "5", 3, 1, 1, lambda: self.btn_click(5))
        self.create_btn(frame, "6", 3, 2, 1, lambda: self.btn_click(6))
        self.create_btn(frame, "-", 3, 3, 1, lambda: self.btn_click("-"))

        # Row 4
        self.create_btn(frame, "1", 4, 0, 1, lambda: self.btn_click(1))
        self.create_btn(frame, "2", 4, 1, 1, lambda: self.btn_click(2))
        self.create_btn(frame, "3", 4, 2, 1, lambda: self.btn_click(3))
        self.create_btn(frame, "+", 4, 3, 1, lambda: self.btn_click("+"))

        # Row 5
        self.create_btn(frame, "0", 5, 0, 2, lambda: self.btn_click(0))
        self.create_btn(frame, ".", 5, 2, 1, lambda: self.btn_click("."))
        self.create_btn(frame, "=", 5, 3, 1, lambda: self.btn_equal(), "#ccffcc")
        
        return frame

    def create_btn(self, frame, text, row, col, colspan, command, bg="white"):
        tk.Button(frame, text=text, fg="black", width=10 * colspan, height=3, bd=0, bg=bg, cursor="hand2", command=command).grid(row=row, column=col, padx=1, pady=1, sticky="nsew", columnspan=colspan)

        frame.grid_columnconfigure(col, weight=1)
        frame.grid_rowconfigure(row, weight=1)

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()