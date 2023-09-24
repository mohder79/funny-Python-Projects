from gtts import gTTS
import pygame
import requests




def tts(text = "I'm your text"):
    if requests.get("http://www.google.com", timeout=5) :

        # Create a gTTS object 
        tts = gTTS(text=text, lang='en')

        # Save the audio file
        tts.save("output.mp3")

        # Initialize pygame
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock()
    else :
      
        import winsound

        # Beep when we have conction problem
        winsound.Beep(1000, 500)  

tts('once upon a time Jesse Pinkman says:     Biatch') 

