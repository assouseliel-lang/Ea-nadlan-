import json,glob,os
a=[]
for f in sorted(glob.glob('content/properties/*.json')):
 with open(f,encoding='utf-8') as h:a.append(json.load(h))
os.makedirs('data',exist_ok=True)
with open('data/properties.json','w',encoding='utf-8') as h:json.dump(a,h,ensure_ascii=False,indent=2)
