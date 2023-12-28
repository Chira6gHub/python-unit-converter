class units():
    def __init__(self, value:str) -> None:
        #Validation
        
        
        #Assigning to self
        self.value = value
        
    check_length = ["cm", "m", "km"]
    check_liquid = ["ml", "l"]
    check_time = ["ms", "s", "min", "hours", "days", "weeks"]
    check_mass = ["mg", "g", "kg"]
    chech_temp = ["c", "f", "K"]
            
    def length(self):
        def cmtom(ui):
            return ui / 100
        
        def cmtokm(ui):
            return ui / 100000
        
        def mtocm(ui):
            return ui * 100
        
        def mtokm(ui):
            return ui / 1000
        
        def kmtocm(ui):
            return ui * 100000
        
        def kmtom(ui):
            return ui * 1000 
        
        user_input = self.value.split(" ")
        user_input[0] = int(user_input[0])
        
        if "cm" in user_input:
            print(f"Answer : {cmtom(user_input[0])} m \n")
            print(f"Answer : {cmtokm(user_input[0])} km \n")
            
        elif "m" in user_input:
            print(f"Answer : {mtocm(user_input[0])} cm \n")
            print(f"Answer : {mtokm(user_input[0])} km \n")
            
        elif "km" in user_input:
            print(f"Answer : {kmtocm(user_input[0])} cm \n")
            print(f"Answer : {kmtom(user_input[0])} m \n")
            
    def liquid(self):
        def mltol(ui):
            return ui / 1000
        
        def ltoml(ui):
            return ui * 1000
        
        user_input = self.value.split(" ")
        user_input[0] = int(user_input[0])
        
        if "ml" in user_input:
            print(f"Answer : {mltol(user_input[0])} l \n")
            
        if "l" in user_input:
            print(f"Answer : {ltoml(user_input[0])} ml \n")
            
    def mass(self):
        def mgtog(ui):
            return ui / 1000
        
        def mgtokg(ui):
            return ui / 1000000

        def gtomg(ui):
            return ui * 1000
        
        def gtokg(ui):
            return ui / 1000
        
        def kgtomg(ui):
            return ui * 1000000
        
        def kgtog(ui):
            return ui * 1000
        
        user_input = self.value.split(" ")
        user_input[0] = int(user_input[0])
        
        if "mg" in user_input:
            print(f"Answer : {mgtog(user_input[0])} g \n")
            print(f"Answer : {mgtokg(user_input[0])} kg \n")
            
        elif "g" in user_input:
            print(f"Answer : {gtomg(user_input[0])} g \n")
            print(f"Answer : {gtokg(user_input[0])} kg \n")
        
        elif "kg" in user_input:
            print(f"Answer : {kgtomg(user_input[0])} mg \n")
            print(f"Answer : {kgtog(user_input[0])} g \n")        
            
if __name__ == "__main__":
    print("Please enter the value that you want to convert a | x unit | with whitespace in the middle \n")   
    print("Example : 100 cm \n")
    print("The program will automatically calculate the all possible calculations based on the unit that was given! \n")
    
    while True:
        try:
            user_input = input("Value : ")
            converter = units(user_input)
            
            check = user_input.split(" ")
            
            if any(value in check for value in units.check_length):
                converter.length()
                
            elif any(value in check for value in units.check_liquid):
                converter.liquid()
                
            elif any(value in check for value in units.check_mass):
                converter.mass()    
            
        except ValueError:
            print("Enter a valid value !! or Calculation not yet implemented")
            
        except KeyboardInterrupt:
            print("Thank you !!")
            break
            