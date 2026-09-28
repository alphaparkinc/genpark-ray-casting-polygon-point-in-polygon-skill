# Point-in-Polygon & Shoelace Engine Skill

Robust Jordan curve ray-casting and Shoelace cross-product formulation for polygon containment and geometrical properties.

```mermaid
flowchart LR
    Point["Test Point (x, y)"] --> Ray["Cast Horizontal Semi-Infinite Ray"]
    Polygon["Polygon Boundary Edges"] --> Ray
    Ray --> Intersections["Count Edge Intersections"]
    Intersections --> OddEven{"Odd Intersections?"}
    OddEven -- Yes --> Inside["Point is INSIDE"]
    OddEven -- No --> Outside["Point is OUTSIDE"]
```

## Features
- **100% Python Standard Library**: Pure analytical geometric intersection.
- **Shoelace Formula**: Area and center of mass in \(O(n)\) time.
