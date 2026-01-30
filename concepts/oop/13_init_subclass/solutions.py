# __init_subclass__ Exercises Solutions

class Registry:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

class SubClass1(Registry):
    pass

class SubClass2(Registry):
    pass

# Test
print(Registry.subclasses)  # [<class '__main__.SubClass1'>, <class '__main__.SubClass2'>]