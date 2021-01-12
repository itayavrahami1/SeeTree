import json

class Polygon:

    def __init__(self):
        self.data = {}

    def query(self,file_name):
        base_url = "C:\\Users\\itay.a\\Coding\\SeeTree\\inventory\\data\\"
        url = base_url + file_name
        polygon_data = open(url)
        self.data = json.load(polygon_data)
        polygon_data.close()

    # def get_polygon(self,image_name):

    def __str__(self):
        return self.data


