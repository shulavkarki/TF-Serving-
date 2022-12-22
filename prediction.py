import requests, pickle
# from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
def predictions(url:str, text:list, tokenizer):
    """
    It takes a URL, a list of text, and a tokenizer, and returns the response from the TensorFlow
    Serving server
    
    :param url: The URL of the TensorFlow Serving server
    :type url: str
    :param text: list of strings to be sent to the model for inference
    :type text: list
    :param tokenizer: the tokenizer object that was used to train the model
    :return: The response is a JSON object that contains the prediction results.
    """
    # Send the request to the TensorFlow Serving server
    inference_sent = tokenizer.texts_to_sequences(text)
    testing_padded = pad_sequences(inference_sent, maxlen=120)
    data = {"instances": testing_padded.tolist()}

    response =  requests.post(url, json=data)
    return response.content
    
# Print the response
# print(response.json())
if __name__=="__main__":
    print('Checking....')
    sentences = []
    tokenizer = None
    URL = "http://localhost:8501/v1/models/saved_model:predict"
    with open('tokenizer.pickle', 'rb') as handle:
        print('loading pickle')
        tokenizer = pickle.load(handle)
        print('loaded pickle')

    while True:
    # Prompt the user to enter a sentence
        sentence = input("Enter the reviews (or 'q' to quit): ")

        # Check if the user wants to quit
        if sentence.lower() == 'q':
            break

        # Add the sentence to the list
        sentences.append(sentence)
    print(sentences)
    print(predictions(URL, sentences, tokenizer))