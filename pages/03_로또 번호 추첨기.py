# lotto_picker_app.py

import streamlit as st
import random


# ====== 로또 번호 생성 함수 ======
def generate_one_set():
    """1~45 사이에서 6개 랜덤 추첨"""
    return sorted(random.sample(range(1, 46), 6))


def generate_sets(n):
    """n개의 세트 생성"""
    return [generate_one_set() for _ in range(n)]


def compare_with_winning(generated, winning):
    """추천 번호와 당첨 번호 비교"""
    r
