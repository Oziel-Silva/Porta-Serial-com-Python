import RPi.GPIO as gpio                        
import time                                    

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)                       
while(True):
   try:
        gpio.output(18, gpio.HIGH)                     
        time.sleep(1)                                  
        gpio.output(18, gpio.LOW)                     
        time.sleep(1)                                  
   except KeyboardInterrupt:
        break
gpio.cleanup()    
print "Finished" 
                                                                              
