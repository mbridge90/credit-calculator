import argparse
import math
import sys

args_list = sys.argv

parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=int, help="Monthly payment")
parser.add_argument("--type", required=True, choices=["diff", "annuity"], help="Choose 'annuity' or 'diff'")
parser.add_argument("--principal", type=int, help="Credit principal")
parser.add_argument("--periods", type=int, help="Number of months to repay")
parser.add_argument("--interest", type=float, help="Interest rate")
args = parser.parse_args()

if args.interest:
    i = args.interest / 1200
p = args.principal
n = args.periods
a = args.payment

def get_differential_monthly_payment(p, n, i):
    total = 0
    for m in range(1, n + 1):
        d = math.ceil((p / n) + i * (p - (p * (m-1)) / n))
        print(f'Month {m}: paid out {d}')
        total += d
    print(f'\nOverpayment = {total - p}')

def get_annuity_principal(a, i, n):
    p = math.floor(a / ((i * (1 + i) ** n) / (((1 + i) ** n) - 1)))
    print(f'Your credit principal = {p}!\nOverpayment = {a * n - p}')

def get_annuity_monthly_payment(p, i, n):
    a = math.ceil(p * (i * (1 + i) ** n) / (((1 + i) ** n) - 1))
    print(f'Your monthly annuity = {a}!\nOverpayment = {a * n - p}')

def get_repayment_time(a, i, p):
    n = math.ceil(math.log((a / (a - i * p)), 1 + i))
    years = n // 12
    months = n % 12
    if years and months:
        print(f'You need {years} years and {months} months to repay this credit!')
    elif months and not years:
        print(f'you need {months} months to repay this credit!')
    elif years and not months:
        print(f'You need {years} years to repay this credit!')
    print(f'Overpayment = {a * n - p}')

def calculate():
    if len(args_list) < 5:
        print("Incorrect parameters.")
        return

    if args.type == "diff":
        if args.payment:
            print("Incorrect parameters.")
        else:
            get_differential_monthly_payment(p, n, i)
    elif args.type == "annuity":
        if not args.periods:
            get_repayment_time(a, i, p)
        if not args.payment:
            get_annuity_monthly_payment(p, i, n)
        if not args.principal:
            get_annuity_principal(a, i, n)

calculate()