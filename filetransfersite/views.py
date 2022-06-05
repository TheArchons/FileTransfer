from django.shortcuts import render
from django import forms
from io import BytesIO
import os

directory_path = os.getcwd()

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
            with open(str(file), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return render(request, 'index.html', {'url' : 'asd'})
        else:
            #print errors
            print(form.errors)
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html',
            {'form': fileUploadForm()})