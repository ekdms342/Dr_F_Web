from django.shortcuts import render
from django.http import HttpResponse

# 파일 업로드 위한 import 
# pip install django-upload-form
from upload_form.forms import UploadForm


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

def main (request) :
    
    return render(
        request,
        "dr_f_app/main.html",
        {}
    )
 
def diagnosis (request) :
    
    return render(
        request,
        "dr_f_app/diagnosis.html",
        {}
    )   

# 비전 모델 불러오기 
def vison_predict(request) :
    
    if request.method == "GET" :
        form = UploadForm(request.GET, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES           
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 입력되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
    elif request.method == "POST" :
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES 
            print(uploaded_file)
            # 모델 처리 코드 넣기 
            return HttpResponse('{"form" : "파일이 잘 입력되었습니다"}')
        else :
            return HttpResponse('{"form" : "파일이 없습니다"}')
    
    
# 머신러닝 모델 불러오기 

        



    

# Create your views here.
