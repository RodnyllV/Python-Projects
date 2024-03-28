
import customtkinter

# Static

units = {
    "Weight": {
        "lbs": {"kg": 0.453, "g": 453, "mg": 453592, "oz": 16},
        "oz": {"kg": 0.028, "g": 28.3, "mg": 28349.5, "lbs": .0625},
        "kg": {"g": 1000, "mg": 1000000, "lbs": 2.204, "oz": 35.2},
        "g": {"kg": 0.001, "mg": 1000, "lbs": .002, "oz": .035},
        "mg": {"g": 0.001,"kg": (0.001 / 1000), "lbs": 0, "oz": (0.035 / 1000)}
    },

    "Length": {
        "m": {"km": 0.001, "cm": 100, "mm": 1000, "in": 39.3, "ft": 3.28, "yd": 1.09, "mi": (1 / 1609)},
        "km": {"mm": 1000000, "cm": 100000, "m": 1000, "in": 39370, "ft": 3280, "yd": 1093, "mi": 0.621},
        "mm": {"cm": 0.1, "m": 0.001, "km": (1 / 1e6), "in": 0.039, "ft": (1 / 304), "yd": (1 / 914), "mi": (1 / 1.609e6)},
        "cm": {"mm": 10, "m": 0.01, "km": 1e-5, "in": 0.393, "ft": 0.032, "yd": 0.0109, "mi": 6.21e-6},
        "in": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 0.254e-5, "ft": (1 / 12), "yd": (1 / 36), "mi": 1.57e-5},
        "ft": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": (1 / 3281), "in": 12, "yd": (1 / 3), "mi": (1 / 5280)},
        "yd": {"mm": 914.4, "cm": 91.44, "m": 0.9144, "km": (1 / 1094), "in": 36, "ft": 3, "mi": (1 / 1760)},
        "mi": {"mm": 1.609e6, "cm": 1.609e5, "m": 1609, "km": 1.609, "in": 63360, "ft": 5280, "yd": 1760}
    },

    "Time": {
        "ms": {"s": 0.001, "min": (1 / 60000), "h": (1 / 3.6e6)},
        "s": {"ms": 1000, "min": (1 / 60), "h": (1 / 3600)},
        "min": {"ms": 60000, "s": 60, "h": (1 / 60)},
        "h": {"ms": 3.6e6, "s": 3600, "min": 60}
    }
}

fullNames = {
    "lbs": "pounds",
    "oz": "ounces",
    "mg": "milligrams",
    "g": "grams",
    "kg": "kilograms",
    "s": "seconds",
    "ms": "milliseconds",
    "min": "minutes",
    "h": "hours",
    "m": "meters",
    "km": "kilometers",
    "mm": "millimeters",
    "cm": "centimeters",
    "in": "inches",
    "ft": "feet",
    "yd": "yards",
    "mi": "miles"
}

abbrevNames = {
    "pounds": "lbs",
    "ounces": "oz",
    "milligrams": "mg",
    "grams": "g",
    "kilograms": "kg",
    "seconds": "s",
    "milliseconds": "ms",
    "minutes": "min",
    "hours": "h",
    "meters": "m",
    "kilometers": "km",
    "millimeters": "mm",
    "centimeters": "cm",
    "inches": "in",
    "feet": "ft",
    "yards": "yd",
    "miles": "mi"
}

windowWidth, windowHeight = 500, 350

# Dynamic
unitOptions = []
for unitType, _ in units.items():
    unitOptions.append(unitType)

currentUnitType = unitOptions[0]

# Background and root
customtkinter.set_appearance_mode("dark"); customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry(str(windowWidth) + "x" + str(windowHeight))
root.title("Unit")

mainFrame = customtkinter.CTkFrame(master = root)
mainFrame.pack(pady = 5, padx = 5, fill = "both", expand = True)

headerLabel = customtkinter.CTkLabel(
    master = mainFrame, 
    text = "Unit Converter", 
    font = customtkinter.CTkFont(family = "Roboto", size = 24, weight = "bold")
)
headerLabel.place(relx = .5, rely = .125, anchor = customtkinter.CENTER)

# Unit needed to convert
oldUnitOptions = customtkinter.CTkOptionMenu(master = root)
oldUnitOptions.place(relx = .3, rely = .6, anchor = customtkinter.CENTER)

oldUnitQuantityBox = customtkinter.CTkEntry(
    master = root,
    placeholder_text = "Enter an amount"
)
oldUnitQuantityBox.place(relx = .3, rely = .5, anchor = customtkinter.CENTER)

# Unit after conversion
newUnitOptions = customtkinter.CTkOptionMenu(master = root)
newUnitOptions.place(relx = .7, rely = .6, anchor = customtkinter.CENTER)

newUnitQuantityBox = customtkinter.CTkEntry(
    master = root,
    state = "disabled",
    placeholder_text = "Enter an amount"
)
newUnitQuantityBox.place(relx = .7, rely = .5, anchor = customtkinter.CENTER)

# Conversion Button
unitTypeOptions = customtkinter.CTkOptionMenu(
    master = root,
    values = unitOptions
)
unitTypeOptions.place(relx = .5, rely = .25, anchor = customtkinter.CENTER)
unitTypeOptions.set(currentUnitType)

convertButton = customtkinter.CTkButton(
    master = root,
    text = "Convert",
    font = customtkinter.CTkFont(family = "Robot", size = 14)
)
convertButton.place(relx = .5, rely = .9, anchor = customtkinter.CENTER)

equalsLabel = customtkinter.CTkLabel(
    master = mainFrame,
    text = "=",
    font = customtkinter.CTkFont(family = "Robot", size = 24)
)
equalsLabel.place(relx = .5, rely = .5, anchor = customtkinter.CENTER)

def swapUnitType(newUnit):
    global currentUnitType
    currentUnitType = newUnit

    unitOptions = []

    for unitAbbrev, _ in units[newUnit].items():
        unitOptions.append(fullNames[unitAbbrev])
    
    oldUnitOptions.configure(values = unitOptions)
    oldUnitOptions.set(unitOptions[0])
    newUnitOptions.configure(values = unitOptions)
    newUnitOptions.set(unitOptions[0])

swapUnitType(currentUnitType)
unitTypeOptions.configure(command = swapUnitType)

def convertUnit():
    oldQuantity = oldUnitQuantityBox.get()
    oldQuantityUnit = oldUnitOptions.get()
    newQuantityUnit = newUnitOptions.get()

    if oldQuantityUnit == newQuantityUnit:
        newUnitQuantityBox.configure(textvariable = customtkinter.StringVar(
            master = newUnitQuantityBox, 
            value = oldQuantity
        ))

        return None
    
    newQuantityVariable = units[currentUnitType][abbrevNames[oldQuantityUnit]][abbrevNames[newQuantityUnit]]
    convertedQuantity = float(oldQuantity) * newQuantityVariable

    newUnitQuantityBox.configure(textvariable = customtkinter.StringVar(
        master = newUnitQuantityBox, 
        value = str(convertedQuantity)
    ))

convertButton.configure(command = convertUnit)

root.mainloop()
