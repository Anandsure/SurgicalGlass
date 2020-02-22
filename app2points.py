import analyze as az

#text comes in as an input from the api.
SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"
f=0

text = '''
Keep blood pressure lower than 80 mmHg.
patient has a busted vain in the right arm.
have to ensure unconsious anesthesia levels.
patient has a weak spine and is anemic.
'''
extract=''
x=[]
for i in text:
    if i != '\n':
        extract+=i
    else:
        phrases = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,extract)
        if phrases:
            print(phrases[1])
            extract=''