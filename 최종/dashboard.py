import warnings

warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import rc

rc('font', family='AppleGothic')


@st.cache_data
def load_data(data_path, xlsx=False):
    # 여기에 데이터를 로드하는 코드를 작성하세요
    if xlsx:
        df = pd.read_excel(data_path, engine='openpyxl')
    else:
        df = pd.read_csv(data_path)
    return df

order_df = load_data('/Users/raphaelseo/Documents/study/fastcampus/바이트디그리/최종/order-9968.txt')
course_df = load_data('/Users/raphaelseo/Documents/study/fastcampus/바이트디그리/최종/course-9968.csv')
customer_df = load_data('/Users/raphaelseo/Documents/study/fastcampus/바이트디그리/최종/customer-9968.xlsx', True)
refund_df = load_data('/Users/raphaelseo/Documents/study/fastcampus/바이트디그리/최종/refund-9968.csv')
user_df = load_data('/Users/raphaelseo/Documents/study/fastcampus/바이트디그리/최종/user-9968.csv')



option = st.sidebar.selectbox(
    'Menu',
     ('페이지1', '페이지2', '페이지3'))


st.title('데이터 분석 대시보드')


st.subheader('데이터 미리보기')
st.write(order_df.head())
st.write(course_df.head())
st.write(customer_df.head())
st.write(refund_df.head())
st.write(user_df.head())

st.subheader('데이터 시각화')
# 여기에 차트와 그래프를 추가하세요