import streamlit as st

st.subheader('여행 계획 스타일 조사')

# 일반 slider가 아닌 select_slider를 사용합니다.
plan_style = st.select_slider(
    "여행 계획은 어떻게 세우는 편이신가요?",
    options=['꼼꼼하게', '대략적으로', '무계획'],
    value='대략적으로'  # 슬라이더가 처음 켜졌을 때 위치할 기본값 (가운데로 설정)
)

# 결과 출력
st.write(f"당신의 계획 스타일: **{plan_style}**")
