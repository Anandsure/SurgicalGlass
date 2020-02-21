import analyze as az
import speech_trial as stt
SUBSCRIPTION_KEY_ENV_NAME = "bc20ced3c3014badbf34d1799e28f2a2"

text =  stt.rec()
print(text)

keys = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,text)
    #print(keys)

#ent = az.entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,text)
#print(ent)
print('input text: ',keys[0])
print('phrases: ',keys[1])