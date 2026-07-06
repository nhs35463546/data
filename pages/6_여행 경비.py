import streamlit as st

st.subheader('여행 경비 정산 방식')

# 드롭다운(Selectbox) 위젯 생성
expense_method = st.selectbox(
    "여행 경비는 어떻게 정산하고 싶으신가요?",
    ['한 번에 모아서', '각자 알아서', '후청구'],
    index=None,  # 첫 화면에서 아무것도 선택되지 않은 상태로 시작 (선택 사항)
    placeholder="정산 방식을 선택해 주세요"
)

# 사용자가 항목을 선택했을 때만 결과 출력
if expense_method:
    st.write(f"선택하신 정산 방식: **{expense_method}**")
else:
    st.write("⚠️ 경비 정산 방식을 선택해 주세요.")
