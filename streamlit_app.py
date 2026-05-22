import streamlit as st

# 페이지 제목 설정
st.title("📦 배송비 안내 프로그램")
st.markdown("---")

# 사용자 입력 받기 (input 대체)
member = st.radio("정기 회원입니까?", ("예(y)", "아니오(n)"))
total = st.number_input("주문 금액은 얼마입니까?", min_value=0, step=1000, format="%d")

# 계산 및 결과 출력 (print 대체)
if st.button("결제 금액 확인"):
    if member == "예(y)":
        st.success("정기회원으로 배송비가 면제됩니다.")
        st.subheader(f"총 결제 금액은 {total:,}원 입니다.")
    else:
        st.warning("배송비 3,000원이 부과됩니다.")
        final_total = total + 3000
        st.subheader(f"총 결제 금액은 {final_total:,}원 입니다.")
   ```
