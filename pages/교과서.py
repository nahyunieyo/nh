# quadratic_graph_basic.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 제목
st.title("이차함수의 그래프 기본형(y=ax²) 분석하기")
st.write("a값을 조절해서 그래프 모양을 관찰해봅시다.")

# 사용자 입력: a값
a = st.slider("a값을 선택하세요", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)

# x, y 계산
x = np.linspace(-5, 5, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color='blue', linewidth=2)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_title(f'y = {a}x²')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle='--', alpha=0.5)

st.pyplot(fig)

# 그래프 성질 설명
if a > 0:
    st.write("✅ a > 0 → 아래로 볼록 (U자형)")
elif a < 0:
    st.write("✅ a < 0 → 위로 볼록 (∩자형)")
else:
    st.write("⚠️ a = 0 → y=0 직선")

st.write("|a|이 커질수록 그래프 폭이 좁아집니다.")
st.write("|a|이 작을수록 그래프 폭이 넓어집니다.")
