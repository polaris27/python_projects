import math
import argparse
import sys

class CreditCalculator:
    def __init__(self):
        self.error = ""
        self.parser = ""
        self.i = 0
        self.periods_count = 0
        self.credit_principal = 0
        self.annuity_payment = 0
        self.payment = 0
        self.payments = 0

    def main(self):
        self.error = "Incorrect parameters"

        if len(sys.argv) >= 4:
            self.parser = argparse.ArgumentParser()
            self.parser.add_argument("--type", type=str, help="Type of calculation you want to do.")
            self.parser.add_argument("--payment", type=int, help="What the monthly payment would be.")
            self.parser.add_argument("--principal", type=int, help="Starting Balance.")
            self.parser.add_argument("--periods", type=int, help="How many months or years you' need for repayment.")
            self.parser.add_argument("--interest", type=float, help="Interest rate.")
            self.args = self.parser.parse_args()

            if (self.args.payment or self.args.principal or self.args.periods or self.args.interest) < 0:
                print(self.error)
            else:
                if self.args.type not in ("annuity", "diff"):
                    print(self.error)
                else:
                    if self.args.type == 'diff' and self.args.payment is not None:
                        print(self.error)
                    else:
                        if self.args.interest is None:
                            print(self.error)
                        else:
                            CreditCalculator.interest(self)

                            if self.args.type == 'diff':
                                CreditCalculator.diff(self)

                            elif self.args.type == 'annuity':
                                CreditCalculator.annuity(self)

                            if (self.args.payment and self.args.periods) is not None:
                                CreditCalculator.principal(self)

                            if (self.args.principal and self.args.payment) is not None:
                                CreditCalculator.periods(self)
        else:
            print(self.error)

    def diff(self):
        self.payments = []
        for self.month in range(0, self.args.periods):
            self.month += 1
            self.payment = (self.args.principal / self.args.periods) + \
                (self.i * (self.args.principal - ((self.args.principal * (self.month - 1)) / self.args.periods)))
            self.payment = math.ceil(self.payment)
            self.payments.append(self.payment)
            print(f'Month {self.month}: paid out {self.payment}')
        print(f'\nOverpayment = {math.ceil(sum(self.payments) - self.args.principal)}')

    def annuity(self):
        if (self.args.principal and self.args.periods) is not None:
            self.annuity_payment = (self.args.principal * (self.i * ((1 + self.i) ** self.args.periods)) /
                                    (((1 + self.i) ** self.args.periods) - 1))
            self.annuity_payment = math.ceil(self.annuity_payment)
            print(f'Your annuity payment = {self.annuity_payment}!')
            print(f'Overpayment = {(self.annuity_payment * self.args.periods) - self.args.principal}')

    def principal(self):
        self.credit_principal = self.args.payment / \
                           ((self.i * ((1 + self.i) ** self.args.periods)) / (((1 + self.i) ** self.args.periods) - 1))
        self.credit_principal = math.ceil(self.credit_principal)
        print(self.credit_principal)

    def periods(self):
        self.periods_count = math.log(self.args.payment / (self.args.payment - (self.i * self.args.principal)),
                                      1 + self.i)
        self.periods_count = math.ceil(self.periods_count)
        if self.periods_count <= 12:
            print(f'You need {self.periods_count} months to repay this credit!')
        elif self.periods_count > 12 and self.periods_count % 12 == 0:
            print(f'You need {self.periods_count // 12} years to repay this credit!')
        else:
            print('You need {} years and {} months to repay this credit!'.format(
                self.periods_count // 12, self.periods_count % 12))
        print(f'Overpayment = {(self.periods_count * self.args.payment) - self.args.principal}')

    def interest(self):
        self.i = self.args.interest / (12 * 100)


credit_calculator = CreditCalculator()
credit_calculator.main()
