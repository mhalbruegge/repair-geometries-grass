import argparse

from .func import repair_geometries


def main():
    """
    Main function to parse arguments and handle errors.
    """
    parser = argparse.ArgumentParser(description="Clean geometries using GRASS GIS")
    parser.add_argument("--input_shp", required=True, help="The input shapefile")
    parser.add_argument("--output_shp", required=True, help="The output shapefile")
    parser.add_argument(
        "--crs", required=True, help="The Coordinate Reference System (CRS)"
    )

    args = parser.parse_args()

    try:
        repair_geometries(args.input_shp, args.output_shp, args.crs)
    except Exception as e:
        print(f"Error while repairing geometries: {e}")
