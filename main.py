# Maria's UGX Loan Amortization Calculator - Full 24 Month Table
def ugx_loan_emi_with_table(principal, annual_rate, years):
    print("--- Maria's UGX Loan Calculator ---")
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    print(f"Loan: UGX {principal:,.0f} | Rate: {annual_rate}% | Period: {years} years")
    print(f"Monthly EMI = UGX {emi:.0f}")
    
    balance = principal
    print("\nMonth-by-Month Amortization Schedule")
    print(f"{'Month':<8}{'Payment':<12}{'Principal':<12}{'Interest':<12}{'Balance':<12}")
    print("-" * 56)
    
    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance = balance - principal_paid
        if balance < 1: balance = 0 # fixes rounding on last month
        print(f"{month:<8}{emi:<12.0f}{principal_paid:<12.0f}{interest:<12.0f}{balance:<12.0f}")
    
    print("-" * 56)
    print("Done. All 24 months accounted for.")

# Test case: 1M UGX loan at 15% for 2 years
ugx_loan_emi_with_table(1000000, 15, 2)
