# rational_expression_app.py
import streamlit as st
from sympy import symbols, simplify, Rational, sympify

# 페이지 제목
st.title("유리식의 연산 학습 앱")
st.write("두 유리식을 입력하고 연산을 선택해 결과를 확인해보세요.")

# 변수 정의
x = symbols('x')

# 사용자 입력
st.subheader("유리식 입력")
expr1_str = st.text_input("첫 번째 유리식 입력 (예: (x**2 + 2*x + 1)/(x+1))")
expr2_str = st.text_input("두 번째 유리식 입력 (예: (x+1)/(x+2))")

# 연산 선택
operation = st.selectbox("연산 선택", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

# 연산 버튼
if st.button("연산하기"):
    try:
        # 문자열을 sympy 표현식으로 변환
        expr1 = sympify(expr1_str)
        expr2 = sympify(expr2_str)
        
        # 선택한 연산 수행
        if operation == "덧셈":
            result = simplify(expr1 + expr2)
        elif operation == "뺄셈":
            result = simplify(expr1 - expr2)
        elif operation == "곱셈":
            result = simplify(expr1 * expr2)
        elif operation == "나눗셈":
            result = simplify(expr1 / expr2)
        
        st.subheader("결과")
        st.write(result)
        
        # 추가: 약분 전후 비교
        st.subheader("성질 확인")
        st.write("약분 전/후 비교:", expr1 + expr2 if operation=="덧셈" else
                 expr1 - expr2 if operation=="뺄셈" else
                 expr1 * expr2 if operation=="곱셈" else
                 expr1 / expr2, "→", result)
        
    except Exception as e:
        st.error(f"입력 오류: {e}")
