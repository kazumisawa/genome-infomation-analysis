from scipy import stats
a, b, c, d = 3,1,1,3
pearson, pvalue = stats.chisquare( [a, b],[c,d] )
print(pvalue)
