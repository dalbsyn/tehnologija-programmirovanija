# 5 вариант
class Device:
    def _init_(self, name, buttery_life):
        self.__name = name
        self.__buttery_life = buttery_life

    def get_name(self):
        return self.__name
       
    def get_buttery_life(self):
        return self.__buttery_life
        
    def set_buttery_life(self, name, buttery_life):
        self.__buttery_life = buttery_life

#2
class Smartphone(Device):
    def call(self):
        print("Телефон звонит")
    def compile_code(self):
        print("Ноутбук компилирует код")   
    def draw(self):
        print("Планшет используется для рисования")    
      
              
        
                  
                  