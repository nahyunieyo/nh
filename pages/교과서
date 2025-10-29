import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 이차함수의 그래프 기본형(y = ax²) 분석하기")
st.write("""
이 앱에서는 **y = a·x²** 의 그래프를 다양한 a값에 대해 그려보며  
그래프의 **모양(볼록 방향)** 과 **폭(가파름)** 이 어떻게 달라지는지 살펴볼 수 있습니다.
""")

# a 값 슬라이더
a = st.slider("a 값 선택", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
st.write(f"현재 a 값: **{a}**")

# 데이터 생성
x = np.linspace(-5, 5, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {a:.2f}x²")
ax.grid(True, linestyle="--", alpha=0.5)
fig.tight_layout()

st.pyplot(fig)

# 설명 출력
st.subheader("그래프 관찰 포인트 🧠")

if a > 0:
    st.write("- **a > 0** 이므로 그래프는 **아래로 볼록(U자형)** 입니다.")
elif a < 0:
    st.write("- **a < 0** 이므로 그래프는 **위로 볼록(∩자형)** 입니다.")
else:
    st.write("- **a = 0** 이므로 그래프는 **y=0 직선**입니다.")

st.write("- |a|가 커질수록 그래프의 **폭이 좁아지고** 가파릅니다.")
st.write("- |a|가 작을수록 그래프의 **폭이 넓어집니다.**")
