
class Person:

    def __init__(self, name, gender, eyeColor, height, weight ):
        self.__name = name
        self.__gender = gender
        self.__eyeColor = eyeColor
        self.__height = height
        self.__weight = weight


    def __str__(self):
        return f"Name: {self.__name}\
            Gender: {self.__gender}\
            Eye Color: {self.__eyeColor}\
            Height: {self.__height}\
            Weight: {self.__weight}"