import pickler
import requests
import json
import time

FIVE_SECONDS = 4

def get_engagement(url):
    access_token = 'EAAES1ZCsXZCGABABjEGM1ZCqnBZAWp0yxJRj7MIxmUVSeOFcLdpjfi8K5UzqFiMfYwvGqnLAG1lDk6oZB7NuzWJWRuZBRx3qHldmVZBT0Uuz5XfMpRINoP1e7dHbZAVk2Px0Is6yhbevsuEt1viZBack6G0wLf19R5u3wj6RllYZBCZAgYxeCmcPK0tXi14dws1S4oZD'
    graph_url = 'https://graph.facebook.com/v3.2/?fields=engagement&access_token=' + access_token + '&id=' + url
    print(graph_url)
    r = requests.get(graph_url)
    print(r.json())
    result = json.loads(r.text)
    engagement = result.get('engagement')
    # {'engagement': {u'comment_count': 0, u'comment_plugin_count': 0, u'share_count': 0, u'reaction_count': 0}
    print(engagement)
    return engagement


base_url = 'https://www.stugknuten.com'

urls = pickler.load('urls.pickle', [])
result = []
for url in urls:
    full_url = base_url + url
    engagement = get_engagement(full_url)
    obj = {
        'url': full_url,
        'engagement': engagement
    }
    print(obj)
    result.append(obj)
    time.sleep(FIVE_SECONDS)

pickler.save('result.pickle', result)
