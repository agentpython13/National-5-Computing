#cones

radius = 0.0
height = 0.0
volume = 0.0

def getConeDimensions():
    global radius, height, volume
    radius = float(input("Enter radius:"))
    height = float(input("Enter height:"))

def calculateConeVolume():
    global radius, volume, height
    volume = (radius ** 2 * 3.14 * height) / 3

def displayConeVolume():
    global volume
    print("The volume of the cone is", round(volume, 2), "cm cubed")
    
getConeDimensions()
calculateConeVolume()
displayConeVolume()
