# pages/유리식_문제.py
import streamlit as st
from sympy import symbols, simplify
import random

st.set_page_config(page_title="유리식 연산 문제", layout="wide")
st.title("📘 유리식 연산 문제 교과서")

x = symbols('x')

st.write("코드가 문제를 만들어주고, 계산 후 답을 확인할 수 있습니다. 모든 답은 정수꼴입니다.")

# ===== 문제 생성 함수 =====
def generate_problem():
    # 정수 계수 생성
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    # 연산 선택
    op = random.choice(["+", "-", "*", "/"])
    
    if op == "+":
        expr = a*x + b*x
        solution
