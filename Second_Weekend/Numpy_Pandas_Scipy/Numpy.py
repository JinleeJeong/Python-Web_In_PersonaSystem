import numpy as np
import zarr
import pandas as pd
import matplotlib.pyplot as plot


# data = numpy.random.randn(3,4) # 3_row 4_col
# # # print(data)
# # #
# # # print(data+data)
# #
# # list1 = [3, 5.6, 5, 8, 9.5] # 리스트(배열)을 통한 값 즉시 계산 가능
# # arr1 = numpy.array(list1)
# #
# # list2 = [ [1,2,3,4,5], [6,7,8,9,10 ] ]
# # arr2 = numpy.array(list2)
# #
# # print("합계: ", arr1.sum())         #합계:  31.1
# # print("최대값: ", arr1.max())       #최대값:  9.5
# # print("최소값: ", arr1.min())       #최소값:  3.0
# # print("분산: ", arr1.var())         #분산:  5.2336
# # print("표준편차: ", arr1.std())      #표준편차:  2.28770627485
# #
# # print(arr2 * 2 , '\n')
# #
# # arr_1 = numpy.zeros((3,5)) # ones / eye > 단위행렬
# # print(arr_1)
#
# x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # numpy 배열
# print(x)
# frame = pd.DataFrame(np.arange(12).reshape((3,4)), columns=['a','b','c','d']) # DataFrame -> arange 순서 숫자 input
# print(frame)
# print(frame.a)
# plot.plot(frame)
# plot.show()

vector_set = []
for i in range(100) :                          # 0~99
    x = np.random.normal(0,1)                  # normal(평균, 표준편차) : 표준정규분포
    y = x * 0.1 + 0.2 + np.random.normal(0,1)
    vector_set.append([x, y])                  # [[x1, y1], [x2, y2], [x3, y3], ... ,[x100, y100]]

x_data = [ v[0]  for v in vector_set ]      # v = [x1, ]
y_data = [ v[1]  for v in vector_set ]      # v = [, y1]


plot.plot(x_data, y_data, 'ro')
plot.show()
# =================================# // 시각화 + 차트 4개 동시 생성 가능
# flg = plot.figure()               # 차트 플롯 생성
# x1 = flg.add_subplot(2, 2, 1)    # 행, 열, 위치
# x2 = flg.add_subplot(2, 2, 2)
# x3 = flg.add_subplot(2, 2, 3)
# x4 = flg.add_subplot(2, 2, 4)
#
#
#
# data2  = np.random.randint(1, 100, 100)    # randint(start, end, size) 난수 정수 발생
#
#
# x1.hist(data2)
#
# x2.scatter(x_data, y_data)
#
# x3.plot(np.arange(50))
#
# x4.plot(np.random.rand(100), 'k--')
# plot.show()
