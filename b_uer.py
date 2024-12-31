from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

s = open('cleaned.data', 'r', encoding='utf-8').read().strip().split('\n')
ss = list()
for i in s:
    if len(i) > 256:
        ss += i.split('. ')
    else:
        ss.append(i)

model_name = 'uer/roberta-base-finetuned-cluener2020-chinese'

model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

nlp = pipeline(
    'ner',
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy='simple',
    device='cuda'
)

names = list()
for i in ss:
    ner_results = nlp(i)
    name = [entity['word'] for entity in ner_results if entity['entity_group'] == 'name']
    names += name

names = list(set([i.replace(' ', '') for i in names]))
print(names)
