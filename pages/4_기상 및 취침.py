import streamlit as st

st.subheader('기상 및 취침 패턴 조사')

# 1. 기상 시간 라디오 버튼 (index=None으로 기본 선택 해제)
wake_up = st.radio(
    "여행지에서의 기상 패턴을 선택해 주세요:",
    ('일찍 일어난다', '늦게 일어난다'),
    index=None
)

# 2. 취침 시간 라디오 버튼
sleep_time = st.radio(
    "여행지에서의 취침 패턴을 선택해 주세요:",
    ('일찍 잔다', '늦게 잔다'),
    index=None
)

# 3. 두 항목을 모두 선택했을 때만 결과를 보여줌
if wake_up and sleep_time:
    st.write(f"당신의 여행 스타일: **{wake_up}**, **{sleep_time}**")
else:
    # 아직 선택하지 않은 항목이 있다면 안내 메시지 출력
    st.write("⚠️ 기상 패턴과 취침 패턴을 모두 선택해 주세요.")
