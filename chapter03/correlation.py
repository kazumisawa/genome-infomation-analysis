import numpy as np
def correlation(realData1, realData2):
    len1, len2 = len(realData1), len(realData2)
    size = len1
    if( len2 > len1 ):
        size = len2
    data1, data2 = np.zeros(size), np.zeros(size)
    for i in range(len1):
        data1[i] = realData1[i]
    for i in range(len2):
        data2[i] = realData2[i]
    tmp2 = np.fft.fft(data2).conjugate()
    tmp =  np.fft.fft(data1) * tmp2
    result =  np.fft.ifft( tmp )
    return result
