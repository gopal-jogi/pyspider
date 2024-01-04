import json
with open('test.py','r') as obj:
    content=obj.read()
    with open('test.json','w') as ob:
       ob.write(json.dumps(content))