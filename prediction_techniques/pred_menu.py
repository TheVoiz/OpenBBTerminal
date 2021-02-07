import config_bot as cfg
import argparse
import datetime
from datetime import datetime
from stock_market_helper_funcs import *
import config_bot as cfg
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from prediction_techniques import sma

# -----------------------------------------------------------------------------------------------------------------------
def print_prediction(s_ticker, s_start, s_interval):
    """ Print help """

    s_intraday = (f'Intraday {s_interval}', 'Daily')[s_interval == "1440min"]

    if s_start:
        print(f"\n{s_intraday} Stock: {s_ticker} (from {s_start.strftime('%Y-%m-%d')})")
    else:
        print(f"\n{s_intraday} Stock: {s_ticker}")

    print("\nPrediction Techniques:")
    print("   help        show this prediction techniques menu again")
    print("   q           quit this menu, and shows back to main menu")
    print("   quit        quit to abandon program")
    print("")
    print("   sma         simple moving average")
    print("")
 

# ---------------------------------------------------- MENU ----------------------------------------------------
def pred_menu(df_stock, s_ticker, s_start, s_interval):

    # Add list of arguments that the prediction techniques parser accepts
    pred_parser = argparse.ArgumentParser(prog='technical_analysis', add_help=False)
    pred_parser.add_argument('cmd', choices=['help', 'q', 'quit',
                                             'sma'])

    print_prediction(s_ticker, s_start, s_interval)

    # Loop forever and ever
    while True:
        # Get input command from user
        as_input = input('> ')
        
        # Parse prediction techniques command of the list of possible commands
        try:
            (ns_known_args, l_args) = pred_parser.parse_known_args(as_input.split())

        except SystemExit:
            print("The command selected doesn't exist\n")
            continue

        if ns_known_args.cmd == 'help':
            print_prediction(s_ticker, s_start, s_interval)

        elif ns_known_args.cmd == 'q':
            # Just leave the FA menu
            return False

        elif ns_known_args.cmd == 'quit':
            # Abandon the program
            return True

        # ------------------------------------------ SIMPLE MOVING AVERAGE ------------------------------------------
        elif ns_known_args.cmd == 'sma':
            sma.simple_moving_average(l_args, s_ticker, s_interval, df_stock)

        # ------------------------------------------------------------------------------------------------------------
        else:
            print("Command not recognized!")
