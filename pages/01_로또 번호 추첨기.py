# lotto_picker_app.py

import streamlit as st  
import random  
from typing import List, Set

def generate_one_set() -> List[int]:  
    return sorted(random.sample(range(1, 46), 6))

def generate_sets(n: int) -> List[List[int]]:  
    return [generate_one_set() for _ in range(n)]

def compare_with_winning(generated: List[int], winning: Set[int]) -> int:  
    return len(set(generated) & winning)

def main():  
    st.title("로또 번호 추천기 (Lotto 6/45)")  
    st.write("1부터 45까지 중에서 6개의 숫자를 추천해 드립니다.")  

    # 사용자 입력  
    num_sets = st.number_input("추천 세트 수를 입력하세요", min_value=1, max_value=100, value=1, step=1)  
    if st.button("추천 생성"):  
        st.write(f"추천 세트 {num_sets}개 생성!")  
        sets = generate_sets(num_sets)  
        for idx, s in enumerate(sets, start=1):  
            st.write(f"세트 {idx}: {s}")  

        # 최근 당첨 번호 입력  
        st.write("---")  
        st.write("최근 당첨 번호를 입력하세요 (6개 숫자).")  
        col1, col2, col3, col4, col5, col6 = st.columns(6)  
        with col1: n1 = st.number_input("1번", min_value=1, max_value=45, value=1, step=1)  
        with col2: n2 = st.number_input("2번", min_value=1, max_value=45, value=2, step=1)  
        with col3: n3 = st.number_input("3번", min_value=1, max_value=45, value=3, step=1)  
        with col4: n4 = st.number_input("4번", min_value=1, max_value=45, value=4, step=1)  
        with col5: n5 = st.number_input("5번", min_value=1, max_value=45, value=5, step=1)  
        with col6: n6 = st.number_input("6번", min_value=1, max_value=45, value=6, step=1)  

        winning_nums = {n1, n2, n3, n4, n5, n6}  
        st.write(f"입력한 최근 당첨 번호: {sorted(winning_nums)}")  

        st.write("추천 번호와 비교 결과:")  
        for idx, s in enumerate(sets, start=1):  
            matched = compare_with_winning(s, winning_nums)  
            st.write(f"세트 {idx}: {s} → 맞은 숫자 개수: {matched}")  

if __name__ == "__main__":  
    main()
