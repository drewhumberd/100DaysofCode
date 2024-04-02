import tkinter

def button_clicked():
    miles = int(miles_input.get())
    km_output["text"] = str("{:.1f}".format(miles * 1.609))

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=25, pady=25)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=0, row=0, columnspan=2, padx=2, pady=2)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0, padx=2, pady=2)

equal_to = tkinter.Label(text="is equal to")
equal_to.grid(column=0, row=1, padx=2, pady=2)

km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1, padx=2, pady=2)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1, padx=2, pady=2)

button = tkinter.Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2, padx=2, pady=2)

window.mainloop()