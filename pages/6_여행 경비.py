import streamlit as st

st.subheader('여행 경비 정산 방식')

# 드롭다운(Selectbox) 위젯 생성
expense_method = st.selectbox(
    "여행 경비는 어떻게 정산하고 싶으신가요?",
    ['한 번에 모아서', '각자 알아서', '후청구'],
    index=None,  # 첫 화면에서 아무것도 선택되지 않은 상태로 시작
    placeholder="정산 방식을 선택해 주세요"
)

# 사용자가 항목을 선택했을 때 요청하신 멘트 출력
if expense_method:
    # 예시: '한 번에 모아서'를 선택하면 -> "한 번에 모아서"으로 정산하자!
    # 단, 한국어 조사(로/으로)를 자연스럽게 맞추기 위해 문구를 조정했습니다.
    st.success(f'**"{expense_method}"** 방식으로 정산하자! 💰')
else:
    st.write("경비 정산 방식을 선택해 주세요.")
