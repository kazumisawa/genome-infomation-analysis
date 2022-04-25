from scipy import stats
a, b, c, d = 4,0,0,4
oddsratio, pvalue = stats.fisher_exact( [ [a, b],[c, d ]] , "greater")
print(pvalue)
