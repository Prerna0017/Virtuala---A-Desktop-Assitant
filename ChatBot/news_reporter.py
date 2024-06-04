import json, requests, pyttsx3

def speak(str):
	engine = pyttsx3.init()
	voice = engine.getProperty('voices')
	engine.setProperty('voice', voice[1].id)
	engine.say(str)
	engine.runAndWait() 
	
def getnews():
	url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=48cc2d4e42274d6f8251e024897de651"
	news = requests.get(url).text
	news_dict = json.loads(news)
	arts = news_dict['articles']
	
	a = 1
	n = 5

	speak("Today's news highlights are...")
	for article in arts:
		print(article['title'])
		speak(article['title'])
		if a==n:
			break
		else:
			speak("Moving on to the next news.")
			a += 1
			# continue

	speak("Thanks for listening...")

# getnews()