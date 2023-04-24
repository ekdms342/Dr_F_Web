from django.shortcuts import render
from django.http import HttpResponse

# 파일 업로드 위한 import 
# pip install django-upload-form
from upload_form.forms import UploadForm

# 파일 저장을 위한 import 
import os
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile 
from django.conf import settings
from dr_f_app import models
from dr_f_app.models import Image

# 판다스 
import pandas as Pd 

# yolo 폴더
#from  dr_f_app.yolo import yolo as yolo

# ml 폴더
# from dr_f_app.ml import 각각의 모델.py 이름

# 자연어 폴더 
#from dr_f_app.nl import nl as nl

#  Hello 문구를 브라우저에 보이기 위한 html 생성하기 
def index(request) :
    html = """
        <html>
            <head>
                <title> ::: Hello ::: </title>
            </head>
            <body>
                <u>Hello 잘 나옴니다!! </u>
            </body>
        </html>
            
    """
    return HttpResponse(html)

# 메인 화면 
def main (request) :
    
    return render(
        request,
        "dr_f_app/main.html",
        {}
    )

# 진단 입력 
def diagnosis (request) :
    
    return render(
        request,
        "dr_f_app/diagnosis.html",
        {}
    )   

# 비전 이밎 저장하기  
def vison_predict(request) :
    
    if request.method == "GET" :
        form = UploadForm(request.GET, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            path = models.Image(
                image = uploaded_file
            )
            path.save()
            result = models.Image.objects.all()
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 저장 되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
    elif request.method == "POST" :
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            path = models.Image(
                image = uploaded_file
            )
            path.save()
            result = models.Image.objects.all()
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 저장 되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
    
    
# 머신러닝 입력
def ml_insert (request) :
    
    return render(
        request,
        "dr_f_app/predict.html",
        {}
    )   

# 머신러닝 파일 저장하기 
def ml_file_save(request) :
    
    if request.method == "GET" :
        form = UploadForm(request.GET, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['csv']
            path = models.Image(
                csv = uploaded_file
            )
            path.save()
            result = models.Image.objects.all()
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 저장 되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
    elif request.method == "POST" :
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['csv']
            path = models.Image(
                csv = uploaded_file
            )
            path.save()
            result = models.Image.objects.all()
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 저장 되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
        



    

# Create your views here.
