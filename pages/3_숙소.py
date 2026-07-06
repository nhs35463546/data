import streamlit as st

st.subheader('선호하는 숙소 유형 선택')

# 중복 선택이 가능한 multiselect 위젯 생성
accommodation_types = st.multiselect(
    "원하시는 숙소 유형을 모두 선택해 주세요 (중복 선택 가능)",
    ['호텔', '리조트', '모텔', '게스트하우스'],
    default=['호텔']  # 웹앱이 처음 켜졌을 때 기본으로 선택되어 있을 항목 (선택 사항)
)

# 사용자가 선택한 결과를 화면에 깔끔하게 출력
if accommodation_types:
    # 선택한 항목들을 쉼표(,)로 연결하여 보여줍니다.
    selected_str = ", ".join(accommodation_types)
    st.write(f"선택하신 숙소: **{selected_str}**")
else:
    # 아무것도 선택하지 않았을 때의 안내 문구
    st.write("⚠️ 최소 하나 이상의 숙소 유형을 선택해 주세요.")
