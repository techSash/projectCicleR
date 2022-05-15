from distutils.command.upload import upload
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from prediction_app import deeplearning
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

# create view to handle file upload
def handle_image_upload(request):
    if request.method == 'POST':

        myfile = request.FILES['image_input']
        if ('.png' in str(myfile)) or ('.jpg' in str(myfile)) or ('.jpeg' in str(myfile)):
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            
            prediction = deeplearning.use_model(uploaded_file_url)
            
            json_data = {'prediction': prediction, 'status': 'success'}
        
        else:
            json_data = {'status': "please upload a png or jpg image"}
        
        return JsonResponse(json_data)