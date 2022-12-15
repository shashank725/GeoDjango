from shapely.geometry import Polygon

polygon1 = Polygon([(30, 10), (40, 40), (20, 35), (10, 20), (30, 10)])
print(f"Polygon area: {polygon1.area}, polygon length: {polygon1.length}") 

polygon1