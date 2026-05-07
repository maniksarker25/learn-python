# singleton => one single instnace
# if you want a new instnace , you will get the old one (already created) instance

class Singleton:
    __intance = None
    def __init__(self):
        if Singleton.__intance is None:
           Singleton.__intance = self
        else:
            raise Exception("This is singleton. Already have an instnace , use that on by calling get_instance method")
    @staticmethod
    def get_instnace():
        if Singleton.__intance is None:
            Singleton()
        return Singleton.__intance

first = Singleton.get_instnace()
print(first)
second  = Singleton.get_instnace()
print(second)


#
# last = Singleton() throw exception
