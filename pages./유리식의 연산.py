# pages/유리식_연산_문제집.py
import streamlit as st
from sympy import symbols, simplify
import random

st.set_page_config(page_title="유리식 연산 문제집", layout="wide")
st.title("📘 유리식 연산 문제집 (정수 결과)")

x = symbols('x')

st.write("아래 문제를 직접 계산하고, '답 보기' 버튼을 눌러 확인하세요. 모든 답은 정수 형태입니다.")

# ===== 문제 생성 함수 =====
def generate_problem():
    # 계수 선택 (정수)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    # 연산 선택
    op = random.choice(["+", "-", "*", "/"])
    
    if op == "+":
        expr = a*x + b*x
        problem_text = f"{a}x + {b}x"
        solution = simplify(expr)
    elif op == "-":
        expr = a*x - b*x
        problem_text = f"{a}x - {b}x"
        solution = simplify(expr)
    elif op == "*":
        expr = (a*x)*(b*x)
        problem_text = f"({a}x) * ({b}x)"
        solution = simplify(expr)
    else:  # "/"
        # 나눗셈은 정수 결과가 나오도록 a, b 조정
        b = random.randint(1, 10)
        a = b * random.randint(1, 10)
        expr = (a*x)/(b*x)
        problem_text = f"({a}x) / ({b}x)"
        solution = simplify(expr)
    
    return problem_text, solution

# ===== 여러 문제 생성 =====
num_problems = 5
problems = [generate_problem() for _ in range(num_problems)]

# ===== 문제 출력 =====
for i, (problem_text, solution) in enumerate(problems, 1):
    st.subheader(f"문제 {i}")
    st.latex(problem_text)
    
    if st.button(f"문제 {i} 답 보기"):
        st.latex(solution)

st.info("🔄 새로고침하면 다른 문제로 바뀝니다.")
