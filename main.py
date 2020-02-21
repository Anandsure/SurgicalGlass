import analyze as az
#import speech_trial as stt

def get_text():
    SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"

   # text =  stt.rec()
    text = 'akshat is a faggot'
    print(text)

    keys = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,text)
    ent = az.entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,text)

    #print(ent)
    #print('input text: ',keys[0])
    #print('phrases: ',keys[1])
    return [keys,ent]