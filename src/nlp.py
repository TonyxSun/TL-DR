import cohere
import os
from dotenv import load_dotenv
from cohere.classify import Example

load_dotenv()

def checkLength(input):
    len_count = len(input.split(" "))
    if len_count > 510:
        input = " ".join(input.split(" ")[0:170])
    max_token_len = len_count/3
    if len_count < 40:
        max_token_len = 10
    
    len_count = len(input.split(" "))
    return (input, max_token_len)

# return tldr text
def generateSummery(co, input):
    # (input, max_tokens) = checkLength(input)
    learning_prompt = '''
  Passage: 
  Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn’t the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to “the dusty section of the dictionary” to find its latest words.\n\nTLDR: Wordle has not gotten more difficult to solve.\n--\nPassage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.\n\nTLDR: ArtificialIvan has raised $190 million in Series C funding.\n--\n
  '''
    prompt = f"{learning_prompt}Passage: {input}\n\nTLDR:"
    response = co.generate(
        model='large',
        prompt=prompt,
        max_tokens=100,
        temperature=1,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    # print('Prediction: {}'.format(response.generations[0].text))
    return response.generations[0].text[:-2]

# return sentiment object
def generateSentiment(co, input):
    (input, max_tokens) = checkLength(input)
    examples = [
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

    inputs = [input]

    response = co.classify(
        model='medium',
        inputs=inputs,
        examples=examples)
    print(response.classifications[0].prediction)
    # prediction = str(response.classifications[0]['prediction'])
    result = {
        # "prediction": prediction,
        'negative': response.classifications[0].labels['negative'].confidence,
        'positive': response.classifications[0].labels['positive'].confidence,
        'neutral': response.classifications[0].labels['neutral'].confidence
    }
    return (response.classifications[0].prediction, result)
