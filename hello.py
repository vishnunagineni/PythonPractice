class Hello:
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print(f"Welcoming {self.name} by Jenkins")
    
h=Hello("Vishnu")
h.greet()