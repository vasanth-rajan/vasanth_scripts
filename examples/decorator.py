class example(object):
    
    def outerFunc(*args, **kwargs):
 
       print *args, **kwargs

    @outerFunc
    def funcVar(a=7):
#        self.a = a 
#        print self.a
        return a

 
a = example()
a.funcVar(5)
