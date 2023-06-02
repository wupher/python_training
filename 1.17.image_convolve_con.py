#  -*- coding:utf-8 -*-

import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import Sequential


if __name__ == "__main__":
    A = Image.open("lena.png", 'r')
    a = np.array(A)
    height, width, channel = a.shape
    soble = np.array([0, -1, 0, -1, 5, -1, 0, -1, 0]).reshape((3, 3, 1))
    soble = np.array([soble]*3)
    print(soble.shape)
    print(soble)
    model = Sequential()
    model.add(Conv2D(filters=1, kernel_size=3, padding='same', activation='linear', input_shape=(height, width, 3)))
    model.layers[0].set_weights([soble, np.array([0.])])

    a = a.reshape((-1, ) + a.shape)
    p = model.predict(a)[0]
    feature_map = p.reshape((height, width))
    print(feature_map)
    if np.ptp(feature_map) > 0.1:
        feature_map = 255 * (feature_map - np.min(feature_map)) / np.ptp(feature_map)  # 将255改成其他值，看相应结果
    cv2.imwrite('result.png', feature_map)
