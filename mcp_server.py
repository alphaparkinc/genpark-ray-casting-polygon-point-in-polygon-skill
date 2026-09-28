"""MCP stdio server for Polygon Spatial Engine."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PolygonSpatial

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "check_point_in_polygon",
                        "description": "Test if point (x, y) is inside 2D polygon vertices via ray casting",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "point": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
                                "polygon": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2}
                                }
                            },
                            "required": ["point", "polygon"]
                        }
                    },
                    {
                        "name": "compute_polygon_metrics",
                        "description": "Compute polygon signed area and centroid via Shoelace formula",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "polygon": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2}
                                }
                            },
                            "required": ["polygon"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "check_point_in_polygon":
            pt = tuple(args.get("point"))
            poly = [tuple(v) for v in args.get("polygon", [])]
            res = PolygonSpatial.point_in_polygon(pt, poly)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"is_inside": res}}
        elif name == "compute_polygon_metrics":
            poly = [tuple(v) for v in args.get("polygon", [])]
            area, centroid = PolygonSpatial.polygon_area_and_centroid(poly)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"area": area, "centroid": centroid}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
