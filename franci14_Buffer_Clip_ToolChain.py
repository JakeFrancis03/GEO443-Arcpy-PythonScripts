# franci14_Buffer_Clip_ToolChain.py
# Jacob S. Francis
# GEO 443A - Python Programming
# This script will buffer the parks by 500 feet and then clip the hospitals
# 03/08/2026
# Tool syntaxes in this script:
# CLIP TOOL
# arcpy.analysis.Clip(in_features, clip_features, out_feature_class, {cluster_tolerance})
# arcpy.Clip_analysis(in_features, clip_features, out_feature_class, {cluster_tolerance})
# BUFFER TOOL
# arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
# arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
import arcpy
# input the module
arcpy.env.workspace = "C:\\francis_jake\\GEO_443\\Module_12\\PythonScripting_Ex05_Data\\Ex05"
# Set the workspace to the folder where the data lives
print("\nThe workspace for the data used in the script is ", arcpy.env.workspace)
# \n as the escape character for a new line
arcpy.env.overwriteOutput = True
# Overwrite output line to allow the code to overwrite the existing database
# starting a try/except block for this new code
try:
    # Set up the feature classes that we will plug into the GP script
    buff_inFC = "parks.shp"
    buff_outFC = "parks_buffer.shp"
    buff_dist = "500 feet"
    clip_inFC = "hospitals.shp"
    clip_outFC = "hospitals_clip.shp"
    print("\nVariables have been set for the script")
    print("\nBuffer analysis is starting.....")
    arcpy.analysis.Buffer(buff_inFC, buff_outFC, buff_dist)
    # Buffer analysis of the parks (inFC) for 500 foot buffer.
    print(arcpy.GetMessages())
    # Getmessages() to print out the latest tool use
    print("\nClip analysis is now starting.....")
    arcpy.analysis.Clip(clip_inFC, buff_outFC, clip_outFC)
    # clip out the hospitals that are within 500 feet of the parks
    # these variables are used as data inputs/outputs
    print(arcpy.GetMessages())
    # Getmessages() to print out the latest tool use
    print("\nYou can go to", arcpy.env.workspace, "to find the output data named", clip_outFC)
    # print statement for the workspace that these new GP sources live
    arcpy.env.overwriteOutput = False
except Exception as e:
    print(e)

except:
    print("Error in Script")
