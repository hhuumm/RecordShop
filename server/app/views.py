from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def importer(request):
    html = "<html><form enctype = 'multipart/form-data' action = 'upload_csv.py' method = 'post'><br> File Uploading <input type = 'file' name = 'filename' /><input type = 'submit' value = 'Upload Now' /></form></html>"
    return HttpResponse(html)