import pyttsx3
from PyPDF2 import PdfReader

reader = PdfReader('book.pdf')
number_of_pages = len(reader.pages)
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

for page in range(number_of_pages):
    folha = reader.pages[page+7]
    texto = folha.extract_text()
    print(texto)
    speaker.say(texto)
    speaker.runAndWait()

print("Livro Completo")
