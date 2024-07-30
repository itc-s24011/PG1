class Sample:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1
        self.__d_ = 1
        self.__e__ = 1

        def show_attribute(self):
            a = self.a
            b = self._b
            c = self.__c
            d = self.__d_
            e = self.__e__
            print("a: {}, b: {}, c: {}, d: {}, e: {}".format(a,b,c,d,e))

s = Sample()
print(s.show_attribute())

s.a

s._b

s.__c

s.a = 2
s._b = 2
s.__c = 2
s.__d_ = 2
s.__e__ = 2
s.a, s._b, s.__c, s.__d_, s.__e__
