#!/usr/bin/env python3

""" Module to test mining.py """

__author__ = 'Anisha/Grant/Vidhya'

import pytest
from mining import *


def test_goog():
    # test for GOOG json file
    # function call to read stock data and calculate monthly average stock prices
    read_stock_data("GOOG", "data/GOOG.json")
    # test for best six months
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                 ('2008/05', 576.29), ('2008/06', 555.34)]
    # test for worst six months
    assert six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09),
                                  ('2004/12', 181.01), ('2005/03', 181.18)]
    # test for visualization
    visualize("GOOG")


def test_tse_so():
    # test for TSE-SO json file
    # function call to read stock data and calculate monthly average stock prices
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    # test for six best months
    assert six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96), ('2013/06', 19.94),
                                 ('2013/04', 19.65), ('2007/10', 19.11)]
    # test for six worst months
    assert six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41),
                                  ('2009/04', 2.75), ('2009/01', 3.14)]
    # test for visualization
    visualize("TSE-SO")


def test_gui():
    # test for graphical user interface
    gui_function()


def test_files():
    # file not found test cases
    with pytest.raises(FileNotFoundError):
        read_stock_data("GOOG", "GOOG.json")

    # invalid stock name test case
    with pytest.raises(ValueError):
        read_stock_data("ABC", "abc.json")
        read_stock_data("", "goog.json")
