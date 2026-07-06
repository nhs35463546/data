import streamlit as st

# 페이지 설정 (웹 브라우저 탭에 표시될 이름과 아이콘)
st.set_page_config(page_title="여행 일정 플래너", page_icon="✈️")

# 제목과 아이콘
st.title('✈️ 여행 일정 정하기')

# 구분선 추가
st.divider()

# 작성자 정보 (캡션 스타일로 작게)
st.caption('### 30410 노현서')
st.info('완벽한 여행 일정을 같이 조정해봐요!')
