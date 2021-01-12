
from Scripts.Service.image import Image
from Scripts.Service.polygon import Polygon

if __name__ == "__main__":
    polygon1 = Polygon()
    polygon1.query("polygons_metadata.geojson")

    img1 = Image()
    img1.query("Images_metadata_1.csv")

    raw = polygon1.data['features'][0]['geometry']

    print(raw)