import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="유리식의 연산", page_icon="⚡", layout="centered")

# 문제 생성 함수
def generate_fraction_problem():
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    
    while True:
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        c = random.randint(1, 12)
        d = random.randint(1, 12)

        if op == '+':
            result = (a*d + b*c) / (b*d)
        elif op == '-':
            result = (a*d - b*c) / (b*d)
        elif op == '*':
            result = (a*c) / (b*d)
        else:  # 나눗셈
            if c == 0 or b*c == 0:
                continue
            result = (a*d) / (b*c)

        # 정답이 1~100 사
