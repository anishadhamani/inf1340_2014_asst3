#!/usr/bin/env python3

""" Docstring """

__author__ = 'Anisha/Grant/Vidhya'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

import json
import datetime
import operator

stock_data = []
monthly_averages = []
year_list = []
month_list = []
month_tuple = ()


def read_stock_data(stock_name, stock_file_name):
    stock_data = read_json_from_file(stock_file_name)
    for entry in stock_data:
        date = datetime.datetime.strptime(entry["Date"], "%Y-%m-%d")
        if date.year not in year_list:
            year_list.append(date.year)
        if date.month not in month_list:
            month_list.append(date.month)
    print(year_list)
    print(month_list)
    for year_value in year_list:
            for month_value in month_list:
                month_average = 0
                product = 0
                sum_of_volumes = 0
                for item in stock_data:
                    item_date = datetime.datetime.strptime(item["Date"], "%Y-%m-%d")
                    item_year = item_date.year
                    item_month = item_date.month
                    if item_year == year_value:
                        if item_month == month_value:
                            product += item["Volume"] * item["Close"]
                            sum_of_volumes += item["Volume"]
                if sum_of_volumes != 0:
                        month_average = product/ sum_of_volumes
                        month_average = round(month_average,2)
                        month_value = '{0:0=2d}'.format(month_value)
                        year_month = str(year_value) + "/" + str(month_value)
                        month_tuple = (year_month,month_average)
                        monthly_averages.append(month_tuple)


def six_best_months():
    monthly_averages.sort(key=operator.itemgetter(-1))
    monthly_averages.reverse()
    print("Best six months: ", monthly_averages[0:6])
    return monthly_averages[0:6]


def six_worst_months():
    monthly_averages.sort(key=operator.itemgetter(-1))
    print("Worst six months: ", monthly_averages[0:6])
    return monthly_averages[0:6]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

