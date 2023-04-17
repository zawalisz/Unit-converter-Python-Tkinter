conversion_factors = {
    "length": {
        "meters": {
            "meters": lambda x: x,
            "yards": lambda x: x * 1.0936,
            "feet": lambda x: x * 3.28084,
            "centimeters": lambda x: x * 100,
            "kilometers": lambda x: x / 1000.0,
            "miles": lambda x: x / 1000.0 / 1.60934
        },
        "yards": {
            "yards": lambda x: x,
            "meters": lambda x: x / 1.0936,
            "centimeters": lambda x: x / 1.0936 * 100,
            "feet": lambda x: 3 * x,
            "kilometers": lambda x: x * 0.0009144,
            "miles": lambda x: x * 0.0009144/ 1.60934
        },
        "centimeters": {
            "centimeters": lambda x: x,
            "meters": lambda x: x / 100.0,
            "yards": lambda x: x * 1.0936 / 100,
            "feet": lambda x: x * 3.28084 / 100,
            "kilometers": lambda x: x / 100 / 1000,
            "miles": lambda x: x * 100 * 1000 / 1.60934
        },
        "feet": {
            "feet": lambda x: x,
            "meters": lambda x: x / 3.28084,
            "yards": lambda x: x / 3.0,
            "centimeters": lambda x: x * 100 / 3.28084,
            "kilometers": lambda x: x * 3.28084 / 1000,
            "miles": lambda x: x * 3.28084 / 1000 / 1.60934
        },
        "miles": {
            "miles": lambda x: x,
            "kilometers": lambda x: x * 1.60934,
            "meters": lambda x: x * 1.60934 * 1000,
            "centimeters": lambda x: x * 1.60934 * 1000 * 100,
            "feet": lambda x: x * 5280,
            "yards": lambda x: x * 5280 / 3.0
        },
        "kilometers": {
            "kilometers": lambda x: x,
            "meters": lambda x: x * 1000,
            "centimeters": lambda x: x * 1000 * 100,
            "miles": lambda x: x / 1.60934,
            "yards": lambda x: x * 1093.61,
            "feet": lambda x: x * 1093.61 * 3
        }
    },
    
    "temperature": {
        "celsius": {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: x * 1.8 + 32,
            "kelvin": lambda x: x + 273.15,
        },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celsius": lambda x: (x - 32) * 5.0 / 9.0,
            "kelvin": lambda x: (x - 32) * 5.0 / 9.0 + 273.15,
        },
        "kelvin": {
            "kelvin": lambda x: x,
            "celsius": lambda x: x - 273.15,
            "fahrenheit": lambda x: 1.8 * (x - 273.15) + 32,
        }
    },

    "weight": {
        "ton": {
            "ton": lambda x: x,
            "kilogram": lambda x: x * 1000,
            "gram": lambda x: x * 1000 * 1000,
        },
        "kilogram": {
            "kilogram": lambda x: x,
            "ton": lambda x: x / 1000,
            "gram": lambda x: x * 1000,
        },
        "gram": {
            "gram": lambda x: x,
            "kilogram": lambda x: x / 1000,
            "ton": lambda x: x / 1000 / 1000,
        }
    }
}