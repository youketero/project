import os
import zipfile
from django.shortcuts import render, get_object_or_404
import arcpy
from blog.models import Article, point2
def home(request):
    articles = Article.objects.all()
    context = {
         'articles':articles
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')
def article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    return render(request , 'blog/article.html' , {"article" : article})
def mymap(request):
    return render(request, "blog\map.html")
def serial(models):
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = r"D:\Lesson1"
    featureClassList = arcpy.ListFeatureClasses()
    featureClass = "Europe_cities_5"
    if featureClass not in featureClassList:
        arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "Europe_cities_4.shp", "DISABLED",
                                            "DISABLED", "Europe_cities_4.shp")
        print "Europe_cities_4 was created"
    '''
    searchedField = ['UIDENT', 'POPCLASS', 'CAPITAL', 'STATEABB']
    arcpy.DeleteField_management(featureClass + '.shp', searchedField)
    '''
def cursor(models):
    arcpy.env.overwriteOutput = True
    insertedField = "SHAPE@XY"
    fie = ['NAME', 'COUNTRY']
    w = 0
    data = models.objects.values_list('y', 'x')
    data1 = models.objects.values_list('city','Country')
    with arcpy.da.InsertCursor("Europe_cities_5" + '.shp', insertedField) as cursor:
        for row in data:
            cursor.insertRow([row])
    del cursor
    with arcpy.da.UpdateCursor("Europe_cities_5" + '.shp', fie) as cursor:
        for row in cursor:
            row[0] = data1[w][0]
            row[1] = data1[w][1]
            cursor.updateRow(row)
            w += 1
    del cursor
def zippo(models):
    arcpy.CopyFeatures_management("Europe_cities.shp", "D:/json/Europe_cities.shp")
    zipfd = zipfile.ZipFile('Europe_final.zip', 'w', zipfile.ZIP_DEFLATED)
    path = 'D:\\json\\'
    files = os.listdir(path)
    for i in files:
        file = os.path.join(path, i)
        zipfd.write(file)
    zipfd.close()
serial(point2)
cursor(point2)
zippo(point2)