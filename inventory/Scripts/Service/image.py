import pandas as pd

class Image:

    def __init__(self):
        self.data = []

    def query(self,file_name):
        base_url = "C:\\Users\\itay.a\\Coding\\SeeTree\\inventory\\data\\image\\"
        url = base_url + file_name
        self.data = pd.read_csv(url)
        self.data.columns = ['ImageName','latitude','longitude','Z(High)','yaw','pitch','roll']
        return self.data

    def __str__(self):
        return f'num of images is {len(self.data)}'
