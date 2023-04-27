import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height/100)**2
    result_label.config(text="BMI: {:.2f}".format(bmi))

# Create a GUI window
window = tk.Tk()
window.title("BMI Calculator")

# Create GUI widgets
height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()