import pandas as pd
import re
res = pd.read_csv('parsed.csv')
res['match'] = ''
regex = r"[^.]*\s+\d+\s+(январ[ьея]|феврал[ьея]|март[еа]?|апрел[ьея]|ма[йея]|ию[нл][яье]|август[еа]?|(?:сент|окт|но|дек)[ая]бр[яье])[^.]*\."
matches = re.finditer(regex, res['text'][0], re.MULTILINE)
for match in matches:
    print(match.group())
