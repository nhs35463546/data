import streamlit as st

st.subheader('선호하는 여행지 유형 선택')

# 1. 단일 선택 라디오 버튼 생성
destination = st.radio(
    "어떤 유형의 여행지를 선호하시나요?",
    ('도시', '자연', '휴양지', '기타')
)

# 2. '기타' 선택 시 동작할 조건문
if destination == '기타':
    # 기타를 선택하면 텍스트 입력창을 띄움
    other_destination = st.text_input("원하시는 여행지 유형을 직접 입력해 주세요:")
    
    # 사용자가 빈칸에 내용을 입력했을 때만 결과 출력
    if other_destination:
        st.write(f"선택하신 여행지: **{other_destination}**")
else:
    # 기타 외의 항목을 선택했을 때 결과 출력
    st.write(f"선택하신 여행지: **{destination}**")
