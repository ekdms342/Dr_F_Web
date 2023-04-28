import pandas as pd
import os 
from collections import defaultdict
import warnings
from pycaret.classification import *

class ML :
    def __init__(self) :
        # 모델들 불러오기 
        # 딸기 모델
        self.sb_model = load_model("./models/strawberry_ml_lgbm_24.pkl")
        # 파프리카 모델
        self.pp_model = load_model("./models/paprika_ml_rf_24.pkl")
        # 오이 모델
        self.cu_model = load_model("./models/cucumber_lgbm.pkl")
        # 고추 모델
        self.ch_model = load_model("./models/chili_ml_knn_24.pkl")
        # 토마토 모델
        self.to_model = load_model("./models/tomato_model.pkl")
        # 포도 모델
        self.gr_model = load_model("./models/grape_model.pkl")
    
    def predicton(self,crop,csv):
        crop_csv = pd.read_csv(csv)
        warnings.filterwarnings(action='ignore')
        crop_df = pd.DataFrame()
        crop_df['온도평균'] = crop_csv['내부온도'].mean()
        crop_df['습도평균'] = crop_csv['습도평균'].mean()
        crop_df['이슬점평균'] = crop_csv['이슬점평균'].mean()
        
        crop_df['온도최고'] = crop_csv['내부온도'].max()
        crop_df['습도최고'] = crop_csv['내부습도'].max()
        crop_df['이슬점최고'] = crop_csv['내부이슬점'].max()
        
        crop_df['온도최저'] = crop_csv['내부온도'].min()
        crop_df['습도최저'] = crop_csv['내부습도'].min()
        crop_df['이슬점최저'] = crop_csv['내부이슬점'].min()
        
        if crop == "딸기" :
            self.sb_model
        
        
        
    
    
            



