# replace wlp2s0 with preferred network adapter (example: replace wlp2s0 with enp3s0)
import os
from random import randint
a=str(randint(1000, 9999))
b=str(randint(1000, 9999))
c=str(randint(10, 99 ))
e=(f"00:{a[0]+a[1]}:{b[2:]}:{b[0]+b[1]}:{a[2:]}:{c}") #RANDOM MAC ADDRESS
de="sudo ifconfig wlp2s0 down" #DISABLES WLP2S0
ce=m=(f"sudo ifconfig wlp2s0 hw ether {e}") #CHANGES MAC ADDRESS TO RANDOM
ee="sudo ifconfig wlp2s0 up" #ENABLES WLP2S0
os.system(de)
os.system(ce)
os.system(ee)
