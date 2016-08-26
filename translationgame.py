import json
import random
from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslation

languagecodes=['ar',  'es', 'fr', 'it', 'pt']

language_translation = LanguageTranslation(username='9dd55b4f-a39c-41c8-aa44-2cc658d86b2e', password='OtrdTORKfqrU')

prevlanguage='en'

translation=raw_input("Text to translate: ")



for i in range(10):
	language=random.choice(languagecodes)
	print language

	    
	translation = language_translation.translate(text=translation, source='en', target=language)
	print(translation)
	translation=language_translation.translate(text=translation, source=language, target='en')
	print(translation)
	
	prevlanguage=language

#finaltranslation=language_translation.translate(text=translation, source=prevlanguage, target='en')
#print(finaltranslation)


