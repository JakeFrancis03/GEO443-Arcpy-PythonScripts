# GEO 443 – Python Programming Scripts

Python scripts written by **Jacob S. Francis** for GEO 443 – Python Programming at Miami University (Spring 2026). They range from ArcPy geoprocessing workflows to Python fundamentals.

## ArcPy / Geoprocessing

| Script | Description |
|---|---|
| `franci14_OxfordQueryScript.py` | **Attribute and Spatial Selection – Oxford, OH.** Selects residential buildings from Ohio LBRS address data by attribute, narrows the selection to buildings within the Oxford city limits after checking that both datasets share a spatial reference, and exports the result to a new shapefile. |
| `franci14_Wifi_PointsInsertCursor_script.py` | **Insert Cursor Data Appending – NYC Wi-Fi Hotspots.** Creates a file geodatabase and point feature class (WGS 84), then uses an `InsertCursor` to build point geometry and attributes from a text file. |
| `franci14_GPArcPy_Assignment.py` | **Buffer and Clip Spatial Analysis – Grand River, OH.** Buffers the Grand River by 300 m, clips Lake County land cover to the buffer, and summarizes land-use area by type with Summary Statistics. |
| `franci14_Buffer_Clip_ToolChain.py` | **Buffer and Clip Tool Chain.** Buffers parks by 500 ft and clips the hospitals that fall within that buffer. |

## Python Fundamentals

| Script | Description |
|---|---|
| `input_little_calculator.py` | Takes user input and returns the square of each number, demonstrating two methods of integer conversion. |
| `franci14_TeamCheer.py` | Uses a `for` loop and string methods to spell out a cheer for the user's favorite team. |
| `franci14_MyDoublesGameFunctions.py` | Uses user-defined functions with return values to play a number-doubling game. |

## Requirements

The geoprocessing scripts require **ArcGIS Pro** and its bundled `arcpy` package. Workspace paths point to local course data folders and must be updated to run on another machine. The fundamentals scripts run with standard Python 3.

## Portfolio

More GIS and planning work: [Portfolio link – add once the new site is live]
