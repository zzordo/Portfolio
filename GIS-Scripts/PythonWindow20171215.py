"""
Created By:    Zachary Ordo
Created Date:  2017-12-15
Last Modified: 2017-12-15
This ArcGIS Python Script was created to describe data sources in an MXD file and print output for analysis and troubleshooting.
"""

import arcpy
import os
workspace = os.path.dirname("ROW Areas")
print workspace
desc = arcpy.Describe("ROW Areas")
print desc
print desc.path
workspace = os.path.dirname(desc)
arcpy.Describe(desc)
domainDisc = [d.codedValues for d in arcpy.da.ListDomains(desc)]
print workspace
print desc
print desc.path
desc = arcpy.Describe("\MIDSTREAM.DBO.PROPOSED\ROW Areas")
workspace = os.path.defpath("ROW Areas")
os.path.basename("ROW Areas")
os.path.basename(workspace)
desc_fc = arcpy.Describe("ROW Areas")
print desc_fc
print desc_fc.path
desc_gdb = arcpy.Describe(desc_fc.path)
mxd = arcpy.mapping.MapDocument("CURRENT_DOCUMENT")
mxd = arcpy.mapping.MapDocument("CURRENT_MXD")
mxd = arcpy.mapping.MapDocument("CURRENT")
desc_fc.name
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
    print(".lyr file: {}".format(desc.catalogPath))
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))
    
for lyr in arcpy.mapping.ListLayers(mxd)
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dsource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + fcName[1]
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dSource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + fcName[1]
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dSource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + fcName
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dSource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + str(fcName)
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
        print "Layer Name: " + lyr.name
        print "DB Name: " + dbName
        print "Service Name: " + serviceName
        print "Server Name: " + serverName
        print "User Name: " + userName
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dSource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + str(fcName)
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("SERVICEPROPERTIES"):
        servProp = lyr.serviceProperties
        lName = lyr.name
        dbName = servProp.get('Database', 'N/A')
        serviceName = servProp.get('Service', 'N/A')
        serverName = serviceName.split(':')
        userName = servProp.get('UserName', 'N/A')
        print "Layer Name: " + lyr.name
        print "DB Name: " + dbName
        print "Service Name: " + serviceName
        print "Server Name: " + str(serverName)
        print "User Name: " + userName
    else:
        print "SERVICEPROPERTIES not supported on " + lyr.name
        continue
    if lyr.supports("DATASOURCE"):
        dSource = str(lyr.dataSource)
        fcName = dSource.split('.sde\\')
        print "Layer Name: " + lyr.name
        print "Feature Class: " + str(fcName)
    else:
        print "DATASOURCE not supported on " + lyr.name
        continue
        
thisGDB = "Database Connections\THOPSQL02 - Midstream.sde"
fields = arcpy.ListFields(self.params[4].value)for field in fields:
    if field.name == self.params[4].value and field.domain != "":
      self.params[5].filter.list = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
    
thisGDB = "Database Connections\THOPSQL02 - Midstream.sde"
fields = arcpy.ListFields("ROW Areas")        

print fields
for field in fields:
    if field.name == "Route Type" and field.domain != "":
        self.params[5].filter.list = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]]
        
for field in fields:
    if field.name == "Route Type" and field.domain != "":
        self.params[5].filter.list = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
        
for field in fields:
    if field.name == "Route Type" and field.domain != "":
        cvdList = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
        
print cvdList
for field in fields:
    print field
    if field.name == "Route Type" and field.domain != "":
        cvdList = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
        
for field in fields:
    print field.name
    if field.name == "Route Type" and field.domain != "":
        cvdList = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
        
for field in fields:
    print field.name
    if field.name == "Route_Type" and field.domain != "":
        cvdList = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
        
print cvdList
for field in fields:
    print field.name + " - " + field.domain
    if field.name == "Route_Type" and field.domain != "":
        cvdList = [d.codedValues for d in arcpy.da.ListDomains(thisGDB) if d.name == field.domain]
