from tkinter import *
from tkinter import ttk
from factors import conversion_factors


def update_unit_menu(*args):
    from_unit_menu['values'] = tuple(conversion_factors[from_quantity.get().lower()].keys())
    to_unit_menu['values'] = tuple(conversion_factors[from_quantity.get().lower()].keys())


def convert(*args):
    result_value = "{0:.4f}".format(conversion_factors[from_quantity.get().lower()][from_unit.get()][to_unit.get()](
        float(entry.get())))
    result_string = f"{entry.get()} {from_unit.get()} = {result_value} {to_unit.get()}"
    result.set(result_string)

'''
# fuction for testing
def convert(from_quantity, from_unit, to_unit, value):
    result_value = "{0:.4f}".format(conversion_factors[from_quantity.lower()][from_unit][to_unit](float(value)))
    return f"{value} {from_unit} = {result_value} {to_unit}"
'''

root = Tk()
root.title("Unit converter")

factors_label = Label(root, text="Quantity")
factors_label.grid(row=1, column=0, padx=10, pady=10)

from_quantity = StringVar(root)
quantity_menu = ttk.Combobox(root, textvariable=from_quantity, values=tuple([x.capitalize() for x in conversion_factors.keys()]))
quantity_menu.bind("<<ComboboxSelected>>", update_unit_menu)
quantity_menu.grid(row=1, column=1, padx=10, pady=10)

from_unit_label = Label(root, text="From unit")
from_unit_label.grid(row=2, column=0, padx=10, pady=10)

from_unit = StringVar(root)
from_unit_menu = ttk.Combobox(root, textvariable=from_unit, state="readonly")
from_unit_menu.grid(row=2, column=1, padx=10, pady=10)

to_unit_label = Label(root, text="To unit")
to_unit_label.grid(row=3, column=0, padx=10, pady=10)

to_unit = StringVar(root)
to_unit_menu = ttk.Combobox(root, textvariable=to_unit, state="readonly")
to_unit_menu.grid(row=3, column=1, padx=10, pady=10)

entry_label = Label(root, text="Enter a value")
entry_label.grid(row=4, column=0, padx=10, pady=10)

entry = Entry(root)
entry.grid(row=4, column=1, padx=10, pady=10)

convert_button = Button(root, text="Convert", command=convert)
convert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

result = StringVar()
result_entry = Entry(root, state="readonly", textvariable=result)
result_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky="we")

root.mainloop()