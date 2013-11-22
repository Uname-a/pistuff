x=1
y=2
import time

while x< y:
    x = x+15
    
    time.sleep(1)
    if x < y:
        print('e')
        break
    x = x+15
    
    time.sleep(1)
    
    if x<y:
        print('e')
        break
    x = x+15
    
    time.sleep(1)
    if x<y:
        print('e')
        break
else:
    print('D')
