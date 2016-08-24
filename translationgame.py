import json
from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslation

languagecodes=['ar', 'en', 'es', 'fr', 'it', 'pt']

#language=random.choice(

language_translation = LanguageTranslation(username='9dd55b4f-a39c-41c8-aa44-2cc658d86b2e', password='OtrdTORKfqrU')
    
translation = language_translation.translate(text='Hello, my name is Rohit', source='en', target='ar')
#print(json.dumps(translation, indent=2, ensure_ascii=False))
print(translation)


translation = language_translation.translate(text=translation, source='ar', target='es')
print(translation)

#translation=language_translation.translate(text=translation, source='es', target='ru')

#translation=language_translation.translate(text=translation, source='ru', target='en')


