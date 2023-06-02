# encoding: utf-8

import numpy as np
from PIL import Image
import os
import subprocess

if __name__ == '__main__':
    image_file = 'lena.png'
    height = 100

    img = Image.open(image_file)
    print(img)
    img_width, img_height = img.size
    width = int(2 * height * img_width // img_height)    # 假定字符的高度是宽度的2倍
    img = img.resize((width, height), Image.ANTIALIAS)
    pixels = np.array(img.convert('L'))
    print('type(pixels) = ', type(pixels))
    print(pixels.shape)
    print(pixels)
    chars = "MNHQ$OC?7>!:-;. "
    N = len(chars)
    step = 256 // N
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j] // step]
        result += '\n'
    image_file_name = os.path.splitext(image_file)[0] + '.txt'
    with open(image_file_name, mode='w') as f:
        f.write(result)
    print(image_file_name + '文件生成完成。')
    # subprocess.call(['notepad', image_file_name], shell=False)
