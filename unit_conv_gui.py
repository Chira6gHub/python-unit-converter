import PySimpleGUI as sg

from numpy import append

class units():
    def __init__(self, value:str):
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
            print(f"Answer : {cmtom(user_input[0])} m")
            print(f"Answer : {cmtokm(user_input[0])} km \n")
            
        elif "m" in user_input:
            print(f"Answer : {mtocm(user_input[0])} cm")
            print(f"Answer : {mtokm(user_input[0])} km \n")
            
        elif "km" in user_input:
            print(f"Answer : {kmtocm(user_input[0])} cm")
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
            window["out_put"].update(value =f"Answer : {mgtog(user_input[0])} g")
            window["out_put"].update(value = f"Answer : {mgtokg(user_input[0])} kg \n")
            
        elif "g" in user_input:
            window["out_put"].update(value = f"Answer : {gtomg(user_input[0])} g")
            window["out_put"].update(value =f"Answer : {gtokg(user_input[0])} kg \n")
        
        elif "kg" in user_input:
            print(f"Answer : {kgtomg(user_input[0])} mg")
            print(f"Answer : {kgtog(user_input[0])} g \n")
            
            
    def temp(self):
        def ctof(ui):
            return (ui * 9/5) + 32
        
        def ctoK(ui):
            return ui + 273.15
        
        def ftoc(ui):
            return ui - 32 * (5/9)
        
        def ftoK(ui):
            ui = ftoc(ui)
            return ui + 273.15
        
        def Ktoc(ui):
            return ui - 273.15
        
        def Ktof(ui):
            ui = Ktoc(ui)
            return ctof(ui)
        
        user_input = self.value.split(" ")
        user_input[0] = int(user_input[0])
        
        if "c" in user_input:
            print(f"Answer : {ctof(user_input[0])} f")
            print(f"Answer : {ctoK(user_input[0])} K \n")
            
        elif "f" in user_input:
            print(f"Answer : {ftoc(user_input[0])} c")
            print(f"Answer : {ftoK(user_input[0])} K \n")
        
        elif "K" in user_input:
            print(f"Answer : {Ktoc(user_input[0])} c")
            print(f"Answer : {Ktof(user_input[0])} f \n")
            
    def time(self):
        def mstos(ui):
            return ui / 1000

        def mstomin(ui):
            return ui / 60000

        def mstohours(ui):
            return ui / 3600000

        def mstodays(ui):
            return ui / 86400000

        def mstoweeks(ui):
            return ui / 604800000

        def stoms(ui):
            return ui * 1000

        def stomin(ui):
            return ui / 60

        def stohours(ui):
            return ui / 3600

        def stodays(ui):
            return ui / 86400

        def stoweeks(ui):
            return ui / 604800

        def mintoms(ui):
            return ui * 60000

        def mintos(ui):
            return ui * 60

        def mintohours(ui):
            return ui / 60

        def mintodays(ui):
            return ui / 1440

        def mintoweeks(ui):
            return ui / 10080

        def hourstoms(ui):
            return ui * 3600000

        def hourstos(ui):
            return ui * 3600

        def hourstomin(ui):
            return ui * 60

        def hourstodays(ui):
            return ui / 24

        def hourstoweeks(ui):
            return ui / 168

        def daystoms(ui):
            return ui * 86400000

        def daystos(ui):
            return ui * 86400

        def daystomin(ui):
            return ui * 1440

        def daystohours(ui):
            return ui * 24

        def daystoweeks(ui):
            return ui / 7

        def weekstoms(ui):
            return ui * 604800000

        def weekstos(ui):
            return ui * 604800

        def weekstomin(ui):
            return ui * 10080

        def weekstohours(ui):
            return ui * 168

        def weekstodays(ui):
            return ui * 7
        
        user_input = self.value.split(" ")
        user_input[0] = int(user_input[0])
        
        if "ms" in user_input:
            print(f"Answer: {mstos(user_input[0])} s")
            print(f"Answer: {mstomin(user_input[0])} min")
            print(f"Answer: {mstohours(user_input[0])} hours")
            print(f"Answer: {mstodays(user_input[0])} days")
            print(f"Answer: {mstoweeks(user_input[0])} weeks \n")
            
        elif "s" in user_input:
            print(f"Answer: {stoms(user_input[0])} ms")
            print(f"Answer: {stomin(user_input[0])} min")
            print(f"Answer: {stohours(user_input[0])} hours")
            print(f"Answer: {stodays(user_input[0])} days")
            print(f"Answer: {stoweeks(user_input[0])} weeks \n")
            
        elif "min" in user_input:
            print(f"Answer: {mintoms(user_input[0])} ms")
            print(f"Answer: {mintos(user_input[0])} s")
            print(f"Answer: {mintohours(user_input[0])} hours")
            print(f"Answer: {mintodays(user_input[0])} days")
            print(f"Answer: {mintoweeks(user_input[0])} weeks \n")

        elif "hours" in user_input:
            print(f"Answer: {hourstoms(user_input[0])} ms")
            print(f"Answer: {hourstos(user_input[0])} s")
            print(f"Answer: {hourstomin(user_input[0])} min")
            print(f"Answer: {hourstodays(user_input[0])} days")
            print(f"Answer: {hourstoweeks(user_input[0])} weeks \n")

        elif "days" in user_input:
            print(f"Answer: {daystoms(user_input[0])} ms")
            print(f"Answer: {daystos(user_input[0])} s")
            print(f"Answer: {daystomin(user_input[0])} min")
            print(f"Answer: {daystohours(user_input[0])} hours")
            print(f"Answer: {daystoweeks(user_input[0])} weeks \n")

        elif "weeks" in user_input:
            print(f"Answer: {weekstoms(user_input[0])} ms")
            print(f"Answer: {weekstos(user_input[0])} s")
            print(f"Answer: {weekstomin(user_input[0])} min")
            print(f"Answer: {weekstohours(user_input[0])} hours")
            print(f"Answer: {weekstodays(user_input[0])} days \n")

layout = [
    [sg.Text("Please enter the value that you want to convert a | x unit | with whitespace in the middle", background_color="black", font=("Helvatica", 20))],
    [sg.Text("Example : 100 cm", background_color="black", font=("Helvatica", 20))],
    [sg.Text("The program will automatically calculate the all possible calculations based on the unit that was given!", background_color="black", font=("Helvatica", 20))],
    [sg.Text("Enter the value : ", background_color="black", font=("Helvatica", 20)), sg.InputText(key='user_input', font=('Helvetica', 30), size=(30,1))],
    [sg.Output(size=(40, 10), key='out_put', font=('Helvetica', 20), text_color="white", background_color="black")],
    [sg.Button("Run", size=(5, 1), font=('Helvetica', 20), button_color="green"), sg.Button("Clear", size=(5, 1), font=('Helvetica', 20), button_color="Blue")]
]

window = sg.Window("Unit Conversion Calculator by Chirasthi Thennkoon", layout, background_color="black", resizable=True)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:

        break
    
    elif event == "Clear":
        window["user_input"].update( value ="")
        window["out_put"].update( value ="") 
    
    elif event == "Run":
        try:
            user_input = values["user_input"]
            converter = units(user_input)
            
            check = user_input.split(" ")
            
            if any(value in check for value in units.check_length):
                converter.length()
                
            elif any(value in check for value in units.check_liquid):
                converter.liquid()
                
            elif any(value in check for value in units.check_mass):
                converter.mass()
                
            elif any(value in check for value in units.chech_temp):
                converter.temp()
                
            elif any(value in check for value in units.check_time):
                converter.time()
            
        except ValueError as e:
            print("Enter a valid value !! {e} or Calculation not yet implemented \n")
        
    