import pandas as pd
from scipy import stats
from numpy import mean

data1 = [4,6,17,16,8,9]        # 관측치
data2 = [10,10,10,10,10,10]    # 기대치
chis = stats.chisquare(data1, data2)
print("statistic = %.3f, pvalue = %.3f" % chis)


# 한 집단 평균 검정
one_sample = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]
print(mean(one_sample) )  # 177.96
result = stats.ttest_1samp(one_sample, 175.6)   # 비교집단, 관측치

print('t검정 통계량 = %.3f, pvalue = %.3f'%(result))

# 두 집단 평균 검정

female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]
result = stats.ttest_ind(male, female)

print("t검정 통계량: %.3f, pvalue=%.3f"%(result))


# Before, After 두 집단 평균 검정

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
paired_sample = stats.ttest_rel(baseline, follow_up)

print('t검정 통계량 = %.3f, pvalue = %.3f'% paired_sample)



