import time  

def focus_timer(duration):  
   print(f"Focus time started. Study for {duration} minutes.")  
   start_time = time.time()  
   while True:  
      current_time = time.time()  
      elapsed_time = current_time - start_time  
      if elapsed_time >= duration * 60:  
        print("Focus time ended. Take a break!")  
        break  
      else:  
        remaining_time = duration * 60 - elapsed_time  
        minutes = int(remaining_time // 60)  
        seconds = int(remaining_time % 60)  
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')  
        time.sleep(1)  

def break_timer(duration):  
   print(f"Break time started. Relax for {duration} minutes.")  
   start_time = time.time()  
   while True:  
      current_time = time.time()  
      elapsed_time = current_time - start_time  
      if elapsed_time >= duration * 60:  
        print("Break time ended. Get back to work!")  
        break  
      else:  
        remaining_time = duration * 60 - elapsed_time  
        minutes = int(remaining_time // 60)  
        seconds = int(remaining_time % 60)  
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')  
        time.sleep(1)  

def main():  
   focus_duration = int(input("Enter the focus duration in minutes: "))  
   break_duration = int(input("Enter the break duration in minutes: "))  
   num_sessions = int(input("Enter the number of focus sessions: "))  

   for i in range(num_sessions):  
      focus_timer(focus_duration)  
      break_timer(break_duration)  

if __name__ == "__main__":  
   main()