from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile, File
from django.conf import settings
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import MyModel
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.conf import settings
import os

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
        
            request_file = request.FILES['upload'] if 'upload' in request.FILES else None
            if request_file:
                fs = FileSystemStorage()
                file = fs.save(request_file.name, request_file)
                fileurl = fs.url(file)
                print(fileurl)
                request.session['file'] = file
                return redirect('index1')
    form = UploadFileForm()
    return render(request, "index.html",{"form":form})


def index1(request):
    return render(request,'index1.html')
    
   
    
def download_file(request):
    file = request.session.get('file')
    pat=settings.MEDIA_ROOT
    ME = os.path.join(pat,file)
    response = HttpResponse(content_type='application/xlsx')
    response['Content-Disposition'] = f'attachment; filename="FILENAME.xlsx"'
    with pd.ExcelWriter(response) as writer:
        df = pd.read_csv(ME)
        df['Number of Plays'] = df['Number of Plays'].astype(int)
        data = df.groupby(['Song','Date'],as_index=False).sum()
        print(data)
        data.to_excel(writer, sheet_name='SHEET NAME')

    return response