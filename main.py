import tkinter

window = tkinter.Tk()

def button_clicked():
    label_value["text"] = int(input.get()) * 1.60934

window.title("Miles to KM")
window.minsize(200,100)

input = tkinter.Entry(width=10)
input.grid(column=1,row = 0)

label = tkinter.Label(text="miles")
label.grid(column=2, row=0)

label_is_equal = tkinter.Label(text="is equal to")
label_is_equal.grid(column=0, row=1)

label_value = tkinter.Label(text="0")
label_value.grid(column=1, row=1)

label_km = tkinter.Label(text="kilometers")
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()