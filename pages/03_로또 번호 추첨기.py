# lotto_picker_app.py

import streamlit as st
import random
from typing import List, Set


def generate_one_set() -> List[int]:
    """1부터 45 사이에서 6개 랜덤 숫자를 추첨"""
    return sorted(random.sample(range(1, 46), 6))


def generate_sets(n: int) -> List[List[int]]:
    """n개의 추천 세트를 생성"""
    return [generate_one_set() for _ in range(n)]


def compare_with_winning(generated: List[int], winning: Set[int]) -> int:
    """추천 번호와 당첨 번호 비교"""
    return len(set(generated) & winning)


def main():
    st.title("🎰 로또 번호 추천기 (Lotto 6
