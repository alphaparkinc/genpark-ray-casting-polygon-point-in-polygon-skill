"""Example checking point in polygon."""
from client import PolygonSpatial

def main():
    poly = [(0, 0), (10, 0), (10, 10), (0, 10)]
    pt_inside = (5, 5)
    pt_outside = (15, 5)
    print("Is (5, 5) inside:", PolygonSpatial.point_in_polygon(pt_inside, poly))
    print("Is (15, 5) inside:", PolygonSpatial.point_in_polygon(pt_outside, poly))
    area, centroid = PolygonSpatial.polygon_area_and_centroid(poly)
    print(f"Area: {area}, Centroid: {centroid}")

if __name__ == "__main__":
    main()
