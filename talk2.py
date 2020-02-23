import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "008eed6eb82346a7a07ac66369b076bf", "centralindia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

def rec():
    print("Say something...")
    result = speech_recognizer.recognize_once()
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        #print("Recognized: {}".format(result.text))
        z = ''
        for i in result.text:
            if i != '.':
                z+=i
            else:
                continue

        return z
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return 0
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))

        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            return 0

if __name__ == '__main__':
    text=  rec()
    print(text)