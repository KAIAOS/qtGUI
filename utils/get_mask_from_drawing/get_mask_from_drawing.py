# 从笔迹获取笔记的掩膜
from PIL import Image
from PIL import ImageChops
import cv2

def get_drawing_mask(original = 'original.png', drawing = 'drawing.png'):
    original = Image.open(original)
    drawing = Image.open(drawing)
    diff = ImageChops.difference(original, drawing)
    #二值化
    diff = diff.convert('L')
    threshold = 10
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(255)
    diff = diff.point(table, '1')
    save_name = 'drawing_mask.png'
    diff.save(save_name)

    #return cv2.imread(save_name)

if __name__ == '__main__':
    get_drawing_mask()