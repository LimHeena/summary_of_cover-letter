import streamlit as st
import pandas as pd
import numpy as np

col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
    # column 1 에 담을 내용
    st.header('here is column1')
with col2 :
    # column 2 에 담을 내용
    st.header('자기소개서 문장 입력')
    st.markdown("<div style='text-align: center;'>완성하기 어려운 문장을 입력해주세요.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>합격자소서를 바탕으로 문장을 작성해드립니다.</div>", unsafe_allow_html=True)
    
    sentences = ['문장1:', '문장2:', '문장3:']
    for sentence in sentences:
        st.text_input(sentence)

    if st.button('완성하고 싶은 문장 추가하기'): #없어도 괜찮을듯..
        sentences.append(f'문장{len(sentences)+1}:')
        st.text_input(sentences[-1])
    
    # st.markdown("<div style='text-align: center;'>"
    #         "<button>문장 완성하기</button>"
    #         "</div>", unsafe_allow_html=True)
    button_style = 'width: 23rem; height: 3rem; font-size: 1.2rem; border: none; border-radius: 4px;'
    st.markdown(f'<center><button style="{button_style}">문장 완성하기</button></center>', unsafe_allow_html=True)



#streamlit run st.py