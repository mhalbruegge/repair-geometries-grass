import os
import tempfile

from grass_session import Session
from grass.script import core as gcore


def validate_shapefile(file_path):
    """
    Validate if the filename ends with .shp.
    """
    if not file_path.endswith(".shp"):
        raise ValueError(f"Invalid shapefile path: {file_path}")
    return file_path


def repair_geometries(input_shp, output_shp, crs):
    """
    Clean geometries using GRASS GIS.
    """
    validate_shapefile(input_shp)
    validate_shapefile(output_shp)

    with tempfile.TemporaryDirectory() as gisdb:
        location = "grass_location"
        output_vect = "output_vect"
        output_clean_vect = "output_clean_vect"

        with Session(gisdb=gisdb, location=location, create_opts=crs):
            if not os.path.isfile(input_shp):
                raise ValueError(f"Invalid input shapefile: {input_shp}")
            gcore.parse_command("v.in.ogr", input=input_shp, output=output_vect)
            # Perform cleaning
            gcore.parse_command(
                "v.clean",
                input=output_vect,
                output=output_clean_vect,
                tool="break,rmdupl",
            )
            gcore.parse_command(
                "v.out.ogr",
                input=output_clean_vect,
                output=output_shp,
                format="ESRI_Shapefile",
                overwrite=True,
            )
