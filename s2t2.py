import speech_recognition as sr
import os,time
class CustomSource(sr.Microphone):
    def init(self, device_index = None, sample_rate = 16000, chunk_size = 1024):
        print("about to initialize microphone")
        result = super(self.__class__, self).init()
        print("done initializing microphone")
        return result

class CustomRecognizer(sr.Recognizer):
    def listen(self, source, timeout = 10):
       	print("speak a valid command \n !!Caution expert pronunciation Required ")
       	print("starting listening")
       	result = super(self.__class__, self).listen(source, timeout)
       	print("done listening")
       	return result
try:
	#time.sleep(2)
	#print("                                   ")
	#print("                                   ")
	sr.Recognizer = CustomRecognizer
	sr.Microphone = CustomSource

	r = sr.Recognizer()
	with sr.Microphone(chunk_size = 512) as source:
    		audio = r.listen(source)
	user_input_command = r.recognize_google(audio)
	print (user_input_command)
	x=os.system(user_input_command)
	print (x)
	#print("you said:  " + r.recognize_google(audio))
except:
	os.system('echo " this is not a command,try again" | festival --tts')


