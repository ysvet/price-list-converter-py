GRAY = "#f3f4ed"
MID_GRAY = "#536162"
DARK_GRAY = "#424642"
BROWN = "#c06014"
FONT_NAME = "Courier"
WORLDCALL_FILE="Worldcall_Premium_EUR.xls"


from tkinter import *
import pandas
import glob

window = Tk()
window.title("Price-list converter")
window.minsize(width=250, height=250)
window.config(padx=15, pady=15, bg=GRAY)


def idt_file():
    try:
        my_label_convert.config(text="T357 file has been created")
        return glob.glob("*.csv")[0]
    except Exception as error:
        print(error)
        my_label_convert.config(text="No files to convert found")


def worldcall_file():
    try:
        my_label_convert.config(text="T357 file has been created", fg=DARK_GRAY)
        return glob.glob(WORLDCALL_FILE)[0]
    except Exception as error:
        print(error)
        my_label_convert.config(text="No files to convert found", fg=BROWN)
        # except Exception as error:
    #     print(error)


def button_clicked():
    selected_operator = radio_state.get()

    if selected_operator == 1:
        idt()
        idt_file()

    elif selected_operator == 2:
        worldcall_file()
        worldcall()

    elif not selected_operator:
        my_label_convert.config(text="Please select an operator", bg=GRAY, fg=BROWN)




def idt():
    if idt_file():
        data = pandas.read_csv(idt_file())
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
    else:
        pass


def worldcall():
    if worldcall_file():
        data = pandas.read_excel(worldcall_file(), 3)
        data_1 = {row["Destination"]: row["First Price"] for (index, row) in data.iterrows()
                  if not row["First Price"] == 0}

        data_ser = pandas.Series(data_1).to_frame()
        pandas.DataFrame.from_dict(data_ser).to_excel("T357.xls", header=False)
    else:
        pass


my_label_text = Label(text="Price-list converter", font=("Arial", 14, "bold"), fg=GRAY)
my_label_text.grid(column=0, row=0, )
my_label_text.config(padx=20, pady=20, bg=MID_GRAY)

my_label_convert = Label(text=" ", font=("Arial", 8, "bold"))
my_label_convert.grid(column=0, row=4, sticky="ew")
my_label_convert.config(padx=20, pady=20, bg=GRAY)

# def select_operator():
#
radio_state = IntVar()
radiobutton1 = Radiobutton(text="IDT", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Worldcall", value=2, variable=radio_state)
radiobutton1.grid(column=0, row=1, sticky="w")
radiobutton2.grid(column=0, row=2, sticky="w")
radiobutton2.config(padx=10, pady=5, bg=GRAY)
radiobutton1.config(padx=10, pady=10, bg=GRAY)

button = Button(text="Convert", font=("Arial", 12, "bold"), bg=BROWN, fg=GRAY, command=button_clicked)
button.grid(column=0, row=3, sticky="ew")

window.mainloop()
