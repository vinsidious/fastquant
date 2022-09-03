#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import standard library
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

# Import modules
import backtrader as bt

# Import from package
from fastquant.strategies.base import BaseStrategy


class DFMAStrategy(BaseStrategy):
    """
    Deviation From Moving Average (MA-n) strategy.

    Similar to the Bollinger Bands strategy but uses an absolute percentage
    deviation from the moving average instead of the standard deviation.

    Parameters
    ----------
    period : int
        Period used as basis in calculating the moving average.
    upper_limit : int
        The percentage deviation from the moving average to derive the upper
        band/crossover.
    lower_limit : int
        The percentage deviation from the moving average to derive the lower
        band/crossover.
    """

    params = (
        ("period", 20),  # period for the fast moving average
        ("upper_limit", 8),  # upper percentage deviation from the moving average
        ("lower_limit", 8),  # lower percentage deviation from the moving average
    )

    def __init__(self):
        # Initialize global variables
        super().__init__()

        # Strategy level variables
        self.period = self.params.period
        self.upper_limit = self.params.upper_limit
        self.lower_limit = self.params.lower_limit

        if self.strategy_logging:
            print("===Strategy level arguments===")
            print("period :", self.period)
            print("upper_limit :", self.upper_limit)
            print("lower_limit :", self.lower_limit)
        sma = bt.ind.SMA(period=self.period)
        self.bot = sma * (1 - self.lower_limit / 100)
        self.top = sma * (1 + self.upper_limit / 100)
        
        self.is_above = False
        self.is_below = False

    def buy_signal(self):
        was_below = self.is_below
        self.is_below = self.dataclose[0] < self.bot
        return was_below and not self.is_below

    def sell_signal(self):
        was_above = self.is_above
        self.is_above = self.dataclose[0] > self.top
        return was_above and not self.is_above
