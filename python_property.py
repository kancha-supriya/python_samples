class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def show_title(self):
        print("Listening to {} and {}".format(self.title, self.artist))

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title.upper()

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist + ' test'

    title = property(get_title, set_title)
    artist = property(get_artist, set_artist)

# Teddy_Bear = Song('Teddy Bear', 'supriya')
# Teddy_Bear.artist = 'amruta'
# Teddy_Bear.show_title()
# print(Teddy_Bear.artist)
# Teddy_Bear = Song('Teddy Bear', 'supriya')
# Teddy_Bear.show_title()
# print(Teddy_Bear.artist)


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def email(self):
        return "{}-{}@gmail.com".format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None


# emp = Employee("supriya", "kanchan")
# emp.fullname = 'Urvi Gala'
# emp.fullname = 'Amruta Nevrekar'
# print(emp.email)
# del emp.fullname
# print(emp.email)


class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def email_getter(self):
        return "{}.{}@gmail.com".format(self.firstname, self.lastname)

    def email_setter(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    property(email_getter,email_setter)
    # lastname=property(email_getter,email_setter)

s = Student('Urvi', 'Gala')
print(s.firstname)
# print(s.email)
# s.email = 'amruta neverekar'
# print(s.email)
