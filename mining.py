#!/usr/bin/env python3

""" Data Mining on the prices of stock data """

__author__ = 'Anisha/Grant/Vidhya'


import json
import datetime
import operator
# Package for plotting graphs
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
# Package for GUI
import tkinter

#global variables
stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    Reads the stock data and makes call to get_monthly_averages function
    :param stock_name: string, possible values : 'GOOG' or 'TSE-SO'
    :param stock_file_name: The name of a JSON formatted file that contains stock data
    :return: none
    """
    global stock_data
    # Check if stock name is 'GOOG' or 'TSE-SO'
    if stock_name == "GOOG":
        stock_data = read_json_from_file(stock_file_name)
        get_monthly_averages(stock_data)
    elif stock_name == "TSE-SO":
        stock_data = read_json_from_file(stock_file_name)
        get_monthly_averages(stock_data)
    else:
        raise ValueError("Invalid stock name")


def get_monthly_averages(stock_info):
    """
    Calculates the monthly average prices of a stock
    :param stock_info: List with information on stock i.e date, open, high, low, close, volume
    :return: none
    """
    monthly_averages[:] = []
    year_list = []
    month_list = []

    for entry in stock_info:
        # Extracting date from stock_info
        date = datetime.datetime.strptime(entry["Date"], "%Y-%m-%d")
        if date.year not in year_list:
            year_list.append(date.year)
        if date.month not in month_list:
            month_list.append(date.month)
    for year_value in year_list:
        for month_value in month_list:
            product = 0
            sum_of_volumes = 0
            for item in stock_data:
                item_date = datetime.datetime.strptime(item["Date"], "%Y-%m-%d")
                item_year = item_date.year
                item_month = item_date.month
                if item_year == year_value:
                    if item_month == month_value:
                        # Calculating average price
                        # Step1 = (V1 * C1 + V2 * C2 + ... + Vn * Cn) where V is volume and C is close price
                        product += item["Volume"] * item["Close"]
                        # Step2 = V1 + V2 + .... + Vn
                        sum_of_volumes += item["Volume"]
            if sum_of_volumes != 0:
                    # Step3 = Step1 / Step2
                    month_average = product/sum_of_volumes
                    month_average = round(month_average, 2)
                    # Convert month value to 2 digits; ex - from 2 to 02
                    month_value = '{0:0=2d}'.format(month_value)
                    year_month = str(year_value) + "/" + str(month_value)
                    # Tuple for each month with month/year and average stock price for that month
                    month_tuple = (year_month, month_average)
                    # monthly_averages list with appended tuples
                    monthly_averages.append(month_tuple)


def six_best_months():
    """
    Determines the best six months based on monthly average stock prices
    :return: List of tuples, (month/year, monthly average)
    """
    # Sort the list monthly_averages
    monthly_averages.sort(key=operator.itemgetter(-1))
    # Reverse the list to get months with greater monthly averages
    monthly_averages.reverse()
    return monthly_averages[0:6]


def six_worst_months():
    """
    Determines the worst six months based on monthly averages
    :return: List of tuples, (month/year, monthly average)
    """
    monthly_averages.sort(key=operator.itemgetter(-1))
    return monthly_averages[0:6]


def read_json_from_file(file_name):
    """
    Reads data from a json file
    :param file_name: The name of a JSON formatted file that contains stock data
    :return: json data loaded and parsed
    """
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


def visualize(stock_name):
    """
    Creates a visualization (bar graph) for best six and worst six months for the given stock file
    :param stock_name: string, possible values : 'GOOG' or 'TSE-SO'
    :return: none
    """
    six_best = six_best_months()
    six_worst = six_worst_months()
    # Plot six best months - average monthly stock prices over time
    for i in range(len(six_best)):
        month_year, average = six_best[i]
        x_series = datetime.datetime.strptime(month_year, '%Y/%m')
        y_series = average
        plt.bar(x_series, y_series, align='center', width=10.0, color='green')
    plt.xticks(rotation=15)
    plt.title("Six Best Months for %s" % stock_name, fontsize=16)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Average Monthly Price", fontsize=14)
    # Save the graph as an image for the given stock name in the current project
    plt.savefig('Six_Best_Months_%s.png' % stock_name)
    plt.show()
    # Plot six worst months - average monthly stock prices over time
    for i in range(len(six_worst)):
        month_year, average = six_worst[i]
        x_series = datetime.datetime.strptime(month_year, '%Y/%m')
        y_series = average
        plt.bar(x_series, y_series, align='center', width=10.0, color='purple')
    plt.xticks(rotation=15)
    plt.title("Six Worst Months for %s" % stock_name, fontsize=16)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Average Monthly Price", fontsize=14)
    plt.savefig('Six_Worst_Months_%s.png' % stock_name)
    plt.show()


def gui_function():
    """

    :return: none
    """

    def invoke_function(event):
        stock_name = entry.get()
        if stock_name in ["GOOG", "goog"]:
            read_stock_data("GOOG", "data/GOOG.json")
            var1 = tkinter.StringVar()
            var1.set("Calculation of average stock price(monthly) for GOOG Json file Successful! You can proceed!")
            message = tkinter.Message(window, textvariable=var1, bg='green', fg='white')
            message.pack()
        elif stock_name == "TSE-SO":
            read_stock_data("TSE-SO", "data/TSE-SO.json")
            var1 = tkinter.StringVar()
            var1.set("Calculation of average stock price(monthly) for TSE-SO Json file Successful! You can proceed!")
            message = tkinter.Message(window, textvariable=var1, bg='green', fg='white')
            message.pack()
        else:
            var1 = tkinter.StringVar()
            var1.set("Invalid stock name. Enter a valid stock name")
            message = tkinter.Message(window, textvariable=var1, bg='green', fg='white')
            message.pack()

    def display_best(event):
        six_best_months()
        var = tkinter.StringVar()
        var.set(monthly_averages[0:6])
        frame1 = tkinter.Frame(window)
        frame1.pack()
        best_six_label = tkinter.Label(frame1, text='Best six months:')
        best_six_label.pack()
        display_message = tkinter.Message(frame1, textvariable=var, bg='blue', fg='white')
        display_message.pack()

    def display_worst(event):
        six_worst_months()
        var = tkinter.StringVar()
        var.set(monthly_averages[0:6])
        frame2 = tkinter.Frame(window)
        frame2.pack()
        worst_six_label = tkinter.Label(frame2, text='Worst six months:')
        worst_six_label.pack()
        display_message = tkinter.Message(frame2, textvariable=var, bg='red', fg='white')
        display_message.pack()

    window = tkinter.Tk()
    window.title('Assignment-3:Data Mining')
    frame = tkinter.Frame(window)
    frame.pack()
    heading = tkinter.Label(frame, text='AVERAGE STOCK PRICE CALCULATION', fg='magenta')
    heading.pack()
    label = tkinter.Label(frame, text='Enter stock name(GOOG/TSE-SO) and press Enter:')
    label.pack()
    entry = tkinter.Entry(frame)
    entry.bind('<Return>', invoke_function)
    entry.pack()
    button1 = tkinter.Button(frame, text='Best Six Months', bg='blue', fg='white')
    button1.bind('<Button>', display_best)
    button1.pack()
    button2 = tkinter.Button(frame, text='Worst Six Months', bg='red', fg='white')
    button2.bind('<Button>', display_worst)
    button2.pack()
    window.mainloop()

