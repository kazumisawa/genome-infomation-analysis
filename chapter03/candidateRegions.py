import windowScore
import overThreshold
import connect
import bunkatsu
import bunkatsuScore
import positionAndScore

def regions(peak, pv1, pv2):
    region = []
    for lag in peak:
        x = windowScore.windowScore(lag, pv1, pv2, 30)
        y= overThreshold.overThreshold(x, 100)
        if len(y) > 0:
            z = connect.connect(y)
            a = bunkatsu.bunkatsu(z)
            b = bunkatsuScore.bunkatsuScore(a, x)
            if len(b) > 0:
                t = positionAndScore.positionAndScore(lag, b)
                for subregion in t:
                    region.append(subregion)
    return region
