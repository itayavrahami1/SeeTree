import pandas as pd
import Scripts.Service.polygon as polygon_service

def query(file_name):
    global image_data
    # image_data only from one file for now. later will be an array

    base_url = "C:\\Users\\itay.a\\Coding\\SeeTree\\inventory\\data\\image\\"
    url = base_url + file_name
    data = pd.read_csv(url,header=None)
    data.columns = ['ImageName', 'latitude', 'longitude', 'Z(High)', 'yaw', 'pitch', 'roll']
    image_data = data


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
    polygon = polygon_service.get_polygon_by_name(polygon_name)
    print(polygon)

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
