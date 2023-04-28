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

# json 으로 넘기기 위한 import 
from django.http import JsonResponse
from django.core import serializers

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

# diagnosis.html 의 데이터 받아오기 
def diagnosis_predict(request) :
    if request.method == 'POST':
        # 이미지 파일 
        image = request.FILES['image']
        # 이미지 파일 저장
        path = models.Image(
                image = image
        )
        path.save()
        
        # 이미지 모델 돌리기 
        vison_result = "이미지 처리 결과(병해 여부)" 
        # 이미지 처리 결과(작물 종류)
        vison_crop = "딸기"
        
        # 자연어 입력 데이터 
        position = request.POST['position']
        color = request.POST['color']
        shape = request.POST['shape']
        
        # 자연어 모델 돌리기 
        nl_result = "자연어 처리 결과"
        
        # 이미지 모델 결과와 자연어 모델 결과 바탕으로 가중치 부여햇 최종 결과 만들기
        result = "정상"
        
        # 최종결과에 따른 방제방법 안내 
        how_control = "토양을 짚 같은 것으로 피복을 하거나 병든 조직을 조기에 제거하는 것도 좋은 방법이며 무엇보다도 환기를 철저히 하여 식물체 표면을 건조한 상태로 유지하는 것이 매우 중요하다."
        
        # 최종 결과가 정상인지 아닌지에 따라 분기하기 
        if result == "정상" : 
            return render(request,
                          "dr_f_app/nomal_result.html",
                          {'image':image,
                           'position' : position,
                           'color': color,
                           'shape' : shape,
                           'crop':vison_crop,
                           'result' : result
                           })
        else :
            return render(request,
                        "dr_f_app/dise_result.html",
                        {'image':image,
                        'position' : position,
                        'color': color,
                        'shape' : shape,
                        'result' : result,
                        'how_control' : how_control
                        })    
    else:
        return HttpResponse('error 발생')
 
    
# 머신러닝 입력창 열기 
def ml_insert (request) :
    crop = request.POST['crop']
    return render(
        request,
        "dr_f_app/predict.html",
        {"crop" : crop}
    )   
  
# predict.html 의 데이터 받아오기 
def ml_predict(request) :
    if request.method == 'POST':
        # csv 파일 
        csv = request.FILES['csv']
        # csv 파일 저장
        path = models.Image(
                csv = csv
        )
        path.save()
        
        # 작물 이름 가져오기 
        crop = request.POST['crop_name']

        # 작물이름에 따라 머신러닝 모델 돌리기 
        if crop == "딸기":
            ml_result = "잿빛곰팡이"
        elif crop == "파프리카" : 
            ml_result = "파프리카"
        elif crop == "오이" :
            ml_result = "오이"
        
        # 최종 결과에 따라 방제방법 불러오기 
        protect_result = "병든 식물은 수거하여 시설 밖 지정된 장소에서 소각하거나 땅속에 묻어 전염원을 차단하는 것이 중요하다. 또한 환기나 난방을 통해 습도를 낮추고 주야 간 온도차가 심하지 않도록 관리하는 게 중요하다."
        
        # 최종 결과 보여주기 
        return render(request,
                    "dr_f_app/predict_result.html",
                    {'csv':csv,
                    'ml_result' : ml_result,
                    'protect_result': protect_result,
                    'crop' : crop
                    })  
    else:
        return HttpResponse('error 발생')
 


    

# Create your views here.
