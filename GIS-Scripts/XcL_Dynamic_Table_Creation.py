import arcpy
import os
import numpy
import decimal
from datetime import date
arcpy.env.overwriteOutput = True
today = str(date.today())
today = today.replace("-", "")

Path = os.path.normpath(arcpy.GetParameterAsText(0))

map_path = arcpy.GetParameterAsText(1)
mxd = arcpy.mapping.MapDocument(map_path)

genMXDs = arcpy.GetParameterAsText(2)
genPDFs = arcpy.GetParameterAsText(3)
outputNames = arcpy.GetParameterAsText(4)
param5 = arcpy.GetParameterAsText(5)
exhibitType = arcpy.GetParameterAsText(6)
prelimROWWidth = int(arcpy.GetParameterAsText(7))
pageRangeType = arcpy.GetParameterAsText(8)
pageRange = arcpy.GetParameterAsText(9)

# Used to accommodate special use cases (such as overriding Route Type text)
# specialSettings = arcpy.GetParameterAsText(10)

ddp = mxd.dataDrivenPages

def unique_values(table, field):
    data = arcpy.da.TableToNumPyArray(table, [field])
    return numpy.unique(data[field]).tolist()

def exitHandler():
    import sys
    sys.exit()

# Accepts a user input comma or semi-colon separated string of page numbers
# or page number ranges and converts it to a list of integers containing all
# page numbers that will be printed.
def pagesParser(pageRange):
    pageRangeReplacer = pageRange.replace(';',',')
    pageRangeReplacer = pageRangeReplacer.replace(' ',',')
    pageRangeSplitter = pageRangeReplacer.split(',')
    pageRangeSplitter = filter(None, pageRangeSplitter)
    pagesList = []
    try:
        # Find any ranges and append each page number in the range to pagesList
        for item in pageRangeSplitter:
            pages = item.split('-')
            if len(pages) == 2:
                for num in range(int(pages[0]), int(pages[1]) + 1):
                    pagesList.append(num)
            # If the item is not a range (only a single page), append to pagesList
            else:
                pagesList.append(int(pages[0]))
    except:
        # Throw an error if the function fails to append any values to pagesList
        raise sys.exit("Error: " + arcpy.GetMessages(x))
    
    # Validation to make sure no page numbers are negative values or higher than
    # the number of available pages in the data driven pages mxd.pagesList[:]
    # creates a copy of the list so values can be removed from the original list.
    for page in pagesList[:]:
        if page > ddp.pageCount or page < 1:
            pagesList.remove(page)

    pagesListString = str(pagesList).replace('[','')
    pagesListString = pagesListString.replace(']','')
    arcpy.AddMessage("\nPrinting the following pages: " + pagesListString)
    del pageRangeReplacer, pageRangeSplitter, pagesListString
    return pagesList

#mxd = arcpy.mapping.MapDocument(r"A:\GIS\Projects\EXHIBITS\MXD\20170818_COVESTRO_EXHIBIT.mxd")
ddp.refresh()
arcpy.RefreshTOC()

#Reference items in the map document
lyr = "ROW Areas" #****Layer name you are working off of for calcs. 
horzLine = arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT", "horzLine")[0]
vertLine = arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT", "vertLine")[0]
tableText = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "TableText")[0]

#Get/set information about the table
numRows = 6
rowHeight = 0.1571428571428571
fieldNames = ["Route_Type", "Distance_Feet", "Area_Acres", "Surface_Owner"]
fieldAlias = ["Route Type", "Distance (Feet)", "Area (Acres)"]
numColumns = len(fieldAlias)
colWidth = 1.6824

#Build graphic table lines based on upper left coordinate
#  set the proper size of the original, parent line, then clone it and position appropriately
upperX = 1.9533
upperY = 1.5

#Vertical lines
vertLine.elementPositionX = upperX
vertLine.elementPositionY = upperY
vertLine.elementHeight =  (rowHeight * numRows) + rowHeight #extra line for column names

x = upperX
for vert in range(1, numColumns+1):
    x = x + colWidth
    vert_clone = vertLine.clone("_clone")
    vert_clone.elementPositionX = x

#Horizontal lines
horzLine.elementPositionX = upperX
horzLine.elementPositionY = upperY
horzLine.elementWidth = numColumns * colWidth

y = upperY - rowHeight
for horz in range(1, numRows +2 ):  #need to accommodate the extra line for field names
    temp_horz = horzLine.clone("_clone")
    temp_horz.elementPositionY = y
    y = y - rowHeight

#Place text column names
tableText.elementPositionX = upperX + 0.05 #slight offset
tableText.elementPositionY = upperY - 0.03
tableText.text = fieldAlias[0]
accumWidth = colWidth
for field in range(1, numColumns):
    newFieldTxt = tableText.clone("_clone")
    newFieldTxt.text = fieldAlias[field]
    newFieldTxt.elementPositionX = newFieldTxt.elementPositionX + accumWidth
    accumWidth = accumWidth + colWidth

#Create text elements based on values from the table
#Table to table
geoDatabasePath = str(Path) + '\Working.gdb'

arcpy.TableToTable_conversion(lyr, geoDatabasePath,'DDP_Data')
myTablePath = geoDatabasePath + '\DDP_Data'

#table = arcpy.da.SearchCursor(myTablePath,fieldNames, sql_clause =(None, 'ORDER BY Surface_Owner'))
#for row in table:
#    arcpy.AddMessage(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))

pageRangeID = -1 # += 1 will be performed upon entering the uniqueOwners for loop
if pageRangeType == 'ALL':
    pageNumRange = pagesParser('1-' + str(ddp.pageCount))
elif pageRangeType == 'CURRENT':
    pageNumRange = []
    pageNumRange.append(int(ddp.currentPageID))
elif pageRangeType == 'RANGE':
    pageNumRange = pagesParser(pageRange)

uniqueOwners = []

arcpy.AddMessage("\nPreparing to generate exhibit maps for the following property owners:")
for row in unique_values(myTablePath, 'Surface_Owner'):
    #arcpy.AddMessage(row) # For troubleshooting
    uniqueOwners.append(row)

uniqueOwners.sort(key=lambda x: x.replace("-", " ")) # Use a lambda expression to change the sort method to better match text sort used by ArcMap Sort by Attributes

# Remove owners whose pages are not in the user selected pageNumRange
keptUniqueOwners = []
for page in pageNumRange:
    keptUniqueOwners.append(uniqueOwners[page-1])
    arcpy.AddMessage(u' \u2022 ' + uniqueOwners[page-1])
uniqueOwners = keptUniqueOwners
del keptUniqueOwners

for curOwner in uniqueOwners:
    y = upperY - (rowHeight +.05)   # Reset y position to first row for each new page (owner)
    expression = 'Surface_Owner = ' + "'%s'" % str(curOwner).replace("'", "''") # Parameterized sql where clause to prevent variables that have single quotes in them from throwing an error
    
    routeTypes = []
    ssaRouteTypes = []
    ssaFootage = 0
    ssaAcreage = 0
    arcpy.AddMessage("\n" + curOwner + ":")

    tupleToList = [[routeType[0], routeType[1], routeType[2]] for routeType in arcpy.da.SearchCursor(myTablePath,fieldNames,where_clause = expression)]

    for routeType in tupleToList:
        # Map table must depict None values as 0's
        if routeType[1] is None:
            routeType[1] = 0
        if routeType[2] is None:
            routeType[2] = 0
        
        if exhibitType == 'Surface Use Agreement':
            if routeType[0] == 'Additional Temporary Workspace': # Surface use agreements refer to this as ATWSA.
                routeType[0] = 'ATWSA'
            ssaFootage += routeType[1]
            ssaAcreage += routeType[2]
        
        if exhibitType <> 'Surface Use Agreement':
            routeTypes.append(routeType)
        else:
            ssaRouteTypes.append(routeType)

        if exhibitType == 'Preliminary (Route Only)' and routeType[0] in {'Right-of-Way', 'Water Lines'}:
            twsAcreage = (float(routeType[1]) * prelimROWWidth)/43560
            routeTypes.append(['Temporary Workspace', 0, twsAcreage])

    routeTypes.sort()
    if len(ssaRouteTypes) > 0:
        if len(routeTypes) > 0: # Create separation with a blank row if non-surface site area route types exist on the page.
            ssaRouteTypes.append(['AAA BLANK ROW', 0, 0])
        ssaRouteTypes.sort()
        ssaRouteTypes.append(['Surface Site Area', ssaFootage, ssaAcreage]) 

    pageRangeID += 1
    curPage = pageNumRange[pageRangeID]

    routeTypes += ssaRouteTypes
    
    for row in routeTypes:
        x = upperX + 0.05   # Reset x position to first column for each new route type (row)
        ddp.currentPageID = curPage

        try:  # Add the Route Type to the table
            if row[0] is None or row[0] == 'AAA BLANK ROW':
                #arcpy.AddMessage("Field is None")
                rowText = ''
                next
            else:
                rowText = row[0]
                newCellTxt = tableText.clone("_routeclone")            
                rowText += str(': ')
                if row[0] == 'Surface Site Area': # Bold if Surface Site Area
                    rowText = "<BOL>" + rowText + "</BOL>"
                newCellTxt.text = rowText
                newCellTxt.elementPositionX = x
                newCellTxt.elementPositionY = y
                accumWidth = accumWidth + colWidth
        except:
            arcpy.AddMessage("Invalid value assignment")

        x = upperX + colWidth + 0.05

        try: # Add the Distance (Feet) to the table
            if row[1] is None or row[0] == 'AAA BLANK ROW':
                #arcpy.AddMessage("Field is None")
                distText = ''
                next
            else:
                newCellTxt = tableText.clone("_routeclone")
                distText = '{:,.2f}'.format(round(float(row[1]),2))
                # distText += ' ft' - Removed 1/24/18 per request from Michael Timmons
                if row[0] == 'Surface Site Area': # Bold if Surface Site Area
                    distText = "<BOL>" + distText + "</BOL>"
                newCellTxt.text = distText
                newCellTxt.elementPositionX = x
                newCellTxt.elementPositionY = y
                accumWidth = accumWidth + colWidth
        except:
            arcpy.AddMessage("Invalid value assignment")

        x = upperX + (colWidth * 2) + 0.05

        try: # Add the Area (Acres) to the table
            if row[2] is None or (exhibitType == 'Preliminary (Route Only)' and row[0] == 'Permanent ROW') or row[0] == 'AAA BLANK ROW':
                #arcpy.AddMessage("Field is None")
                areaText = ''
                next
            else:
                newCellTxt = tableText.clone("_routeclone")
                areaText = '{:,.2f}'.format(round(float(row[2]),2))
                # areaText += ' ac' - Removed 1/24/18 per request from Michael Timmons
                if row[0] == 'Surface Site Area': # Bold if Surface Site Area
                    areaText = "<BOL>" + areaText + "</BOL>"
                newCellTxt.text = areaText
                newCellTxt.elementPositionX = x
                newCellTxt.elementPositionY = y
                accumWidth = accumWidth + colWidth

        except:
            arcpy.AddMessage("Invalid value assignment")

        if distText <> '':
            rowText += distText

        if areaText <> '':
            if distText <> '':
                rowText += ' - ' + areaText
            else:
                rowText += areaText

        arcpy.AddMessage(u' \u2022 ' + rowText)

        y -= 0.1572 # Advance to the next row

    #Export to PDF and delete cloned elements
    #arcpy.mapping.ExportToPDF(mxd, r"Z:\GIS\Requests\Exhibits\Stairway\test.pdf")

    pageName = curOwner.replace(" ", "_")

    addtlOutputNameText = param5
    if addtlOutputNameText[0] <> '_' and addtlOutputNameText[0] <> '-' and addtlOutputNameText <> '':
        addtlOutputNameText = '_' + addtlOutputNameText
        
    if outputNames == 'Page # & First 10 of Name':
        namingString = str(curPage) + str("_") + pageName[0:10] + addtlOutputNameText
    elif outputNames == 'Page #':
        namingString = str(curPage) + addtlOutputNameText
    elif outputNames == 'Page Name':
        namingString = pageName + addtlOutputNameText
    elif outputNames == 'Page #, First 10 of Name, Date':
        if addtlOutputNameText <> '':
            addtlOutputNameText += '_'
        namingString = str(curPage) + str("_") + pageName[0:10] + addtlOutputNameText + today
    elif outputNames == 'Page # & Date':
        if addtlOutputNameText <> '':
            addtlOutputNameText += '_'
        namingString = str(curPage) + addtlOutputNameText + today
    elif outputNames == 'Page Name & Date':
        if addtlOutputNameText <> '':
            addtlOutputNameText += '_'
        namingString = pageName + addtlOutputNameText + today
    
    exportFilePath = os.path.normpath(Path + str("\\") + namingString)

    if str(genPDFs) == 'true':
        arcpy.mapping.ExportToPDF(mxd, exportFilePath)
        arcpy.AddMessage(" + Exporting to " + exportFilePath + ".pdf")

    if str(genMXDs) == 'true':
        mxd.saveACopy(exportFilePath + ".mxd")
        arcpy.AddMessage(" + Exporting to " + exportFilePath + ".mxd")

    ddp.refresh()
    arcpy.RefreshTOC()
    
    for elm in arcpy.mapping.ListLayoutElements(mxd, wildcard="*_routeclone*"):
        elm.delete()
        
    x = upperX + colWidth + 0.05

del mxd

del curOwner, routeTypes

arcpy.AddMessage('\n')

