# franci14_Wifi_PointsInsertCursor_script.py
# Jacob S. Francis
# GEO 443 Python Programming
# This script creates a new file geodatabase and associated fields, which we will populate using the InsertCursor from txt file data
# 04/22/2026

#######################################
# ---- TOOL SYNTAX IN THE SCRIPT ---- #
# INSERT CURSOR
# - InsertCursor (in_table, field_names, {datum_transformation}, {explicit}, {load_only})
# CREATE FILE GDB
# - arcpy.management.CreateFileGDB(out_folder_path, out_name, {out_version})
# CREATE POINT FEATURE CLASS
# - arcpy.management.CreateFeatureclass(out_path, out_name, {geometry_type}, {template}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3}, {out_alias}, {oid_type})
# ADD FIELD
# - arcpy.management.AddField(in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
# ---- TOOL SYNTAX IN THE SCRIPT ---- #
#-------------------------------------#

#######################################
# ---- STEPS ---- #
# 1.) Create a try/except block
# 2.) Import arcpy and sys
# 3.) Turn on overwriteOutput
# 4.) Set the workspace
# 5.) Create a new file GDB for the data
# 6.) Update the workspace to be this new file geodatabase
# 7.) Create point feature class within the file GDB with the GCS_WGS84 (WKID: 4326) as the spatial reference
# 8.) Add fields to the new feature class from the text file
# 9.) Open the text file and use read lines to create a list of all the lines in the text file
# 10.) Use InsertCursor to create point geometry and populate new fields in the feature class
# 11.) Turn off overwriteOutput
# 12.) Close with additional exception statement for informative error messages
# ---- STEPS ---- #
#######################################

# 1.) Create a try/except block
try:
    # 2.) Import arcpy and sys
    import arcpy
    import sys

    # 3.) Turn on overwriteOutput
    arcpy.env.overwriteOutput = True

    # 4.) Set the workspace
    arcpy.env.workspace = r"C:\\francis_jake\\GEO_443\\Module_16"

    # 5.) Create a new file GDB for the data
    # first use arcpy.Exists to check if the geodatabase has already been created
    # else - create the file GDB
    if arcpy.Exists("WifiHotspots.gdb"):
        print("\nThe WifiHotspots.gdb already exists, the script will now continue...")
    else:
        arcpy.management.CreateFileGDB(arcpy.env.workspace, "WifiHotspots.gdb")

    # 6.) Update the workspace to be this new file geodatabase
    # updating the workspace to include the newly created GDB using concatenation with the / in the file path
    arcpy.env.workspace = arcpy.env.workspace + "/WifiHotspots.gdb"
    print("\nThe workspace has been updated to host a new geodatabase, which can be found here: ", arcpy.env.workspace)

    # 7.) Create point feature class within the file GDB with the GCS_WGS84 (WKID: 4326) as the spatial reference
    print("\nA new feature class is now being created in the geodatabase...")
    # use arcpy.Exists again to check for this feature class, delete it if it already exists for a smooth program
    if arcpy.Exists("WIFIHotspots"):
        arcpy.management.Delete("WIFIHotspots")
        print("\nThis feature class already exists in the workspace and will now be deleted...")
    spatial_ref = arcpy.SpatialReference(4326)
    arcpy.management.CreateFeatureclass(arcpy.env.workspace, "WIFIHotspots", "POINT", "", "", "", spatial_ref)
    print("")
    print(arcpy.GetMessages())
    print("")

    # 8.) Add fields to the new feature class from the text file
    # Adding a new field in the GDB for each column in the text file
    arcpy.management.AddField("WIFIHotspots", "HotspotName", "TEXT", "", "", 225)
    print(arcpy.GetMessages())
    print("")
    arcpy.management.AddField("WIFIHotspots", "HotspotType", "TEXT", "", "", 225)
    print(arcpy.GetMessages())
    print("")

    # 9.) Open the text file and use readlines to create a list of all the lines in the text
    # a with block closes the text file automatically once the lines are read
    with open(r"C:\\francis_jake\\GEO_443\\Module_16\\wifi_hotspots_nyc.txt", "r") as open_text:
        # variable for each line in the text
        lst_hotspots_text = open_text.readlines()
    for hotspot in lst_hotspots_text:
        print(hotspot)

    # 10.) Use InsertCursor to create point geometry and populate new fields in the feature class
    # The SHAPE@XY gives access to just the XY coordinates
    with arcpy.da.InsertCursor("WIFIHotspots", ["SHAPE@XY", "HotspotName", "HotspotType"]) as cursor:
        # using the feature class as the input table to populate all the fields that were created with XY point coordinates
        counter = 1
        for hotspot in lst_hotspots_text:
            print("\nNow adding the record number ", str(counter) + " to the feature class")
            if "lat" in hotspot:
                continue  # if the program sees "lat" in the text row of record 1, it will continue
            vals = hotspot.split(",")  # use split to designate the records by an indexed list in the text
            latitude = float(vals[0])  # [0] is index position one (lat)
            print(latitude)
            longitude = float(vals[1])
            print(longitude)
            hotspot_name = str(vals[2])
            print(hotspot_name)
            hotspot_type = str(vals[3])
            print(hotspot_type)
            row_value = [(longitude, latitude), hotspot_name, hotspot_type]
            print(row_value)
            # this is the tuple list which will be populated into the new feature class fields
            cursor.insertRow(row_value)
            print("\nRecord Number " + str(counter) + " written to feature class\n")
            # this inserts the cursor into the current row and populates it with the tuple in row_value
            # add a new counter for the next loop
            counter = counter + 1
    print("\nGo to " + arcpy.env.workspace + " to see the resulting dataset")

    # 11.) Turn off overwriteOutput
    arcpy.env.overwriteOutput = False

# 12.) Close with additional exception statement for informative error messages
except Exception as e:
    print("The error in your script is: ", e)
    print("")
    print(arcpy.GetMessages())
