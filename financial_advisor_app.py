import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("AI-Powered Financial Advisor")

    # Input Section
    st.header("Enter Your Financial Details")
    income = st.number_input("Monthly Income (₹):", min_value=0)
    expenses = st.number_input("Monthly Expenses (₹):", min_value=0)
    savings_goal = st.number_input("Savings Goal (₹):", min_value=0)

    if st.button("Calculate"):
        if income <= 0:
            st.error("Income must be greater than 0.")
        elif expenses >= income:
            st.error("Expenses should be less than Income.")
        else:
            savings = income - expenses
            months_to_goal = savings_goal / savings if savings > 0 else float('inf')

            # Display Recommendations
            st.subheader("Financial Summary")
            st.write(f"Your monthly savings: ₹{savings:.2f}")
            if savings_goal > 0:
                if months_to_goal == float('inf'):
                    st.write("It's impossible to reach your savings goal with the current income and expenses.")
                else:
                    st.write(f"You will reach your savings goal in {months_to_goal:.2f} months.")

            # Budget Visualization
            st.subheader("Budget Visualization")
            labels = ['Expenses', 'Savings']
            values = [expenses, savings]
            colors = ['#ff9999', '#66b3ff']

            # Pie Chart
            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
            ax.axis('equal')  # Equal aspect ratio ensures the pie is a circle.
            st.pyplot(fig)

            # Savings Goal Progress
            st.subheader("Savings Goal Progress")
            if savings_goal > 0:
                fig, ax = plt.subplots()
                months = list(range(1, int(months_to_goal) + 1))
                cumulative_savings = [savings * month for month in months]
                ax.plot(months, cumulative_savings, marker='o', label="Cumulative Savings")
                ax.axhline(y=savings_goal, color='r', linestyle='--', label="Savings Goal")
                ax.set_xlabel("Months")
                ax.set_ylabel("Savings (₹)")
                ax.set_title("Progress Towards Savings Goal")
                ax.legend()
                st.pyplot(fig)

if __name__ == "__main__":
    main()

