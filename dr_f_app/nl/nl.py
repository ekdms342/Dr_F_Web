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
        
        self.model