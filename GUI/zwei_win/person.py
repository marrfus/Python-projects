
class Person:

    def __init__(self, name, gender, eyeColor, height, weight ):
        self.__name = name
        self.__gender = gender
        self.__eyeColor = eyeColor
        self.__height = height
        self.__weight = weight


    def __str__(self):
        return (
        f"Name: {self.__name}\n"
        f"Gender: {self.__gender}\n"
        f"Eye Color: {self.__eyeColor}\n"
        f"Height: {self.__height} cm\n"
        f"Weight: {self.__weight} kg"
    )