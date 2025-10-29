import streamlit as st
import random
import numpy as np
from PIL import Image

# 정수로 떨어지는 유리식 연산 문제 생성
def generate_fraction_problem():
    # 분자와 분모는 정수로 만들기
    num1 = random.randint(1, 10)
    denom1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    denom2 = random.randint(1, 10)

    # 유리식 덧셈 문제를 만든다고 가정
    # num1/denom1 + num2/denom2
    common_denominator = denom1 * denom2
    new_num1 = num1 * denom2
    new_num2 = num2 * denom1
    correct_answer = (new_num1 + new_num2) // common_denominator  # 정수로 떨어지게 설정

    problem = f"{num1}/{denom1} + {num2}/{denom2}"
    return problem, correct_answer

# 스트림릿 앱
def app():
    st.title("유리식의 연산 교과서")

    # 문제 생성
    problem, correct_answer = generate_fraction_problem()
    st.write(f"문제: {problem} = ?")

    # 보기 생성 (정답 포함 4개의 틀린 보기)
    options = [correct_answer]
    while len(options) < 5:
        wrong_answer = random.randint(correct_answer - 5, correct_answer + 5)
        if wrong_answer != correct_answer:
            options.append(wrong_answer)
    random.shuffle(options)

    # 보기 출력
    answer = st.radio("정답을 고르세요:", options)

    # 정답 확인
    if answer == correct_answer:
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다!")
        # 박명수 이미지 출력
        st.image(load_image(), caption="응 아니야")

if __name__ == "__main__":
    app()

import streamlit as st
from PIL import Image

# 이미지 업로드 및 표시 함수
def load_image(uploaded_file):
    return Image.open(uploaded_file)

# 스트림릿 앱
def app():
    st.title("이미지 업로드 및 표시")

    # 파일 업로드 기능
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "png", "webp"])

    # 업로드된 파일이 있을 경우
    if uploaded_file is not None:
        # 이미지 불러오기
        image = load_image(uploaded_file)
        st.image(image, caption="업로드된 이미지", use_column_width=True)

# 앱 실행
if __name__ == "__main__":
    app()
