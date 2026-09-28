# franci14_OxfordQueryScript.py
# Jacob S. Francis
# GEO 443 Python Programming
# This script will run an Attribute and Location Selection
# The attribute selection will select all of the residential buildings in the LBRS dataset
# The location selection will select all of the residential buildings in the Oxford Limits
# 04/13/2026

# ----- #
# STEPS
# ----- #
# 1.) Create a try/except block for the bulk of the script
# 2.) Import arcpy and sys module
# 3.) Turn on overwriteOutput
# 4.) Set the workspace
# 5.) Determine the Attribute query needed
# 6.) Use MakeFeatureLayer to create the In-Memory layer to be used for the input layer(dataset to be selected)
# 7.) Place the SQL query into a variable
# 8.) Use SelectLayerByAttribute to select all of the residential buildings in the LBRS dataset
# 9.) Print out the number of selected records using GetCount()
# 10.) Check the spatial reference of the datasets being used in the location selection (use sys.exit to quit script if different)
# 11.) Use SelectByLocation to select all of the residential buildings within the Oxford limits
# 12.) Print out the number of selected records using GetCount()
# 13.) Use CopyFeature to copy the selected records to a new dataset
# 14.) Delete the In-Memory layer
# 15.) Turn off overwriteOutput
# ----- #
# STEPS
# ----- #

# -------------------- #
# TOOL SYNTAX IN SCRIPT
# -------------------- #
# MakeFeatureLayer tool:
# - arcpy.management.MakeFeatureLayer(in_features, out_layer, {where_clause}, {workspace}, {field_info})
# SelectLayerByAttribute tool:
# - arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
# SelectLayerByLocation tool:
# - arcpy.management.SelectLayerByLocation(in_layer, {overlap_type}, {select_features}, {search_distance}, {selection_type}, {invert_spatial_relationship})
# GetCount() tool:
# - arcpy.management.GetCount(in_rows)
# CopyFeatures tool:
# - arcpy.management.CopyFeatures(in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
# -------------------- #
# TOOL SYNTAX IN SCRIPT
# -------------------- #

# 1.) Create a try/except block for the bulk of the script
try:
    # 2.) Import arcpy and sys module
    # sys.exit used to exit the program if spatial references are different in the location selection
    import arcpy
    import sys

    # 3.) Turn on overwriteOutput
    arcpy.env.overwriteOutput = True

    # 4.) Set the workspace
    arcpy.env.workspace = r"C:\\francis_jake\\GEO_443\\module_15\\CityofOxford_SpatialSelection_AttributeLocation\\data\OxfordQueryData"
    print("\nThe workspace has been set to: ", arcpy.env.workspace)
    print("\nThe data in this folder is: ")
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList:
        print(fc)

    # 5.) Determine the Attribute query needed
    # "COMMENT_" = '' NULL records = residential buildings in the comments field
    # "NEW_SELECTION" for the selection type

    # 6.) Use MakeFeatureLayer to create the In-Memory layer to be used for the input layer(dataset to be selected)
    residential_bldng_lyr = arcpy.management.MakeFeatureLayer("LBRSaddresses.shp", "residential_bldng_lyr")

    # 7.) Place the SQL query into a variable
    qry = """ "Comment_" = '' """

    # 8.) Use SelectLayerByAttribute to select all of the LBRS residential buildings
    print("\nThe Attribute Selection will now run to select all Residential Buildings...")
    print("")
    arcpy.management.SelectLayerByAttribute(residential_bldng_lyr, "NEW_SELECTION", qry)
    print(arcpy.GetMessages())

    # 9.) Print out the number of selected records using GetCount()
    cnt = arcpy.management.GetCount("residential_bldng_lyr")
    print("\nThe number of LBRS Residential Buildings in this dataset is: ", str(cnt))

    # 10.) Check the spatial reference of the datasets being used in the location selection (use sys.exit to quit script if different)
    print("\nNow checking the spatial reference of the datasets to be used in the SelectByLocation for all Residential Buildings in the Oxford City Limits...")
    print("")
    desc_residential_buildings = arcpy.Describe("LBRSaddresses.shp")
    spatial_ref_residential_buildings = desc_residential_buildings.SpatialReference
    print("The Spatial reference of the LBRSaddresses.shp (Residential Buildings) is: " + spatial_ref_residential_buildings.name)
    desc_oxford_limits = arcpy.Describe("oxford_city_limits.shp")
    spatial_ref_oxford_limits = desc_oxford_limits.SpatialReference
    print("The spatial reference of the oxford_limits.shp is: " + spatial_ref_oxford_limits.name)
    if spatial_ref_residential_buildings.name == spatial_ref_oxford_limits.name:
        print("\nThe data in the dataset is in the same spatial reference, selection proceeding...")
    else:
        sys.exit("Please ensure all datasets in the selection are in the same spatial reference. PROGRAM ENDING")

    # 11.) Use SelectByLocation to select all of the residential buildings within the Oxford city limits
    print("\nThe Location Selection will now run to select all residential buildings within the Oxford city limits...")
    print("")
    arcpy.management.SelectLayerByLocation(residential_bldng_lyr, "WITHIN", "oxford_city_limits.shp", "", "SUBSET_SELECTION")
    print(arcpy.GetMessages())

    # 12.) Print out the number of selected records using GetCount()
    cnt = arcpy.management.GetCount("residential_bldng_lyr")
    print("\nThe number of residential buildings within the Oxford city limits is: " + str(cnt))

    # 13.) Use CopyFeature to copy the selected records to a new dataset
    print("\nNow saving all of the selected residential buildings within the Oxford city limits to a new dataset...")
    print("")
    arcpy.management.CopyFeatures(residential_bldng_lyr, "Oxford_ResidentialLBRS.shp")
    print("\nThe Oxford_ResidentialLBRS.shp is now in the folder: ", arcpy.env.workspace)
    print("")
    print(arcpy.GetMessages())

    # 14.) Delete the In-Memory layer
    del residential_bldng_lyr

    # 15.) Turn off overwriteOutput
    arcpy.env.overwriteOutput = False

except Exception as e:
    print("The error in your script is: ", e)
    print(arcpy.GetMessages())
