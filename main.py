from Classes import Mortgage, MortgageCashflows
from MortgageCFengine import calculate_single_mtge_cash
from PVandYIELDS import pv_mtg_cash_flows, calc_mtg_yield
from Read_write_csv import print_mortgage_results, print_mortgage_results_v2
import pandas as pd


def main():
    # Define a mortgage cashflow class object to aggregate all loans' cashflows
    # aggregate = MortgageCashflows()
    # define file name and location of the loan data to import
    csv_file_mortgage_attributes = '/Users/michaelaneiro/Downloads/mortgage_attributes.csv'  # MacBook
    # use pandas function to read csv into a dataframe
    df = pd.read_csv(csv_file_mortgage_attributes)

    # Iterate through the rows of the dataframe into a list variable to run mortgage analytics
    rows = len(df)

    for r in range(rows):
        ml = df.iloc[r].tolist()  # mortgage_list row number count starts at 0
        # create an object of a class 'Mortgage', passing in the variables defining the mortgage
        m = Mortgage(ml[0], ml[1], ml[2], ml[3], ml[4], ml[5], ml[6], ml[7], ml[8], ml[9], ml[10], ml[11], ml[12],
                     ml[13],
                     ml[14], ml[15], ml[16], ml[17], ml[18], ml[19], ml[20], ml[21], ml[22], ml[23], ml[24], ml[25],
                     ml[26],
                     ml[27], ml[28], ml[29], ml[30], ml[31])
        calculate_single_mtge_cash(m)
        m.accrued_interest = m.net_rate / 12 * (m.settle_day - 1) / 30 * 100
        m.price = pv_mtg_cash_flows(m, m.BEY) / m.balance * 100
        print_mortgage_results_v2(m, r)

        print('Loan id   Price   Accrued   Value')
        print(m.loan_id, "  ", round(m.price - m.accrued_interest, 2), " ", round(m.accrued_interest, 2), "   ", round(m.price, 2))
        print("BEY = ", round(calc_mtg_yield(m), 3))
        print()

    return


main()
