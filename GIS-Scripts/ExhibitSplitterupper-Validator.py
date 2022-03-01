"""
Created By:    Zachary Ordo
Created Date:  2017-12-20
Last Modified: 2017-12-20
This ArcGIS Python Validator Script is used to control the behavior of the dialog box for the Exhibit Splitter-Upper tool.
"""

import arcpy
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    cvdList = []
    domainValues = []
    domainPicker = []
    thisGDB = self.params[2].value
    thisOutputLayer = self.params[3].value
    thisOutputField = self.params[4].value
    
    if thisGDB and thisOutputLayer and thisOutputField:
      fields = arcpy.ListFields(thisOutputLayer)
      for field in fields:
        if field.name == str(thisOutputField) and field.domain != "":
          domainValues = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
          for row in sorted(set(domainValues[0].iteritems())):
            domainPicker.append(str(row[0]))
    self.params[5].filter.list = domainPicker
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    return
