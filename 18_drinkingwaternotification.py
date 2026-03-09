import time
from plyer import notification
# plyer extention,notification documentaion


while True:
    print("drink some water")
    notification.notify(title="DRNIK WATER",message="You need to drink some water")
    
    time.sleep(60*60)