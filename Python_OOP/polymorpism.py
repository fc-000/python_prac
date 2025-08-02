class Polygon: # superclass
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon): # subclass
    # renders Sqaure
    def render(self):
        print("Rendering Square...")
    
class Circle(Polygon): # subclassP
    # renders circle
    def render(self):
        print("Rendering Circle...")

#create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()