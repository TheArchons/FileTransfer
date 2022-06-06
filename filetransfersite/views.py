from django.shortcuts import render
from django import forms
from io import BytesIO
import os
from os.path import exists
import base64
from django.urls import path
from django.http import FileResponse

directory_path = os.getcwd()
url = 'http://35.165.232.47:8000/'

# Create your views here.
class fileUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == "POST":
        form = fileUploadForm(request.POST, request.FILES)
        print(request.FILES['file'].file)
        if form.is_valid():
            global directory_path
            file = form.cleaned_data['file']
            if not exists(str(file)):
                with open(str(file), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            else:
                return render(request, 'error.html', {'error': 'Error: File already exists'})
            encodedname = str(base64.b64encode(str(file).encode('utf-8')))[2:][:-1]
            global url
            print(encodedname)
            return render(request, 'uploaded.html', {'url' : url + 'confirmDownload/' + encodedname})
        else:
            #print errors
            print(form.errors)
            return render(request, 'error.html', {'error': form.errors})
    else:
        return render(request, 'upload.html',
            {'form': fileUploadForm()})

def download(request, file_name):
    print(file_name)
    file_name = base64.b64decode(file_name).decode('utf-8')
    return FileResponse(open(file_name, 'rb'))

def confirmDownload(request, file_name):
    print(file_name)
    file_name_decoded = base64.b64decode(file_name).decode('utf-8')
    global url
    return render(request, 'confirmDownload.html', {'downloadURL' : url + 'download/' + file_name, 'filename': file_name_decoded})