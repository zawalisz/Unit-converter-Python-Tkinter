#units = ["meters", "yards", "feet", "centimeters", "kilometers", "miles"]
#units = ["celsius", "fahrenheit", "kelvin"]
units = ["ton", "kilogram", "gram"]

for i in units:
    for j in units:
        print('assert convert("weight", "'+ i +'", "'+ j +'", 2) == "2 '+ i +' = 2.0000 '+ j +'"')