import numpy as np
from datetime import datetime 

def process(a):
    # convert fahrenheit to celsius
    t = []
    for x in a:
        t.append((x-32)*5/9)
    return t

def do_calcs(tmp, p):
    # calculate vapor pressure from clausius clapeyron approximation
    vp = []
    for i in range(len(tmp)):
        x = (17.625 * tmp[i])/(tmp[i] + 243.04)
        v = 6.1094 * np.exp(x)
        vp.append(v)
    
    # calculate relative humidity
    rh = []
    for j in range(len(vp)):
        h = (vp[j]/p[j])*100
        rh.append(h)
    return rh

t_data = [75.2, 77.8, 80.1, 82.4, 85.5, 83.2, 81.9, 79.5]
p_data = [1013.25, 1013.1, 1012.8, 1012.5, 1012.0, 1012.2, 1012.6, 1012.9]

# process temps
result1 = process(t_data)

# do humidity calcs
final = do_calcs(result1, p_data)

# print results
print("Results for " + str(datetime.now()))
for k in range(len(final)):
    print(f"Hour {k}: {final[k]:.1f}%")
