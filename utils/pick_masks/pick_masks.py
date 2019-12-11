#根据笔迹选择保留的掩膜
import cv2
def pick_masks(drawing_pick = 'drawing_pick.png', *args):
    drawing_pick = cv2.imread(drawing_pick)
    threshold = 10
    list = []
    #print(args)
    for arg in args:
        mask = cv2.imread(arg)
        [rows, cols, depth] = mask.shape
        counter = 0
        for i in range(rows - 1):
            for j in range(cols - 1):
                if mask[i, j, 0] == 255 and mask[i, j, 1] == 255 and mask[i, j, 2] == 255:
                    if drawing_pick[i, j, 0] == 255 and drawing_pick[i, j, 1] == 255 and drawing_pick[i, j, 2] == 255:
                        counter += 1
        #print(counter,arg)
        if counter >= threshold:
            list.append(arg)

    return list

if __name__ == '__main__':
    drawing_pick = 'drawing_pick.png'
    print(pick_masks(drawing_pick, 'mask1.png', 'mask2.png'))