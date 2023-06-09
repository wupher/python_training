# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # stock_max, stock_min, stock_close, stock_amount = np.loadtxt('SZ000725.txt', delimiter='\t', skiprows=2, usecols=(2, 3, 4, 5), unpack=True)
    data = pd.read_excel('600519.xlsx')
    stock_close = data['收盘'].values
    N = 200
    stock_close = stock_close[-N:]
    print(stock_close)

    n = 30
    weight = np.ones(n)
    weight /= weight.sum()
    print('卷积核：', weight)
    stock_sma = np.convolve(stock_close, weight, mode='valid')  # simple moving average
    print('输入数据维度：', stock_close.shape)
    print('输出数据维度：', stock_sma.shape)

    weight = np.linspace(1, 0, n)
    print('np.linspace(1, 0, n):', weight)
    # weight = np.linspace(0, 1, n)
    weight = np.exp(weight)
    weight /= weight.sum()
    print(weight)
    stock_ema = np.convolve(stock_close, weight, mode='valid')  # exponential moving average

    t = np.arange(n-1, N)
    poly = np.polyfit(t, stock_ema, 5)
    print(poly)
    t = np.arange(n-1, N)
    stock_ema_hat = np.polyval(poly, t)

    mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(facecolor='w')
    plt.plot(np.arange(N), stock_close, 'ro-', linewidth=2, label='原始收盘价', mec='k')
    t = np.arange(n-1, N)
    plt.plot(t, stock_sma, 'b+-', linewidth=2, label='简单移动平均线')
    plt.plot(t, stock_ema, 'g-', linewidth=2, label='指数移动平均线')
    plt.legend(loc='upper right')
    plt.title('股票收盘价与滑动平均线MA', fontsize=15)
    plt.grid(True, ls=':', color='#404040')
    plt.show()

    print(plt.figure(figsize=(7, 5), facecolor='w'))
    plt.plot(np.arange(N), stock_close, 'ro-', linewidth=1, label='原始收盘价', mec='k')
    plt.plot(t, stock_ema_hat, '-', color='#4040FF', linewidth=3, label='指数移动平均线估计')
    plt.plot(t, stock_ema, 'g-', linewidth=2, label='指数移动平均线')
    plt.legend(loc='upper right')
    plt.title('滑动平均线MA的估计', fontsize=15)
    plt.grid(True, ls=':', color='#404040')
    plt.show()
