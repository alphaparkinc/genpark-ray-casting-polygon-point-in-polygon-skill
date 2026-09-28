"""Ray Casting Point-in-Polygon & Shoelace Area Engine.
100% Python Standard Library.
"""

class PolygonSpatial:
    @staticmethod
    def point_in_polygon(point, polygon):
        x, y = point
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    @staticmethod
    def polygon_area_and_centroid(polygon):
        n = len(polygon)
        area = 0.0
        cx = 0.0
        cy = 0.0
        for i in range(n):
            x0, y0 = polygon[i]
            x1, y1 = polygon[(i + 1) % n]
            cross = (x0 * y1 - x1 * y0)
            area += cross
            cx += (x0 + x1) * cross
            cy += (y0 + y1) * cross
            
        area *= 0.5
        if abs(area) < 1e-9:
            return 0.0, (0.0, 0.0)
        cx /= (6.0 * area)
        cy /= (6.0 * area)
        return abs(round(area, 4)), (round(cx, 4), round(cy, 4))
