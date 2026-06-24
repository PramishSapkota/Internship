class Animal:
    sound = "Make sound"

    @classmethod
    def change_sound(cls,new_sound):
        cls.sound = new_sound

a1 = Animal()
a2 = Animal()

a1.change_sound(1)
print(a2.sound)