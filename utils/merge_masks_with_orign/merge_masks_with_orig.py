import cv2

def merge(orig = 'original.png', *args):
    orig = cv2.imread(orig)

    for arg in args:
        mask = cv2.imread(arg)
        [rows, cols, depth] = mask.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                if mask[i, j, 0] == 255 and mask[i, j, 1] == 255 and mask[i, j, 2] == 255:
                    orig[i, j, 0] = 255
                    orig[i, j, 1] = 255
                    orig[i, j, 2] = 255

    cv2.imwrite('merged_masks_with_orig.png', orig)

    #return
if __name__ == '__main__':
    merge('original.png','mask1.png','mask2.png')