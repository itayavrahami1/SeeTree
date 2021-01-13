import Scripts.Service.polygon as polygon_service
import Scripts.Service.image as image_service
from Scripts.Service.image import Image
from Scripts.Service.polygon import Polygon

if __name__ == "__main__":

    polygon_service.query("polygons_metadata.geojson")
    image_service.query()

    # poly_props = polygon_service.get_polygon('1_DSC08110.JPG')

    print(image_service.get_images("1/304"))


