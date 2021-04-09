from tkinter import *
import pandas

window = Tk()
window.title("Price-list converter")
window.minsize(width=250, height=250)
window.config(padx=15, pady=15)


def button_clicked():
    selected_operator = radio_state.get()

    if selected_operator == 1:
        idt()
    if selected_operator == 2:
        worldcall()
    if selected_operator:
        my_label_convert.config(text="T357 file has been created")
    else:
        my_label_convert.config(text="Please select an operator")


def idt():
    data = pandas.read_csv("file.csv")
    data_no_mexico = {row["Dial Code"]: row["Gold $ USD"] for (index, row) in data.iterrows()
                      if not str(row["Dial Code"]).startswith("522")
                      and not str(row["Dial Code"]).startswith("523")
                      and not str(row["Dial Code"]).startswith("524")
                      and not str(row["Dial Code"]).startswith("525")
                      and not str(row["Dial Code"]).startswith("526")
                      and not str(row["Dial Code"]).startswith("527")
                      and not str(row["Dial Code"]).startswith("528")
                      and not str(row["Dial Code"]).startswith("529")}
    data_no_mexico_ser = pandas.Series(data_no_mexico).to_frame()
    pandas.DataFrame.from_dict(data_no_mexico_ser).to_excel("T357.xls", header=False)


def worldcall():
    data = pandas.read_excel(r"Worldcall_Premium_EUR.xls", 3)
    data_1 = {row["Destination"]: row["First Price"] for (index, row) in data.iterrows()
              if not row["First Price"] == 0}

    data_ser = pandas.Series(data_1).to_frame()
    pandas.DataFrame.from_dict(data_ser).to_excel("T357.xls", header=False)


my_label_text = Label(text="Price-list converter", font=("Arial", 14, "bold"))
my_label_text.grid(column=0, row=0, )
my_label_text.config(padx=20, pady=20)

my_label_convert = Label(text=" ", font=("Arial", 8, "bold"))
my_label_convert.grid(column=0, row=4, sticky="ew")
my_label_convert.config(padx=20, pady=20)

# def select_operator():
#
radio_state = IntVar()
radiobutton1 = Radiobutton(text="IDT", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Worldcall", value=2, variable=radio_state)
radiobutton1.grid(column=0, row=1, sticky="w")
radiobutton2.grid(column=0, row=2, sticky="w")
radiobutton2.config(padx=10, pady=10)
radiobutton1.config(padx=10, pady=5)

button = Button(text="Convert", bg="azure2", command=button_clicked)
button.grid(column=0, row=3, sticky="ew")

window.mainloop()
