# Maria's UGX Loan Amortization Calculator
import pandas as pd

def ugx_loan_emi(principal, annual_rate, years):
    print("--- Maria's UGX Loan Calculator ---")
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    print(f"Monthly EMI = UGX {emi:.0f}")
    return emi

# Test it with 1M UGX loan
ugx_loan_emi(1000000, 15, 2)
