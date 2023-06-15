class Mammals:
    def feed(self):
        print('feeding young')

class Giraffes(Mammals):
    def trees(self):
        print('eating leaves')

reginald=Giraffes()
harold=Giraffes()
reginald.feed()
