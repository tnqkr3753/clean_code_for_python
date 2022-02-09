def annotation_function(x:int, y:int, z:int) -> int:
    print(x + y + z)
    return x+z

print(annotation_function.__annotations__)



class AnnotationClass():
    x : str
    y : int
    z : dict

print(AnnotationClass.__annotations__)