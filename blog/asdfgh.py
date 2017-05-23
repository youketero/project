import arcpy
import os
import zipfile
import ast
from blog.models import point2

data = point2.objects.value_list('x', 'y')
'''
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Lesson1"
featureClassList = arcpy.ListFeatureClasses()
featureClass = "Europe_cities"
w = 0
if featureClass not in featureClassList:    
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "us_cities.shp", "DISABLED", "DISABLED", "us_cities.shp")
searchedField = ['UIDENT','POPCLASS','CAPITAL','STATEABB']
insertedField = ("SHAPE@XY")
fie = ['NAME','COUNTRY']
arcpy.DeleteField_management(featureClass+'.shp', searchedField )
a = []
b = []
j = []
k = []
'''
data1 = point2.objects.values_list('city')
'''
for i in d:
     a.append(i['fields']['y'])
     b.append(i['fields']['x'])
     j.append(i['fields']['city'])
     k.append(i['fields']['Country'])
c = zip(a,b)
with arcpy.da.InsertCursor(featureClass+'.shp',insertedField) as cursor:
    for row in c:
        cursor.insertRow([row])
del cursor
with arcpy.da.UpdateCursor(featureClass+'.shp', fie) as cursor:
        for row in cursor:
            row[0] = j[w]
            row[1] = k[w]
            cursor.updateRow(row)
            w +=1
del cursor
arcpy.CopyFeatures_management("Europe_cities.shp", "D:/json/Europe_cities.shp")
zipfd = zipfile.ZipFile('test.zip','w', zipfile.ZIP_DEFLATED)
path = 'D:\\json\\'
files = os.listdir(path)
for i in files:
    file = os.path.join(path, i)
    zipfd.write(file)
zipfd.close()
'''

