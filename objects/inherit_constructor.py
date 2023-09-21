import math

def make(cls, *args):
    return cls["_new"](*args)

def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }

def shape_density(thing, weight):
    return weight / call(thing, "area")

Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": None,
    "_new": shape_new
}

def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square
    }

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square",
    "_parent": Shape,
    "_new": square_new
}

def circle_new(name, radius):
    return make(Shape, name) | {
        "radius": radius,
        "_class": Circle
    }

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "_classname": "Circle",
    "_parent": Shape,
    "_new": circle_new
}

def call(thing, method_name, *args):
    method = find(thing["_class"], method_name)
    return method(thing, *args)

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError("method_name")

examples = [make(Square, "sq", 3), make(Circle, "ci", 2)]
for ex in examples:
    n = ex["name"]
    d = call(ex, "density", 5)
    print(f"{n} {d:.2f}")
