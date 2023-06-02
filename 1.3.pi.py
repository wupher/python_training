# coding:utf-8

import numpy as np

if __name__ == '__main__':
    print(np.sqrt(6 * np.sum(1 / (np.arange(1, 10000) ** 2))))
    print(np.sum(1 / np.arange(1, 20).cumprod()) + 1)
