import pyttsx3 #the packages we need to import
import PyPDF2 #the packages we need to import
engine = pyttsx3.init() #rate or speed of speaking
rate = engine.getProperty("rate")
print(rate) #prints the default rate
engine.setProperty("rate",120) #change rate
volume = engine.getProperty("volume") #volume
print("volume is{0}".format(volume)) #setting up volume level between 0 and 1 (min 0,max 1)
engine.setProperty("volume",1) #change the default volume
voices = engine.getProperty("voices") #voices
print('male voice : {0}'.format(voices[0].id)) # Male voice of index 0
print('Female voice : {0}'.format(voices[1].id)) # Female voice of index 1
engine.setProperty("voice",voices[0].id)  #setting up voice
book = open('The Epic of Gilgamesh.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(3, pages): #forloop that will start from page 2 and read pages
    page = pdfReader.getPage(3) #will get the 2nd page
    text = page.extractText() #will extract the text
    speaker.say(text)
    speaker.runAndWait()