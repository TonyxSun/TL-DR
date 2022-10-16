import cohere, os
from dotenv import load_dotenv
from cohere.classify import Example

load_dotenv()

api_key = os.getenv('COHERE_KEY')
co = cohere.Client(api_key)

def generateSentiment(input):
    examples=[
        Example("The order came 5 days early", "positive"), 
        Example("The item exceeded my expectations", "positive"), 
        Example("I ordered more for my friends", "positive"), 
        Example("I would buy this again", "positive"), 
        Example("I would recommend this to others", "positive"), 
        Example("The package was damaged", "negative"), 
        Example("The order is 5 days late", "negative"), 
        Example("The order was incorrect", "negative"), 
        Example("I want to return my item", "negative"), 
        Example("The item\'s material feels low quality", "negative"), 
        Example("The product was okay", "neutral"), 
        Example("I received five items in total", "neutral"), 
        Example("I bought it from the website", "neutral"), 
        Example("I used the product this morning", "neutral"), 
        Example("The product arrived yesterday", "neutral"),
        # Example("I am having a great day", "happiness"),
        # Example("Life is fun", "happiness"),
        # Example("So excited to see it!", "happiness"),
        # Example("I am feeling down", "sadness"),
        # Example("We offer our condolances", "sadness"),
        # Example("Unfortunately, we regret to inform", "sadness"),
        # Example("What should I do?", "fear"),
        # Example("His actions posed a threat on us", "fear"),
        # Example("The boy was scared", "fear"),
        # Example("How dare they do this", "anger"),
        # Example("These actions are unacceptable", "anger"),
        # Example("I am not satisfied", "anger"),
        ]
        


    inputs=[input]

    response = co.classify(
    model='medium',
    inputs=inputs,
    examples=examples)

    return response.classifications[0]

if __name__ == '__main__':
    input = 'This item was broken when it arrived'
    res = generateSentiment(input)
    print(res)
    print(res.labels['negative'].confidence)
