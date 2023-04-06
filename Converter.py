import tkinter as tk
from factors import conversion_factors

root = tk.Tk()
root.title("Konwerter jednostek")

quantities = ["distance", "weight"]

distance = ["milimetr", "centymetr", "metr"]
weight = ["gram", "kilogram", "tona"]

from_quantity = tk.StringVar(root)
from_quantity.set(quantities[0])

def update_unit_menu(*args):
    selected_quantity = from_quantity.get()
    if selected_quantity == "distance":
        unit_menu["menu"].delete(0, "end")
        for unit in distance:
            unit_menu["menu"].add_command(label=unit, command=tk._setit(from_unit, unit))
        from_unit.set(distance[0])
    elif selected_quantity == "weight":
        unit_menu["menu"].delete(0, "end")
        for unit in weight:
            unit_menu["menu"].add_command(label=unit, command=tk._setit(from_unit, unit))
        from_unit.set(weight[0])
    else:
        from_unit.set("Wybierz wielkość fizyczną")
        unit_menu["menu"].delete(0, "end")
        unit_menu["menu"].add_command(label="Wybierz wielkość fizyczną", command=tk._setit(from_unit, "Wybierz wielkość fizyczną"))


def convert():
    value = float(entry.get())
    from_unit_value = from_unit.get()
    physical_quantity_value = from_quantity.get()
    converted_values = {}
    if physical_quantity_value in conversion_factors and from_unit_value in conversion_factors[physical_quantity_value]:
        converted_values = conversion_factors[physical_quantity_value][from_unit_value]
    converted_value = ""
    for to_unit, factor in converted_values.items():
        converted_value += f"{value * factor:.2f} {to_unit}\n"
    result_entry.delete(0, tk.END)
    result.set(converted_value)

from_unit = tk.StringVar(root)

from_quantity.trace("w", update_unit_menu)

# Widget OptionMenu
quantity_menu = tk.OptionMenu(root, from_quantity, *quantities)
quantity_menu.grid(row=1, column=0, padx=10, pady=10)

unit_menu = tk.OptionMenu(root, from_unit, "Wybierz wielkość fizyczną")
unit_menu.grid(row=2, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=3, column=0, padx=10, pady=10)

convert_button = tk.Button(root, text="Konwertuj", command=convert)
convert_button.grid(row=4, column=0, padx=10, pady=10)

# Pole wyniku
result = tk.StringVar()
result.set("")
result_entry = tk.Entry(root, state="readonly", textvariable=result)
result_entry.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()