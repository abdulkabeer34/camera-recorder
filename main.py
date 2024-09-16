import cv2 as cv
from time import time ,sleep
import sys


def video_capture(duration,path):
    
    try:
        cap = cv.VideoCapture(0)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        frames  = []
        startTime = time()
        
        print(f'recording video for {duration} seconds ')
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frames.append(frame)

            if time() - startTime > duration:
                out = cv.VideoWriter(path, fourcc, 20.0, (640,  480))
                for _frame in frames:
                  out.write(_frame)
                out.release()
                break

        
        cap.release()
        cv.destroyAllWindows()
    except Exception as e :
        print(f"error ===> {e}")    
        
        
def image_capture(amount,path):
    cap = cv.VideoCapture(0)
     
    if amount > 1 :  
        for i in range(amount):
            _,frame = cap.read()
            
            paths = path.split(".")
            
            if frame is not None:
                cv.imwrite(f"{paths[0]}{i}.{paths[1]}",frame)
    elif amount == 1 :
        _,frame = cap.read()
        cv.imwrite(path,frame)
    
    if amount < 1 : 
        print("please give the postive integer")
    else:    
        print(f"{amount} image captured")  

    
    
    
def find_value (name):
    args = sys.argv
    try:
       item = args[args.index(name) + 1]
       
       item  = int(item)
       
       return item
       
    except ValueError:
        return None 
    
    except Exception as e :
       return None
            
 
def default_check (defaultValue , path):
    res  = find_value(path) 
    res = defaultValue if  res == None else res 
    
    return res
                 
if __name__ == "__main__":
    try:
        delay = default_check(0,"--delay")
        

                
        print(f"delaying for {delay} seconds")
        sleep(delay)
        
        if "--video" in sys.argv:
             path = default_check("output.avi","--path")
             duration = default_check(10,"--duration")

             video_capture(duration= duration,path = path)
        
        elif "--image" in sys.argv:
             path = default_check("images.jpeg","--path")
             amount = default_check(1,"--amount")   

             image_capture(amount=amount,path = path)   
         
        else:
            print("please define the type")     
               
    except IndexError as i:
        print("please enter required arguments ")
    except Exception as e :
        print(f"error===> {e}")                 
        
