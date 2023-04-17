from converter import convert


def test_convert_length():
    assert convert("length", "meters", "meters", 2) == "2 meters = 2.0000 meters"
    assert convert("length", "meters", "yards", 2) == "2 meters = 2.1872 yards"
    assert convert("length", "meters", "feet", 2) == "2 meters = 6.5617 feet"
    assert convert("length", "meters", "centimeters", 2) == "2 meters = 200.0000 centimeters"
    assert convert("length", "meters", "kilometers", 2) == "2 meters = 0.0020 kilometers"
    assert convert("length", "meters", "miles", 2) == "2 meters = 0.0012 miles"

    assert convert("length", "yards", "meters", 2) == "2 yards = 1.8288 meters"
    assert convert("length", "yards", "yards", 2) == "2 yards = 2.0000 yards"
    assert convert("length", "yards", "feet", 2) == "2 yards = 6.0000 feet"
    assert convert("length", "yards", "centimeters", 2) == "2 yards = 182.8822 centimeters"
    assert convert("length", "yards", "kilometers", 2) == "2 yards = 0.0018 kilometers"
    assert convert("length", "yards", "miles", 2) == "2 yards = 0.0011 miles"

    assert convert("length", "feet", "meters", 2) == "2 feet = 0.6096 meters"
    assert convert("length", "feet", "yards", 2) == "2 feet = 0.6667 yards"
    assert convert("length", "feet", "feet", 2) == "2 feet = 2.0000 feet"
    assert convert("length", "feet", "centimeters", 2) == "2 feet = 60.9600 centimeters"
    assert convert("length", "feet", "kilometers", 2) == "2 feet = 0.0066 kilometers"
    assert convert("length", "feet", "miles", 2) == "2 feet = 0.0041 miles"

    assert convert("length", "centimeters", "meters", 2) == "2 centimeters = 0.0200 meters"
    assert convert("length", "centimeters", "yards", 2) == "2 centimeters = 0.0219 yards"
    assert convert("length", "centimeters", "feet", 2) == "2 centimeters = 0.0656 feet"
    assert convert("length", "centimeters", "centimeters", 2) == "2 centimeters = 2.0000 centimeters"
    assert convert("length", "centimeters", "kilometers", 200) == "200 centimeters = 0.0020 kilometers"
    assert convert("length", "centimeters", "miles", 2) == "2 centimeters = 124274.5473 miles"

    assert convert("length", "kilometers", "meters", 2) == "2 kilometers = 2000.0000 meters"
    assert convert("length", "kilometers", "yards", 2) == "2 kilometers = 2187.2200 yards"
    assert convert("length", "kilometers", "feet", 2) == "2 kilometers = 6561.6600 feet"
    assert convert("length", "kilometers", "centimeters", 2) == "2 kilometers = 200000.0000 centimeters"
    assert convert("length", "kilometers", "kilometers", 2) == "2 kilometers = 2.0000 kilometers"
    assert convert("length", "kilometers", "miles", 2) == "2 kilometers = 1.2427 miles"

    assert convert("length", "miles", "meters", 2) == "2 miles = 3218.6800 meters"
    assert convert("length", "miles", "yards", 2) == "2 miles = 3520.0000 yards"
    assert convert("length", "miles", "feet", 2) == "2 miles = 10560.0000 feet"
    assert convert("length", "miles", "centimeters", 2) == "2 miles = 321868.0000 centimeters"
    assert convert("length", "miles", "kilometers", 2) == "2 miles = 3.2187 kilometers"
    assert convert("length", "miles", "miles", 2) == "2 miles = 2.0000 miles"


def test_convert_temperature():
    assert convert("temperature", "celsius", "celsius", 2) == "2 celsius = 2.0000 celsius"
    assert convert("temperature", "celsius", "fahrenheit", 2) == "2 celsius = 35.6000 fahrenheit"      
    assert convert("temperature", "celsius", "kelvin", 2) == "2 celsius = 275.1500 kelvin"

    assert convert("temperature", "fahrenheit", "celsius", 2) == "2 fahrenheit = -16.6667 celsius"      
    assert convert("temperature", "fahrenheit", "fahrenheit", 2) == "2 fahrenheit = 2.0000 fahrenheit"
    assert convert("temperature", "fahrenheit", "kelvin", 2) == "2 fahrenheit = 256.4833 kelvin"  

    assert convert("temperature", "kelvin", "celsius", 2) == "2 kelvin = -271.1500 celsius"
    assert convert("temperature", "kelvin", "fahrenheit", 2) == "2 kelvin = -456.0700 fahrenheit"
    assert convert("temperature", "kelvin", "kelvin", 2) == "2 kelvin = 2.0000 kelvin"


def test_convert_weight():
    assert convert("weight", "ton", "ton", 2) == "2 ton = 2.0000 ton"
    assert convert("weight", "ton", "kilogram", 2) == "2 ton = 2000.0000 kilogram"
    assert convert("weight", "ton", "gram", 2) == "2 ton = 2000000.0000 gram"

    assert convert("weight", "kilogram", "ton", 2) == "2 kilogram = 0.0020 ton"
    assert convert("weight", "kilogram", "kilogram", 2) == "2 kilogram = 2.0000 kilogram"
    assert convert("weight", "kilogram", "gram", 2) == "2 kilogram = 2000.0000 gram"

    assert convert("weight", "gram", "ton", 2000) == "2000 gram = 0.0020 ton"
    assert convert("weight", "gram", "kilogram", 2) == "2 gram = 0.0020 kilogram"
    assert convert("weight", "gram", "gram", 2) == "2 gram = 2.0000 gram"


def test_convert_negatives():
    assert convert("length", "meters", "kilometers", 1) != "1 meters = 0.0020 kilometers"
    assert convert("temperature", "fahrenheit", "celsius", 1) != "1 fahrenheit = -16.6667 celsius"
    assert convert("weight", "gram", "kilogram", 1) != "1 gram = 0.0020 kilogram"


def test_convert_others():
    assert convert("length", "meters", "kilometers", 2.0) == "2.0 meters = 0.0020 kilometers"