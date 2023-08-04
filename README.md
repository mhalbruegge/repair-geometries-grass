# repair-geometries-grass

Repair Geometries GRASS is a simple, easy-to-use wrapper for GRASS GIS, designed to facilitate the repair of geometries in a shapefile.

## Prerequisites

Before you can use Repair Geometries GRASS, please make sure you have fulfilled the following requirements:

- Python and GRASS GIS are installed. If not, please follow their official installation guides.
- You have set your GRASSBIN and PROJ_LIB environment variables appropriately.

For instance:

```bash
$ export GRASSBIN=/usr/bin/grass
$ export PROJ_LIB=/usr/share/proj
```

## Installation and Running

To install and run Repair Geometries GRASS, use the following command:

```bash
$ python3 repair_geometries.py --input_shp <input_shapefile> --output_shp <output_shapefile> --crs <coordinate_reference_system>
```

In this command:

- Replace <input_shapefile> with the path to your input shapefile.
- Replace <output_shapefile> with the desired output path.
- Replace <coordinate_reference_system> with the appropriate CRS (for example, EPSG:25832).

## Usage in Python Projects

Once you have the Repair Geometries GRASS installed, you can use it inside your python project by following these steps:

```python
from repair_geometries_grass import repair_geometries

repair_geometries("path_to_input.shp", "path_to_output.shp", crs="EPSG:25832")
```

Remember to replace "path_to_input.shp" with the path to your input shapefile, "path_to_output.shp" with the desired output path and crs with the appropriate CRS (for example, EPSG:25832).
