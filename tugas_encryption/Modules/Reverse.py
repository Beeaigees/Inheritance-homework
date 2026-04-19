from modules.TextProcessor import Textprocessor

class reverse(Textprocessor):
    def __init__(self, text):
        super().__init__(text)
    
    def reverse(self):
        kalimat = input("Masukkan kalimat yang mau dibalik: ")
        list_kata = kalimat.split()

        output = " ".join([kata[::-1] for kata in list_kata])
    print(f"Hasil: {output.upper()}")