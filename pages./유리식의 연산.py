import streamlit as st
import random
import numpy as np
from PIL import Image

# 박명수 이미지 불러오기
def load_image():
    return Image.open("park_myeongsoo.jpg")  # 이미지 경로를 맞게 설정해줘

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
