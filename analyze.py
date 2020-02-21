
# -*- coding: utf-8 -*-

import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"
TEXTANALYTICS_LOCATION = os.environ.get(
    "https://glasses.cognitiveservices.azure.com/", "westus2")

def key_phrases(subscription_key,text):
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_url = "https://{}.api.cognitive.microsoft.com".format(
        TEXTANALYTICS_LOCATION)
    text_analytics = TextAnalyticsClient(
        endpoint=text_analytics_url, credentials=credentials)

    try:
        documents = [
            {"id": "1", "language": "en", "text": text}
        ]

        for document in documents:
            '''print(
                #"Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))'''
        response = text_analytics.key_phrases(documents=documents)

        for document in response.documents:
            #print("Document Id: ", document.id)
            #print("\tKey Phrases:")
            x=''
            for phrase in document.key_phrases:
                x+=phrase+'\n'
                #print("\t\t", phrase)
        
        ret_list = [documents[0]['text'],x]
        
        return ret_list

    except Exception as err:
        print("Encountered exception. {}".format(err))


def sentiment(subscription_key):
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_url = "https://{}.api.cognitive.microsoft.com".format(
        TEXTANALYTICS_LOCATION)
    text_analytics = TextAnalyticsClient(
        endpoint=text_analytics_url, credentials=credentials)

    try:
        documents = [
            {"id": "1", "language": "en", "text": "I had the best day of my life."},
            {"id": "2", "language": "en",
                "text": "This was a waste of my time. The speaker put me to sleep."},
            {"id": "3", "language": "es", "text": "No tengo dinero ni nada que dar..."},
            {"id": "4", "language": "it",
                "text": "L'hotel veneziano era meraviglioso. È un bellissimo pezzo di architettura."}
        ]

        response = text_analytics.sentiment(documents=documents)
        for document in response.documents:
            print("Document Id: ", document.id, ", Sentiment Score: ",
                  "{:.2f}".format(document.score))

    except Exception as err:
        print("Encountered exception. {}".format(err))


def entity_extraction(subscription_key,text):
    """EntityExtraction.
    Extracts the entities from sentences and prints out their properties.
    """
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_url = "https://{}.api.cognitive.microsoft.com".format(
        TEXTANALYTICS_LOCATION)
    text_analytics = TextAnalyticsClient(
        endpoint=text_analytics_url, credentials=credentials)

    try:
        documents = [
            {"id": "1", "language": "en", "text": text},
        ]
        response = text_analytics.entities(documents=documents)

        for document in response.documents:
            #print("Document Id: ", document.id)
            #print("\tKey Entities:")
            #return document.entities 
            for entity in document.entities:
                print("\t\t", "NAME: ", entity.name, "\tType: ",
                      entity.type, "\tSub-type: ", entity.sub_type)
                ml = [entity.name, entity.type, entity.sub_type]
                return ml
                #for match in entity.matches:
                        #print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ","{:.2f}".format(match.entity_type_score))'''

    except Exception as err:
        print("Encountered exception. {}".format(err))
        return 0


if __name__ == "__main__":
    import sys
    import os.path

    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))

    keys = key_phrases(SUBSCRIPTION_KEY_ENV_NAME,"Someone get his blood pressure lowered.")
    ent = entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,"")
    #print(keys)
    print('input text: ',keys[0])
    print('phrases: ',keys[1])
    print(ent)