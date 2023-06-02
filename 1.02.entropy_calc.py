# coding: utf-8
# @Time: 2020/9/17 16:50
# @Author: zou wei
# @File: 1.02.entropy_calc.py
# @Contact: visio@163.com
# @Software: PyCharm

import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    eps = 1e-6
    N = 10000
    r1 = np.random.normal(0, 10, N).astype(np.int64)
    r2 = np.random.normal(0, 8, N).astype(np.int64)
    r3 = np.random.uniform(r1.min(), r1.max(), N).astype(np.int64)
    p1 = pd.value_counts(r1) / len(r1)
    p2 = pd.value_counts(r2) / len(r2)
    p3 = pd.value_counts(r3) / len(r3)
    print(p1)
    print(p2)
    print(p3)
    p = pd.DataFrame([p1, p2, p3]).T
    p.fillna(0, inplace=True)
    print(p)
    p += eps
    # p.plot()
    # plt.show()
    h0 = -np.sum(p[0] * np.log2(p[0]))
    h1 = -np.sum(p[1] * np.log2(p[1]))
    h2 = -np.sum(p[2] * np.log2(p[2]))
    kl_01 = h0 - np.sum(p[0] * np.log2(p[1]))
    kl_02 = h0 - np.sum(p[0] * np.log2(p[2]))
    print(h0, h1, h2)
    print(kl_01, kl_02)

    plog = np.log2(p)
    h = np.sum(p * plog, axis=0)
    print(h)
