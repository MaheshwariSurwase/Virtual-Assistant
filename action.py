import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action (data):
    user_data = data.lower()
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
    
    elif "i love you my dear assistant" in user_data:
        text_to_speech.text_to_speech("i love you too my dear maheshwari i want to spend whole life with you and i miss you dear mahi")
        return "i love you too my dear maheshwari i want to spend whole life with you and i miss you dear maheshwari"
    
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey, sir How I can help you")
        return "hey, sir How I can help you"
        
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
        
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + " Hour:" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
        
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    
    
        
    elif "play music" in user_data:
        webbrowser.open("https://www.jiosaavn.com/featured/timeless-ghazals/Kdb2rW52fiE_")
        text_to_speech.text_to_speech("jiosaavn.com is now ready for you")
        return "jiosaavn.com is now ready for you"
        
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
        
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"
        
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
        
    
    else :
         text_to_speech.text_to_speech("I am not able to understand")
         return "I am not able to understand"