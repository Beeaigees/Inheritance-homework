from modules.TextProcessor import Textprocessor

class caesar(Textprocessor):
    def __init__(self, text, meter):
        super().__init__(text)
        self.__meter = meter

    def get_meter(self):
        return self.__meter

    def encryption(self):
        text = self.get_text()
        meter = self.get_meter()
        hasil = ""

        for char in text:
            if char == " ":
                hasil += " "
            elif char == char.upper():    
                hasil += chr((ord(char) - 65 + (meter)) % 26 + 65) #ini buat huruf kapital
            else:
                hasil += chr((ord(char) - 97 + (meter)) % 26 + 97) #ini buat yang gak kapital
        
        print(hasil)