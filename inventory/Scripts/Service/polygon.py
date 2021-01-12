import json
import Scripts.Service.image as image_service
from shapely.geometry import Point
from shapely.geometry import Polygon as ShapelyPoly

def query(file_name):
    global polygon_data

    base_url = "C:\\Users\\itay.a\\Coding\\SeeTree\\inventory\\data\\"
    url = base_url + file_name
    polygon_data = open(url)
    data = json.load(polygon_data)
    polygon_data.close()
    polygon_data = data['features']

def get_polygon_by_name(polygon_name):
    polygon_name = polygon_name

    def _compare_polygon_name(polygon):
        print(polygon_name)
        return polygon_name == polygon.properties.index

    polygon = filter(_compare_polygon_name,polygon_data)



def get_polygon(image_name):
    # getting Image object by name and then extract coords
    img = image_service.get_image_by_name(image_name)
    coords = Point(img.longitude[0], img.latitude[0])

    for i in range(len(polygon_data)):
        # extracting polygon coords from json
        polygon_coords = polygon_data[i]['geometry']['coordinates'][0]
        poly = ShapelyPoly(polygon_coords)

        if coords.within(poly):
            print('IN', i)
            return polygon_data[i]['properties']



class Polygon:

    def __init__(self,coordinates = {} ,properties = {}):
        self.coordinates = coordinates
        self.properties = properties

    def __str__(self):
        return self.properties


