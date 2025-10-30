import streamlit as st
from PIL import Image
import random

# 페이지 설정
st.set_page_config(page_title="쫄라맨의 유리함수 교과서", page_icon="📘", layout="centered")

# --- 장면 전환용 페이지 선택 ---
page = st.sidebar.radio("장면 이동", [
    "장면 1: 학교에서 졸고 있는 쫄라맨",
    "장면 2: 쫄라맨의 공부 시작",
    "장면 3: 유리함수의 개념을 배우다",
    "장면 4: 유리함수 요약 정리",
    "장면 5: 문제 풀이하기"
])

# --- 장면 1 ---
if page == "장면 1: 학교에서 졸고 있는 쫄라맨":
    st.title("📖 장면 1: 학교에서 졸고 있는 쫄라맨")
    st.image("https://i.imgur.com/0zZ2M8C.gif", caption="쫄라맨이 수업 중에 졸고 있다 😴", use_column_width=True)
    st.write("""
    오늘은 수학 시간이에요. 선생님은 **유리함수**에 대해 설명하고 계시지만...
    앞자리의 쫄라맨은 졸고 있네요 😪  
    다음 장면으로 넘어가 볼까요?
    """)

# --- 장면 2 ---
elif page == "장면 2: 쫄라맨의 공부 시작":
    st.title("🏠 장면 2: 쫄라맨의 공부 시작")
    st.image("https://i.imgur.com/Q0bYDJF.gif", caption="두 쫄라맨이 집에서 공부 중", use_column_width=True)
    st.write("""
    수업 시간에 졸았던 쫄라맨은 반 친구와 함께 집에서 유리함수를 스스로 공부하기로 했어요.  
    그런데...
    한 쫄라맨이 말하네요.
    """)
    st.markdown("> “유리함수는... 도대체 뭐지?” 🤔")

# --- 장면 3 ---
elif page == "장면 3: 유리함수의 개념을 배우다":
    st.title("💡 장면 3: 유리함수의 개념을 배우다")
    st.image("https://i.imgur.com/3J6pBfW.png", caption="쫄라맨의 대화 장면", use_column_width=True)
    st.markdown("""
    🧍‍♂️ 쫄라맨 A: “유리함수는 무엇일까?”  
    💬 쫄라맨 B(말풍선):  
    > 유리함수는 **다항식의 나눗셈 꼴**로 나타낼 수 있는 함수야!  
    > 예를 들어,  
    > \\( f(x) = \\frac{1}{x} \\), \\( f(x) = \\frac{x+1}{x-2} \\) 같은 게 있어.  
    >
    > **정의역**은 분모가 0이 되지 않는 모든 실수야.  
    > 그래프는 대체로 쌍곡선 모양이고, **점근선**을 갖고 있어!
    """)

# --- 장면 4 ---
elif page == "장면 4: 유리함수 요약 정리":
    st.title("🧾 장면 4: 유리함수 요약 정리")
    st.write("""
    ### ✅ 유리함수의 정의
    - 두 다항식 \\(P(x), Q(x)\\)에 대해 \\( f(x) = \\frac{P(x)}{Q(x)} \\) (단, \\(Q(x) \\neq 0\\))
    - 분모가 0이 되는 값은 정의역에서 제외

    ### ✅ 주요 성질
    - **점근선**:  
      - 수직점근선 → 분모가 0이 되는 곳  
      - 수평점근선 → 최고차항의 차수 비교로 결정
    - **그래프 모양**: 쌍곡선 또는 변형된 형태

    ### ✅ 예시
    - \\( f(x) = \\frac{1}{x} \\)  
    - \\( f(x) = \\frac{x+1}{x-2} \\)
    """)

# --- 장면 5 ---
elif page == "장면 5: 문제 풀이하기":
    st.title("🧩 장면 5: 쫄라맨의 유리함수 문제")

    st.write("이제 쫄라맨이 알려준 내용을 바탕으로 문제를 풀어봅시다!")

    # 객관식 문제 3개
    st.subheader("① 유리함수의 정의에 대한 설명으로 옳은 것은?")
    q1_options = [
        "분모와 분자가 모두 상수인 함수이다.",
        "분모에 다항식이 들어가면 안 된다.",
        "두 다항식의 나눗셈 형태로 표현되는 함수이다.",
        "x가 0일 때 항상 정의된다.",
        "항상 일차함수의 그래프 모양이다."
    ]
    q1 = st.radio("①의 정답:", q1_options)
    if q1 == q1_options[2]:
        st.success("정답입니다! 🎉")
    elif q1 != "":
        st.error("틀렸어요 😢")

    st.subheader("② 다음 중 유리함수가 아닌 것은?")
    q2_options = [
        "f(x) = 1/x",
        "f(x) = (x+1)/(x-2)",
        "f(x) = 3x + 2",
        "f(x) = (x^2 + 1)/(x+3)",
        "f(x) = (2x-1)/(x^2 + 1)"
    ]
    q2 = st.radio("②의 정답:", q2_options)
    if q2 == q2_options[2]:
        st.success("정답입니다! 🎯")
    elif q2 != "":
        st.error("다시 생각해보세요 💭")

    st.subheader("③ 유리함수의 점근선에 대한 설명으로 옳은 것은?")
    q3_options = [
        "점근선은 항상 y=0이다.",
        "점근선은 x축과 y축 중 하나만 있다.",
        "점근선은 그래프가 지나가는 직선이다.",
        "점근선은 그래프가 가까워지지만 만나지 않는 직선이다.",
        "점근선은 존재하지 않는다."
    ]
    q3 = st.radio("③의 정답:", q3_options)
    if q3 == q3_options[3]:
        st.success("정답이에요 💡")
    elif q3 != "":
        st.error("조금만 더 생각해봐요!")

    st.markdown("---")
    st.subheader("④ 주관식: f(x) = 1/x의 수직점근선은 무엇인가요?")
    ans4 = st.text_input("정답을 입력하세요:")
    if ans4.strip() in ["x=0", "0", "x = 0"]:
        st.success("정답입니다! 🎉")
    elif ans4 != "":
        st.error("틀렸어요 😢")

    st.subheader("⑤ 주관식: f(x) = (x+1)/(x-2)의 수평점근선은 무엇인가요?")
    ans5 = st.text_input("정답을 입력하세요:", key="q5")
    if ans5.strip() in ["y=1", "1", "y = 1"]:
        st.success("정답입니다! 🌟")
    elif ans5 != "":
        st.error("다시 생각해봐요 🔍")

    st.markdown("---")
    st.write("🧠 수고했어요! 쫄라맨도 이제 유리함수를 완벽히 이해했답니다 😎")

