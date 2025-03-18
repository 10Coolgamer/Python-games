class Dog:
    
    attr1="mammal"
    attr2="dog"
    
    def fun(self):
        print("I am a", self.attr1)
        print("I am a", self.attr2)
        
Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()

Puff = Dog()

print(Puff.attr1)
Puff.fun()