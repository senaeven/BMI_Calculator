import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(250, 200)
window.config(padx=30, pady=30) #koyacağımız şeyler daha ortadan başladı.

def calculate_bmi():
    height = height_entry.get()
    weight = weight_entry.get()

    if weight == "" or height == "":
        result_label.config(text = "Cannot be left blank.")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number.")


#WEIGHTS
weight_label = tkinter.Label(text="Enter your weight (kg)", font=("Arial", 14, "normal"))
weight_label.pack()

weight_entry = tkinter.Entry(width=10)
weight_entry.pack()

#HEIGHTS
height_label = tkinter.Label(text="Enter your height (cm)", font=("Arial", 14, "normal"))
height_label.pack()

height_entry = tkinter.Entry(width=10)
height_entry.pack()

calculate_button = tkinter.Button(text="Calculate",command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {bmi}.\n You are "
    if bmi <=16.0:
        result_string += "severly underweight."
    elif 16.0 < bmi <= 18.4:
        result_string += "underweight."
    elif 18.4 < bmi <= 24.9:
        result_string += "normal."
    elif 24.9 < bmi <= 29.9:
        result_string += "overweight."
    elif 29.9 < bmi <= 34.9:
        result_string += "moderately obese."
    elif 34.9 < bmi <= 39.9:
        result_string += "severely obese."
    else:
        result_string += "morbidly obese"
    return result_string

window.mainloop()