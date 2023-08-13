import tkinter as tk
from tkinter import PhotoImage
from PIL import Image , ImageFilter

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry(f"{450}x{500}")

        self.convert_jpg_to_ppm("calculator-figures-accounting-dial.jpg", "calculator-figures-accounting-dial.ppm")

        self.background_image = PhotoImage(file="calculator-figures-accounting-dial.ppm")  # Replace with your image path
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        def blur_background(self, ppm_path, blurred_ppm_path):
                  ppm_image = Image.open("calculator-figures-accounting-dial.ppm")
                  blurred_image = ppm_image.filter(ImageFilter.GaussianBlur(80))  # Apply blur filter
                  blurred_image.save(blurred_ppm_path, "ppm")
        
        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Helvetica", 30), fg="red")  # Set font color
        self.result_label.grid(row=0, column=0, columnspan=4, pady=20)
    
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        self.entry = ""

        row_val = 1
        col_val = 0

        for button in self.buttons:
            tk.Button(root, text=button, font=("Helvetica", 30), command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=10, pady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def convert_jpg_to_ppm(self, jpg_path, ppm_path):
        jpg_image = Image.open(jpg_path)
        jpg_image.save(ppm_path, "ppm")

    def button_click(self, button):
        if button == "=":
            try:
                self.result_var.set(eval(self.entry))
            except:
                self.result_var.set("Error")
        elif button == "C":
            self.entry = ""
            self.result_var.set("")
        else:
            self.entry += button
            self.result_var.set(self.entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
