class faba:
    def __init__(self,end):
        self.start=0
        self.s=1
        self.end=end
        self.e=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.e<=self.end:
            f=self.start
            self.start=self.s
            self.s=self.start+f
            self.e+=1
            return f
        
        raise 'stopIteration'
i=iter(faba(5))
while True:
    print(next(i))