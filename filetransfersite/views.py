from django.shortcuts import render
from django import forms
from io import BytesIO
import os
from os.path import exists
import base64
from filetransfersite.models import files
from django.urls import path

directory_path = os.getcwd()
url = 'http://127.0.0.1:8000/'

# Create your views here.
class fileUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == "POST":
        #print(request.FILES)
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
            encodedname = base64.b64encode(str(file).encode('utf-8'))
            files.objects.create(title=encodedname, fileName=str(file))
            global url
            return render(request, 'uploaded.html', {'url' : url + str(encodedname)})
        else:
            #print errors
            print(form.errors)
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html',
            {'form': fileUploadForm()})