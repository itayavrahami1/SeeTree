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

    return polygon_data

def get_polygon_by_name(polygon_name):
    """
    :param polygon_name - the index of the polygon
    :return: polygon full data
    """
    polygon_name = polygon_name

    def _compare_polygon_name(polygon):
        return polygon_name == polygon['properties']['index']

    polygon = list(filter(_compare_polygon_name,polygon_data))[0]
    polygon = Polygon(polygon['geometry']['coordinates'],polygon['properties'])
    return polygon



def get_polygon(image_name):
    """
    :param image_name:
    :return: the properties of the polygon contains the image.
    """
    # getting Image object by name and then extract coords
    img = image_service.get_image_by_name(image_name)
    coords = Point(img.longitude[0], img.latitude[0])

    for i in range(len(polygon_data)):
        # extracting polygon coords from json
        polygon_coords = polygon_data[i]['geometry']['coordinates'][0]

        poly = ShapelyPoly(polygon_coords)
        if coords.within(poly):
            return polygon_data[i]['properties']

def get_all_polygon(image_data):
    polygons_idx = []


    for curr_polygon in polygon_data:
        poly = ShapelyPoly(curr_polygon['geometry']['coordinates'][0])

        for i in range(len(image_data)):
            image = image_data.iloc[i]
            point = Point(image['longitude'], image['latitude'])

            if point.within(poly):
                polygons_idx.append(curr_polygon['properties']['index'])
                break

    return polygons_idx



class Polygon:

    def __init__(self,coordinates,properties):
        self.coordinates = coordinates
        self.properties = properties

    def __str__(self):
        return self.properties['index']



