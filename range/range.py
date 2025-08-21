class Range:
    def __init__(self, start=0, stop=None, step=1):

        if isinstance(start, (int,str)) and isinstance(stop, (int, str,type(None))) and isinstance(step, (int,str)):
            start, stop, step = self._validation(start, stop, step)
            self._start,  self._stop, self._step  = start, stop, step    

        elif isinstance(start, Range):
            self._start, self._stop, self._step = start._start, start._stop, start._step

        else:
            raise TypeError("start, step, and stop must be digit")


    def _start_validation(self, start):
        if isinstance(start, str):
            if start.lstrip("-+").isdigit():
             return int(start)
            raise ValueError("start value must be digit")
        return start
    
    def _stop_validation(self, stop):
        
        if isinstance(stop, str):
            if stop.lstrip("-+").isdigit():
             return int(stop)
            raise ValueError("stop value must be digit")
        return stop
    
    def _step_validation(self, step):
        if isinstance(step, str):
            if step.lstrip("-+").isdigit():
             step = int(step)
            else:
             raise ValueError("step value must be digit")
        if step == 0:   
           raise ValueError("step must be non-0") 
        return step
    
        
    def _validation(self, start, stop, step):
       if stop is None:
          value = start
          stop = value
          start = 0
       start = self._start_validation(start) 
       stop = self._stop_validation(stop)
       step = self._step_validation(step)  
       return start, stop, step

    @property
    def start(self):
     return self._start

    @property
    def stop(self):
     return self._stop

    @property
    def step(self):
     return self._step

    @start.setter
    def start(self, value):
     self._start = self._start_validation(value)

    @stop.setter
    def stop(self, value):
     self._stop = self._stop_validation(value)

    @step.setter
    def step(self, value):
     self._step = self._step_validation(value)

    def __len__(self):
       if self._step > 0:
          return max(0, (self._stop - self._start + self.step -1) // self._step) 
       return max(0, (self._stop - self._start + self._step + 1) // self._step)
    
    def __getitem__(self, j):
       if j < 0:
            j += len(self)
       if not 0 <= j < len(self):
          raise IndexError("index out of range")
       return self._start + j * self._step 
    
    def __str__(self):
       return f"<{self._start} , {self._stop}, {self._step} >"
          




          

    






    

          


            
        
        
          
        
          

        