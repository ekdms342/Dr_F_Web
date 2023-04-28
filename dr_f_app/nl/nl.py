import pandas as pd
import os

## 형태소 분석 
from konlpy.tag import Okt
## 단어별 갯수 카운트
from collections import Counter

# 코사인 유사도 계산 
from sklearn.metrics.pairwise import cosine_similarity

# g나글 사전 학습 모델 가져오기 
from sentence_transformers import SentenceTransformer

class NL :
    
    def __init__(self) :
        
        # 사전에 임베딩 해 저장해둔 파일 가져오기 
        self.df = pd.read_csv("./nl_csv")
        # text 임베딩 값 계산을 위한 모델 가져오기 
        self.model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    
    def predict(self,position,color,shape) :
        
        text = "" + position + color + shape
        ebd=self.model.encode(text)
        # 코사인 유사도 값 계산 해서 저장하기 
        self.df['distance'] = self.df['embedding'].map(lambda x : cosine_similarity([ebd], [x]).squeeze())
        # 