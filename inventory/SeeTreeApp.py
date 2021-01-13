import Scripts.Service.polygon as polygon_service
import Scripts.Service.image as image_service
from Scripts.Service.image import Image
from Scripts.Service.polygon import Polygon

if __name__ == "__main__":
    polygon_data = polygon_service.query("polygons_metadata.geojson")
    image_data = image_service.query()

    polygon_idx = "1/304"
    image_name = '1_DSC02477.JPG'

    poly_props = polygon_service.get_polygon(image_name)
    print(f'The image - "{image_name}" is in polygon: ', poly_props)
    images = image_service.get_images(polygon_idx)
    print(f'Polygon {polygon_idx} contains {len(images)} images: \n ', images)

    polygons = polygon_service.get_all_polygon(image_data)
    print(polygons, len(polygons))


