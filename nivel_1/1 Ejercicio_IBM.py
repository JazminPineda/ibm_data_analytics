import collections
import re, string

class analysedText(object):

    def __init__(self, text):
        self.textMinusc = self.to_lower_case(text)
        self.fmtText = self.remove_signos()
        self.dicionario = self.freqAll()
   

    def to_lower_case(self, text):
        return text.lower()
        
    def remove_signos(self):
        lista_signos = [ ",", ".", "?","!", ":", ";"]
        
        for signo in lista_signos:
            self.textMinusc = self.textMinusc.replace(signo, "")           
        return self.textMinusc 
            
        
    def freqAll(self):
        diccionario = {}
        for palabra in self.fmtText.split(" "):     
            if palabra not in diccionario.keys():
                diccionario[palabra] = 1
            else:
                diccionario[palabra] += 1
        return diccionario         
        # print(collections.Counter(text.split(" ")))
        
    def freqOf(self, palabra):
        return self.dicionario[palabra]
       
       
    
        
def main():
    text =   analysedText('''Title Goes Here  Bolded Text  Title Goes Here  Bolded Text be here!
    I run. Title Goes Here  Bolded Text ?
    I talked. She was talking. They talked to them about running. Who ran to the talking runner?
    ¡Sebastián, Nicolás, Alejandro and Jéronimo are going to the store tomorrow morning!
    something... is! wrong() with.,; this :: sentence.
    I cannot do this anymore. I did not know them. Why could not you have dinner at the restaurant''')
    
    palabra = input("Ingresa la palabra: ")
    print(text.freqOf(palabra=palabra))


if __name__ == "__main__":
    main()
    