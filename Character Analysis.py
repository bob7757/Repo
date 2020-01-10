from pprint import pprint

test_text = input("Type some text here for analysis.")
text_list = [*test_text]
text_list.sort()
analysis = {}
for letter in text_list:
    temp = {letter: text_list.count(letter)}
    analysis.update(temp)
if " " in analysis:
    del analysis[" "]
pprint(analysis, width=1)
sorted_analysis = sorted(analysis.items(), key=lambda kv:kv[1])
pprint(sorted_analysis)