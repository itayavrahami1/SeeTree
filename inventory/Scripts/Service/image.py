import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib
import Scripts.Service.polygon as polygon_service
from shapely.geometry import Point
from shapely.geometry import Polygon as ShapelyPoly

def query():
    global image_data
    image_data = pd.DataFrame()
    file_num = 1

    while True:
        file_name = f'Images_metadata_{file_num}.csv'
        base_url = "C:\\Users\\itay.a\\Coding\\SeeTree\\inventory\\data\\image\\"
        url = base_url + file_name
        try:
            data = pd.read_csv(url,header=None)
            if len(image_data) == 0:
                image_data = data
            else:
                image_data = pd.concat([image_data,data])
            file_num += 1
        except:
            break

    image_data.columns = ['ImageName', 'latitude', 'longitude', 'Z(High)', 'yaw', 'pitch', 'roll']


def get_image_by_name(image_name):
    """
    :param image_name:
    :return: Image object
    for the use of polygon service get_polygon which recieves image_name and uses image_coords
    """
    img = image_data[image_data['ImageName'] == image_name].values[0]
    img = Image(img[0], img[1], img[2], img[3], img[4], img[5], img[6])

    return img

def get_images(polygon_name):
    """
    :param polygon_name:
    :return: imgage_name list of images inside the polygon
    first getting the polygon by the polygon_name (index)
    """
    matplotlib.interactive(True)
    images = []
    polygon = polygon_service.get_polygon_by_name(polygon_name)
    poly = ShapelyPoly(polygon.coordinates[0])
    print(type(np.array(image_data['longitude'])))
    x,y = zip(*polygon.coordinates[0])

    plt.figure()
    plt.scatter(x,y)
    # plt.axis((-21.98,-21.90),(-48.540,-48.5))
    plt.xlim([-48.540,-48.5])
    plt.ylim([-21.98,-21.90])


    # plt.figure()
    plt.scatter(image_data['longitude'],image_data['latitude'], c='red')
    plt.savefig('plot')

    # polygon_coords = [(-60, -25), (-60, 0), (60, 0), (60, -25)]
    # poly = ShapelyPoly(polygon_coords)
    for i in range(len(image_data)):

        image = image_data.iloc[i]
        point = Point(image['longitude'],image['latitude'])
        point1 = Point(-48.524806,-21.92413)

        if point.within(poly):
            images.append(image['ImageName'])


    return images




class Image:

    def __init__(self,ImageName, latitude, longitude, Z_High , yaw, pitch, roll):
        self.ImageName = ImageName
        self.latitude = latitude,
        self.longitude = longitude,
        self.Z_High = Z_High,
        self.yaw = yaw,
        self.pitch = pitch,
        self.roll = roll

    def __str__(self):
        return f'num of images is {len(self.latitude)}'
