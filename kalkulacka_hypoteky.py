# Jednoduchá hypoteční kalkulačka
import math
from tabulate import tabulate


def main():
    print("\n" + "Mortgage calculator", "\n" + "-" * 19)
    loan = int(input("How much do you want to borrow?: "))
    rate = float(input("At what rate?: "))
    years = int(input("How many years?: "))
    print("=" * 45)

    monthly_payment = calc_monthly_payment(loan, rate, years)
    total_paid = calc_total_payment(monthly_payment, years)

    print(f"Loan: {loan} czk")
    print(f"Years: {years:} years")
    print(f"Rate: ", rate, "%")
    print(f"Monthly Payment: {round(monthly_payment):,} czk")
    print(f"Interest: {round(total_paid - loan):,} czk")
    print()
    print_table(create_table_values(years, loan, monthly_payment, rate))


def calc_monthly_payment(principal, interest, years):
    """S ohledem na jistinu, úrok a roky vypočítejte částku měsíční splátky"""
    # měsíční úroková sazba
    month_interest = interest / (100 * 12)
    # počet plateb
    payment_num = years * 12
    # výpočet měsíční splátky
    monthly_payment = principal * (
        month_interest / (1 - math.pow((1 + month_interest), (-payment_num)))
    )
    return round(monthly_payment, 2)


def calc_total_payment(monthly_payment, term_years):
    """S ohledem na měsíční platbu a roky v letech vypočítejte celkovou částku k zaplacení"""
    total_paid = monthly_payment * term_years * 12
    return round(total_paid, 2)


def calc_interest_for_month(principal, monthly_payment, rate):
    """S ohledem na částku jistiny a celkovou částku platby vypočítejte  zaplacený úrok"""
    interest_this_month = principal * (rate / 100) / 12
    return round(interest_this_month, 2)


def create_table_values(years, principal, monthly_payment, rate):
    table_values = []
    remaining_principal = principal
    for year in range(1, years + 1):
        for month in range(1, 12 + 1):
            interest_this_month = calc_interest_for_month(
                remaining_principal, monthly_payment, rate
            )
            # spočítat nižší zůstatek, která má být zaplacen tento měsíc
            # minulý měsíc je nižší než standardní výpočet
            principal_this_month = min(
                monthly_payment - interest_this_month, remaining_principal
            )
            remaining_principal = remaining_principal - principal_this_month
            # uložit hodnoty v pořadí:
            # rok a měsíc platby, splátka úroku, splátka půjčky, zůstatek
            tabl_payment_no = f"Year {year}, Month {month}"
            tabl_interest = f"{interest_this_month:>8,.2f} czk"
            tabl_principal = f"{principal_this_month:>9,.2f} czk"
            tabl_left_to_pay = f"{remaining_principal:>11,.2f} czk"
            table_values.append(
                [tabl_payment_no, tabl_interest, tabl_principal, tabl_left_to_pay]
            )
    return table_values


def print_table(table_values):
    """Se seznamem hodnot vytiskněte tabulku hypotéky"""
    print(
        tabulate(
            table_values,
            headers=["Payment", "Interest", "Principal", "Left to Pay"],
            tablefmt="outline",
        )
    )


def __init__():
    return


if __name__ == "__main__":
    main()
