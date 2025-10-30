import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="유리식 문제집", page_icon="📘", layout="centered")

# 이미지 경로 (images 폴더 아래에 IMG_0019.png 를 넣어주세요)
GANADI_PATH = "images/IMG_0019.png"

st.title("📗 유리식 문제집 (고1 수준)")
st.write("유리식의 성질 · 연산 · 유리함수 성질 문제 총 15문제 — 객관식 보기 5개")

# -----------------------
# 유리식 연산 문제 생성: 결과가 정수(1~100)로 떨어지도록 반복 생성
# -----------------------
def generate_rational_operation():
    # 숫자 범위과 시도 제한을 두어 무한루프 방지
    for _ in range(500):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        c = random.randint(1, 12)
        d = random.randint(1, 12)
        op = random.choice(["+", "-", "*", "/"])

        if op == "+":
            expr = f"({a}/{b}) + ({c}/{d})"
            num = a * d + b * c
            den = b * d
        elif op == "-":
            expr = f"({a}/{b}) - ({c}/{d})"
            num = a * d - b * c
            den = b * d
        elif op == "*":
            expr = f"({a}/{b}) × ({c}/{d})"
            num = a * c
            den = b * d
        else:  # 나눗셈
            # 나눗셈: (a/b) ÷ (c/d) = (a*d) / (b*c)
            expr = f"({a}/{b}) ÷ ({c}/{d})"
            num = a * d
            den = b * c

        if den == 0:
            continue
        if num % den != 0:
            continue
        value = num // den
        if 1 <= value <= 100:
            return expr, str(value)
    # 실패 시 기본 안전 문제 반환 (거의 발생하지 않음)
    return "(1/1) + (1/1)", "2"

# -----------------------
# 객관식 문제 리스트(개념 문제들) — 고1 공통수학 수준
# -----------------------
concept_problems = [
    ("유리식의 정의로 가장 알맞은 것은?", "두 다항식의 나눗셈 꼴",
     ["두 다항식의 나눗셈 꼴", "항상 정수만으로 이루어진 식", "분모가 없는 식", "상수 함수만 해당", "항상 1차식"]),
    ("유리함수 f(x)=1/x의 정의역에서 제외되는 값은?", "x=0",
     ["x=1", "x=0", "모든 실수", "x=-1", "정의역에 제외되는 값이 없다"]),
    ("유리식의 곱셈을 할 때 올바른 규칙은?", "분자끼리 곱하고 분모끼리 곱한다",
     ["분자끼리 곱하고 분모끼리 곱한다", "분자를 통분한다", "항상 통분 후 더한다", "분모끼리 더한다", "분모를 없앤다"]),
    ("유리함수의 수직점근선이 생기는 이유는?", "분모가 0이 되는 x 값 때문",
     ["분자가 0이 되는 x 값 때문", "함수값이 무한대일 때", "항상 y=0 때문", "그래프가 교차할 때", "분모가 1일 때"]),
    ("수평점근선의 의미로 옳은 것은?", "x → ±∞ 일 때 y가 가까워지는 직선",
     ["x → ±∞ 일 때 y가 가까워지는 직선", "항상 y=0인 직선", "그래프가 반드시 지나는 직선", "수직선 형태", "존재할 수 없다"]),
    ("유리식의 덧셈에서 통분을 하는 이유는?", "분모를 동일하게 만들어 더하기 위해",
     ["분모를 동일하게 만들어 더하기 위해", "분자를 0으로 만들기 위해", "항상 약분하기 위해", "곱셈을 쉽게 하기 위해", "함수의 값을 바꾸기 위해"]),
    ("다음 중 유리함수가 아닌 것은?", "f(x)=3x+2",
     ["f(x)=1/x", "f(x)=(x+1)/(x-2)", "f(x)=3x+2", "f(x)=(x^2+1)/(x+3)", "f(x)=(2x-1)/(x^2+1)"]),
    ("유리함수 그래프의 일반적 모양은?", "쌍곡선",
     ["쌍곡선", "직선", "포물선", "원", "곡선 없음"]),
]

# -----------------------
# 문제 조합 만들기: 개념 문제 + 연산 문제(6개) => 총 15문제
# -----------------------
problems = []
# 먼저 개념 문제들(객관식)
for q, ans, opts in concept_problems:
    # 보기가 5개가 되도록 필요시 보충 (이미 5개로 구성되어 있음)
    problems.append((q, ans, opts.copy()))

# 연산 문제 6개 자동 생성 (답은 1~100 정수 문자열)
for _ in range(6):
    expr, correct = generate_rational_operation()
    # 정답을 포함해 보기 5개 생성 (정답 포함)
    wrongs = set()
    while len(wrongs) < 4:
        w = str(random.randint(1, 100))
        if w != correct:
            wrongs.add(w)
    options = list(wrongs) + [correct]
    random.shuffle(options)
    problems.append((f"다음을 계산하시오: {expr}", correct, options))

# 개수 맞추기: 현재 개념_problems 갯수(8) + 6 연산 = 14 -> 추가로 한 문제를 더 만들어 고정형 개념문제 추가
# (원하면 더 조정 가능)
problems.append(("유리함수에서 분모가 0이면 어떤 일이 일어나나요?", "정의되지 않는다",
                 ["정의된다", "무한히 커진다", "정의되지 않는다", "항상 0이 된다", "함수값이 1이 된다"]))

# 확인: 문제 수가 15인지
assert len(problems) == 15, f"문제 개수 오류: {len(problems)} (기대값 15)"

# -----------------------
# 문제 출력 및 채점
# -----------------------
st.markdown("## 🧮 문제 풀이 (총 15문제)")
score = 0

# 로드 가능한지 미리 체크 (이미지 파일)
ganadi_img = None
try:
    ganadi_img = Image.open(GANADI_PATH)
except Exception:
    ganadi_img = None
    # 파일이 없으면 안내 메시지는 나중에 틀렸을 때 보여줄 것

for i, (q, answer, opts) in enumerate(problems, start=1):
    st.write(f"### {i}. {q}")
    # 라디오 버튼의 key를 문제 번호로 고유하게 지정
    choice = st.radio(f"문제 {i} 답 선택:", opts, key=f"q{i}")

    # 사용자가 선택하면 바로 피드백 (실전 테스트 형태)
    if choice:
        if choice == answer:
            st.success("정답이야! 🎉")
            score += 1
        else:
            st.error("응 아니야 😅")
            if ganadi_img:
                st.image(ganadi_img, caption="가나디: 응 아니야!", use_column_width=False)
            else:
                st.warning(f"오답일 때 표시할 이미지({GANADI_PATH})를 찾을 수 없습니다. "
                           "images/IMG_0019.png 파일을 프로젝트의 images 폴더에 넣어주세요.")

st.markdown("---")
st.write(f"### ✅ 총 {len(problems)}문제 중 정답: {score}문제")

# 간단한 피드백 메시지
if score == len(problems):
    st.balloons()
    st.success("완벽해요! 유리식 달인입니다 🌟")
elif score >= 10:
    st.info("잘했어요! 조금만 더 연습해요 💪")
else:
    st.warning("복습이 필요해요. 다시 한번 풀어볼까요? 📘")
