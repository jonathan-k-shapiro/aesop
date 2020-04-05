import json

title_template = '''
# {title}

## Story
'''

para_template = '''
### Paragraph {para_num}

{text}

'''

moral_template = '''
## Moral

_{moral}_
'''

outputDir = 'aesops-fables'

with open('fables.json') as f:
    data = json.load(f)

for row in data:
    filename = '{}/{}.md'.format(outputDir, row['title'].lower().replace(' ', '-'))
    with open (filename, 'w') as fout:
        print(title_template.format(**row), file=fout)
        for i in range(len(row['paragraphs'])):
            print(para_template.format(para_num=i+1, text=row['paragraphs'][i]), file=fout)
        print(moral_template.format(**row), file=fout)

        