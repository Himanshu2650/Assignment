from typing import Dict

class FuelStation:
    def  __init__ (self, diesel: int, petrol: int, electric: int):
        self.slots_capacity: Dict[str, int] = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.slots_occupied: Dict[str, int] = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:

        if fuel_type not in self.slots_capacity:
            return False 
        
        if self.slots_occupied[fuel_type] < self.slots_capacity[fuel_type]:
            self.slots_occupied[fuel_type] += 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:

        if fuel_type not in self.slots_capacity:
            return False 
        
        if self.slots_occupied[fuel_type] > 0:
            self.slots_occupied[fuel_type] -= 1
            return True
        return False

if  __name__  ==  "__main__":
    fuel_station = FuelStation (diesel=2, petrol=2, electric=1)
    print(fuel_station.fuel_vehicle("diesel"))  
    print(fuel_station.fuel_vehicle("petrol"))  
    print(fuel_station.fuel_vehicle("diesel"))  
    print(fuel_station.fuel_vehicle("electric"))  
    print(fuel_station.fuel_vehicle("diesel"))  
    print(fuel_station.open_fuel_slot("diesel")) 
    print(fuel_station.fuel_vehicle("diesel")) 
    print(fuel_station.open_fuel_slot("electric"))  
    print(fuel_station.open_fuel_slot("electric"))  
