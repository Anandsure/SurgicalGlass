import analyze as az
#import speech_trial as stt
import talk2 as tk


def get_text():
    SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"

   # text =  stt.rec()
    #text = 'can someone pass the dissection sissors?'
    text = tk.rec()
    print(text)

    keys = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,text)
    ent = az.entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,text)

    #print(keys[1])

    return [keys,ent]

if __name__ == '__main__':
    get_text()