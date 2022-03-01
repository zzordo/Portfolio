"""
Created By:    Zachary Ordo
Created Date:  2017-12-20
Last Modified: 2017-12-20
This ArcGIS Python Script was created to automate the generation of exhibit maps in ArcMap as an alternative to ArcGIS Production Mapping and Data Driven Pages.
"""

import arcpy
from arcpy import env

arcpy.env.workspace = "in_memory"

proposedPipelinesLayer = arcpy.GetParameterAsText(0)
parcelsLayer = arcpy.GetParameterAsText(1)
# outputWorkspace = arcpy.GetParameterAsText(2) - Only required for validation script purposes.  Not used in ExhibitSplitterupper.py
outputLayer = arcpy.GetParameterAsText(3)
outputTypeField = arcpy.GetParameterAsText(4)
outputTypeValue = arcpy.GetParameterAsText(5)
parcelsLayerOwnerField = arcpy.GetParameterAsText(6)
parcelsLayerIDField = arcpy.GetParameterAsText(7)
outputParcelOwnerField = arcpy.GetParameterAsText(8)
outputParcelIDField = arcpy.GetParameterAsText(9)
appendLayer = "thisOutputLayer"

# Delete layers from memory first, if layers already exist.
try:
    arcpy.Delete_management("pipelineSelection", 'GPFeaureLayer')
except:
    pass
try:
    arcpy.Delete_management(appendLayer, 'GPFeatureLayer')
except:
    pass

# Create feature class in memory containing the selection 
arcpy.CopyFeatures_management(proposedPipelinesLayer, "pipelineSelection")
arcpy.AddField_management("pipelineSelection", outputTypeField, "TEXT", "", "", 50)
expression = "'{value}'".format(value = outputTypeValue)
arcpy.CalculateField_management("pipelineSelection", outputTypeField, expression, "PYTHON_9.3")

# Intersect selection with parcels, output to thisOutputLayer
arcpy.Intersect_analysis(["pipelineSelection",parcelsLayer],appendLayer)

# Begin creating field mappings for "TEST" in arcpy.Append_management()
fieldmappings = arcpy.FieldMappings() # Empty grid of fields.
fieldmappings.addTable(outputLayer)  # Add output dataset fields to the field map table.
fieldmappings.addTable(appendLayer)  # Add append dataset fields to the field map table.

# Map the fields that have different names.
list_of_fields_we_will_map = []
list_of_fields_we_will_map.append([outputParcelOwnerField, parcelsLayerOwnerField])
list_of_fields_we_will_map.append([outputParcelIDField, parcelsLayerIDField])

for field_map in list_of_fields_we_will_map:
    # Find the fields index by name (e.g. parcelsLayerOwnerField)
    field_to_map_index = fieldmappings.findFieldMapIndex(field_map[0])
    # Grab a copy of the current field map object for this particular field
    field_to_map = fieldmappings.getFieldMap(field_to_map_index)
    # Update its data source to add the input from the append layer
    field_to_map.addInputField(appendLayer, field_map[1])
    # We edited a copy, update our data grid object with it
    fieldmappings.replaceFieldMap(field_to_map_index, field_to_map)

# For Dubugging Field Mappings: arcpy.AddMessage(str(fieldmappings))
# Create a list of append datasets and append intersected features to the user selected output layer.
inData = [appendLayer]
arcpy.AddMessage("Creating " + str(arcpy.GetCount_management(appendLayer)) + " features in " + outputLayer)
arcpy.Append_management(inData, outputLayer, "NO_TEST", fieldmappings)
