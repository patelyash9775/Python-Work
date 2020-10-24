from statistics import mean
from scipy import stats
Estimates=[1000,1010,1786,900,700,800,600,500,400,300,200,250,225,200,180,150,120,100,110]
Estimates.sort()
m=stats.trim_mean(Estimates,0.07)
print(m)
#tv=int(.07*len(Estimates))
#Estimates=Estimates[tv:]
#Estimates=Estimates[:len(Estimates)-tv]
#print(mean(Estimates))