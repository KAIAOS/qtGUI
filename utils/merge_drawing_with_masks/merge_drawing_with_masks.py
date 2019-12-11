#合并笔迹与人像掩膜
import cv2
import matplotlib.pyplot as plt

def merge(drawing_mask = None, *args):
    mask = cv2.imread(args[0])
    if drawing_mask is not None:
        drawing_mask = cv2.imread(drawing_mask)
        [rows, cols, depth] = drawing_mask.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                if drawing_mask[i, j, 0] == 255 and drawing_mask[i, j, 1] == 255 and drawing_mask[i, j, 2] == 255:
                    mask[i, j, 0] = 255
                    mask[i, j, 1] = 255
                    mask[i, j, 2] = 255

    for i, arg in enumerate(args):
        if i == 0:
            continue
        mask_i = cv2.imread(arg)
        [rows, cols, depth] = mask_i.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                if mask_i[i, j, 0] == 255 and mask_i[i, j, 1] == 255 and mask_i[i, j, 2] == 255:
                    mask[i, j, 0] = 255
                    mask[i, j, 1] = 255
                    mask[i, j, 2] = 255
    cv2.imwrite('merged_mask.png', mask)

    #return

if __name__ == '__main__':
    drawing_mask = 'drawing_mask.png'
    merge('mask1.png','mask2.png')