class Calendar:
    def __init__ (self):
       
        self.events = []

    def book(self, start: int, end: int) -> bool:
       
        for event_start, event_end in self.events:

            if max(event_start, start) < min(event_end, end):
                return False  
        
        self.events.append((start, end))
        return True


if  __name__  ==  "__main__":
    calendar = Calendar()
    print(calendar.book(5, 10))  
    print(calendar.book(8, 13))  
    print(calendar.book(10, 15))  
