
class Pet:
            
            def __init__(self, options):
                self._name = options

            def set_name(self, new_name):
                self._name = new_name

            def get_name(self):
                return self._name

            def get_animal_type(self):
                return self._animal_type

            def get_age(self):
                return self._age
