class parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passion pro")


class child(parent):
    def phone(self):
        print("iphone")
    def bike(self):
        print("duke")

ch=child()
ch.phone()
ch.bike()