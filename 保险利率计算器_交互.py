import streamlit as st
from scipy.optimize import fsolve

def calculate_annual_interest(annual_investment, investment_years, total_years, final_amount):
    # 定义方程
    def equations(r):
        total = 0
        for i in range(int(investment_years)):
            total += annual_investment * (1 + r)**(total_years - i - 1)
        return total - final_amount

    # 使用fsolve求解方程
    initial_guess = 0.05  # 初始猜测的年利率
    rate = fsolve(equations, initial_guess)
    return rate[0]

def main():
    st.title("年利率计算器")

    annual_investment = st.number_input("每年投入的金额（万元）：", min_value=0.0, value=1.2, step=0.1)
    investment_years = st.number_input("需要投几年的年数：", min_value=1, value=5, step=1)
    total_years = st.number_input("总的投资期数（年）：", min_value=1, value=20, step=1)
    final_amount = st.number_input("最终取出的金额（万元）：", min_value=0.0, value=93.5556, step=0.1)

    if st.button("计算"):
        rate = calculate_annual_interest(annual_investment, investment_years, total_years, final_amount)
        st.success(f"实际年利率约为：{rate * 100:.2f}%")

if __name__ == "__main__":
    main()
