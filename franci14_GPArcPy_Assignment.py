# franci14_GPArcPy_Assignment.py
# GEO 443 Python Programming
# Buffer and Clip analysis - Grand River, OH
# Jacob S. Francis
# 03/13/2026
# Tool syntaxes in this script:
# BUFFER TOOL:
# arcpy.analysis.Buffer(in_features, out_feature_class, buffer_dist_or_field,{line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
# arcpy.Buffer_analysis(in_features, out_feature_class, buffer_dist_or_field,{line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
# CLIP TOOL:
# arcpy.analysis.Clip(in_features, clip_features, out_feature_class, {cluster_tolerance})
# arcpy.Clip_analysis(in_features, clip_features, out_feature_class, {cluster_tolerance})
##########################################
# STEPS:
# Import ArcPy
# Set the workspace to the assignment data
# Print the workspace to the user
# Overwrite the output
# Try/Except block for the bulk of the script
# Set up the list of feature classes that will get plugged into the script
#   - 1=Urban, 2=Agricultural,3=Shrub, 4=Wooded, 5=Open Water, 6=Non Forested Wetlands, 6=Barren
# Print when the variables have been set
# Buffer Grand River by 300 meters
#   - use the optional parameters for a FULL line side, ROUND end type, and ALL dissolve type
#   - print statement to say when it is starting the buffer tool
# Clip the land cover polygon dataset to only include the buffered river
#   - for the lake county data
#   - print statement to say when it is starting the clip tool
###########################################
import arcpy
# import the arcpy module
arcpy.env.workspace = "C:\\francis_jake\\GEO_443\\Module_12\\M12.10_GP_Assignment\\12.10_GP_Data\\GP_Assignment_Data\\GPAssignmentData.gdb"
# workspace set to the data location file in explorer
# must be set to the GDB since the shapefiles cannot live inside the GDB
print("\nThe workspace for the data used in the script is ", arcpy.env.workspace)
# print the workspace to the user
arcpy.env.overwriteOutput = True
# boolean operator to allow the code to overwrite the existing data structure
# try/except block for the code
try:
    buff_inFC = "grand_river_ohsp"
    buff_outFC = "grand_river_buffer"
    buff_dist = "300 meters"
    line_side = "FULL"
    line_end_type = "ROUND"
    dissolve_option = "ALL"
    clip_inFC = "lake_county_lulc94"
    clip_outFC = "StrmBuff_LULC"
    stats_out_table = "LULC_area_summary"
    stats_fields = [["Shape_Area", "SUM"]]
    case_field = "LULC_type"
    print("\nThe VARIABLES have been set for the script")
    # defining the variables that will be plugged into the buffer and clip analysis
    print("\nThe BUFFER analysis is starting...")
    arcpy.analysis.Buffer(buff_inFC, buff_outFC, buff_dist, line_side, line_end_type, dissolve_option)
    # buffer analysis that is run on the river
    # FULL - buffers both sides of the line
    # ROUND - the shape of the buffer line
    # ALL - dissolves all buffers into a single shape
    print(arcpy.GetMessages())
    # print out the buffer tool that was used to the user
    print("\nThe CLIP analysis is now starting...")
    arcpy.analysis.Clip(clip_inFC, buff_outFC, clip_outFC)
    # clip out the land that is not contained within the river buffer
    print(arcpy.GetMessages())
    # print out the clip tool that was used to the user
    print("\nFinally, the SUMMARY STATISTICS tool is now starting...")
    arcpy.analysis.Statistics(clip_outFC, stats_out_table, stats_fields, case_field)
    # summary statistics tool aggregates the sum of land
    # Need the field to calculate (statistic - sum) and the grouping field (CASE)
    print(arcpy.GetMessages())
    print("\nSummary table", stats_out_table, "has been created in the workspace")
    # prints the last run tool
    # prints the summary table back to user
    print("\nYou can find the output data for this script at", arcpy.env.workspace, "which is called", clip_outFC)
    # print statement for where the data can be found in the file
    arcpy.env.overwriteOutput = False
    # Turn off the overwrite output
except Exception as e:
    print(e)
    # use this to print the error messages
    # make sure to comment it out in the end
except:
    print("There is an error in the script")
    # except block to read if an error occurs in the script
