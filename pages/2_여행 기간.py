import streamlit as st
from datetime import date

st.subheader('여행 기간 슬라이더')

# 1. 최소 및 최대 날짜 설정 (2026년 7월 21일 ~ 2026년 8월 12일)
min_date = date(2026, 7, 21)
max_date = date(2026, 8, 12)

# 2. 날짜 범위 선택 슬라이더
# value에 튜플 (시작일, 종료일)을 넣으면 범위를 선택하는 양방향 슬라이더가 생성됩니다.
travel_dates = st.slider(
    "원하는 여행 기간을 선택해 주세요:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),  # 기본 선택값을 전체 기간으로 설정
    format="YYYY/MM/DD"          # 시간 표기(hh:mm) 제거
)

# 3. 결과 출력 (travel_dates는 (선택된 시작일, 선택된 종료일) 형태의 튜플입니다)
st.write("선택된 시작 날짜:", travel_dates[0])
st.write("선택된 종료 날짜:", travel_dates[1])
