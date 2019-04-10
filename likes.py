import pickler
import requests
import json
import time

FIVE_SECONDS = 5

def get_engagement(url):
    access_token = 'EAACuFURl7OgBAFr1hs7fOZCUu7Eq0TQ1s1clSoJtMyfHZBv4UtzyXZAxxs5SC2DA10Q83wrgFeJKr61QNQDVS5CYcpKZBZAHrIjDLZAiSwu363xJuZAbEGRxjO9wOQdRCMyrQHEGHEARTZCjO2ar5lw1ZCz8bHRJRjiP27aaJzEHb8WwHGbOrbAnLfAZBYlzCh7mgZD'
    graph_url = 'https://graph.facebook.com/v3.2/?fields=engagement&access_token=' + access_token + '&id=' + url
    print(graph_url)
    r = requests.get(graph_url)
    print(r.status_code)
    print(r.json())
    if r.status_code == 200:
        result_json = json.loads(r.text)
        engagement_json = result_json.get('engagement')
        # {'engagement': {u'comment_count': 0, u'comment_plugin_count': 0, u'share_count': 0, u'reaction_count': 0}
        print(engagement_json)
        return engagement_json
    else:
        return None


base_url = 'https://www.stugknuten.com'

cottages = pickler.load('stugor_vastkusten.pickle', [])
result = []
for cottage in cottages:
    cottage_href = cottage.get('href')
    engagement = get_engagement(cottage_href)
    if engagement:
        cottage['engagement'] = engagement
        print(cottage)
        result.append(cottage)
        time.sleep(FIVE_SECONDS)
    else:
        print('NO ENGAGEMENT! ERROR! ABORT ABORT!')
        break

pickler.save('likes_vastkusten.pickle', result)
