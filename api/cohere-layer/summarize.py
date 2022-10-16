import cohere
import os
from dotenv import load_dotenv
load_dotenv()

def generateSummery(input):
  api_key = os.getenv('COHERE_KEY')
  co = cohere.Client(api_key)

  learning_prompt = '''
  Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn’t the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to “the dusty section of the dictionary” to find its latest words.\n\nTLDR: Wordle has not gotten more difficult to solve.\n--\nPassage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.\n\nTLDR: ArtificialIvan has raised $190 million in Series C funding.\n--\n
  '''
  prompt = f"{learning_prompt}Passage: {input}\n\nTLDR:"
  response = co.generate(
    model='large',
    prompt= prompt,
    max_tokens=60,
    temperature=1,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
  # print('Prediction: {}'.format(response.generations[0].text))
  return response.generations[0].text

if __name__ == '__main__':
  input = '''
  Vancouver businessman Ken Sim defeated Vancouver Mayor Kennedy Stewart, posting an overwhelming victory after losing the mayor's race to Stewart in 2018 by less than 1,000 votes.

  Sim, 63, paid tribute to his immigrant parents in an acceptance speech that noted the historic election of Vancouver's first Chinese-Canadian mayor.

  "The path to get here was incredibly long," said Sim. "One hundred and thirty-five years after the first Chinese head tax was paid just for the right to come here and work on building a railway, Vancouver has elected its first Chinese mayor."

  "The history of this moment is not lost on me," he said. "But the honour really goes to those whose shoulders I stand on."

  Sim said he's paying tribute to Vancouver's Chinese-Canadian trailblazers who helped him and others in the city achieve success.

  "Thank you for not giving up on the promise we can make Vancouver a better city," said Sim to cheers and claps from his supporters. "Look, you can't lose if you never give up."

  Stewart said the past four years, with the ongoing COVID-19 pandemic, the opioid overdose crisis and housing issues were difficult for Vancouver, but "I do think we got the city through pretty hard times."
  '''
  print(generateSummery(input))
