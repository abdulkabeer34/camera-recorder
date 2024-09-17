import cv2 as cv
from time import time ,sleep
import sys
import os 



def find_counting(str:str):
    arr = list(str)
    arr.reverse()
    index = 0

    for i in arr:
        if not i.isdigit():
            break
        index += 1
        
        
    if index == 0 :
        return [1,-1]
    
    number = str[-index:]  
    
    return [int(number),index]
    

def make_dirs(path):
    try:
        if not os.path.exists(path):
            directory  =  "".join(list(os.path.split(path)[:-1]))
            os.makedirs(directory)
    except Exception as e:
        return        

def make_path(path):
    filename , extension = os.path.splitext(path)
    
    count ,index = find_counting(filename)

    filename = filename[:-index] if index  != -1 else filename[:len(filename)]
    
    newPath = f"{filename}{count}{extension}"

    while os.path.exists(newPath):     
        newPath = f"{filename}{count}{extension}"
        count += 1
        
    
    return newPath


def video_capture(duration,path):
    
    try:
        cap = cv.VideoCapture(0)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        frames  = []
        startTime = time()

        make_dirs(path)

        if os.path.exists(path):
            path = make_path(path)
        
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
                directory = os.path.splitext(path)[0].split("/")
                directory = "/".join(directory[:-1]) if len(directory[:-1]) > 1 else "/"
                print(f"image saved in {directory}")
                out.release()
                break

        cap.release()
        cv.destroyAllWindows()
    except Exception as e :
        print(f"error ===> {e}")    
       
        
def image_capture(amount,path,gap):
    cap = cv.VideoCapture(0)
            
    make_dirs(path)
        
    for i in range(amount):
        _,frame = cap.read()
        
        if os.path.exists(path):
            path = make_path(path)
            
        
        if frame is not None:
            cv.imwrite(path,frame)
            print(f"{gap} seconds delay for the next image")
            sleep(gap)
        
    if amount < 1 : 
        print("please give the postive integer")
    else:    
        directory = os.path.splitext(path)[0].split("/")
        directory = "/".join(directory[:-1]) if len(directory[:-1]) > 1 else "/"
        print(f"image saved in {directory}")
   
    
def find_value (name):
    args = sys.argv
    try:
       item = args[args.index(name) + 1]
       
       item  = int(item)
       
       return item
       
    except ValueError:
        try:
            newItem = args[args.index(name) + 1]
            return newItem 
        except:
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
        home = os.environ.get("HOME")
    
        
        if "--video" in sys.argv:
             path = default_check(f"{home}/Pictures/output.avi","--path")
             duration = default_check(10,"--duration")
             print(f"delaying for {delay} seconds")
             sleep(delay)

             video_capture(duration= duration,path = path)
        
        else :
             path = default_check(f"{home}/Pictures/images.jpeg","--path")
             amount = default_check(1,"--amount")   
             gap = default_check(0,"--gap")

             print(f"delaying for {delay} seconds")
             sleep(delay)

             image_capture(amount=amount,path = path, gap = gap)   
          
               
    except IndexError as i:
        print("please enter required arguments ")
    except Exception as e :
        print(f"error===> {e}")                 
        
