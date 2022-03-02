import numpy as np
from cv2 import cv2

point_list = [(((50, 50))), (((500, 40))), (((510, 520))), (((45, 515)))]

if __name__ == "__main__":
    # 获取原图像
    src = cv2.imread("/Users/lhf/PycharmProjects/Test/0301/data/xuenai.jpeg")

    # 生成一个全为0的和原图同大小的mask
    mask = np.zeros_like(src, dtype=np.uint8)
    # 把特征点的维度转成(n,1,2)，下面用list包起来，参见opencv具体参数要求
    ps = np.array(point_list)
    ps = ps.reshape(ps.shape[0], 1, -1)

    # 用填充方式把特征点围成的区域用1填充
    cv2.drawContours(mask, (ps,), 0, (1, 1, 1), -1)

    # mask和src相应位置相乘或其它方式筛选(for循环……)
    # src[np.where(mask==0)]=0
    src = src * mask

    cv2.imshow("aaa", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
