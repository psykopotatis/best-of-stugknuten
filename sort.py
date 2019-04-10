import pickler
import pprint
import json


urls = pickler.load('likes_vastkusten.pickle', [])
# {'engagement': {u'comment_count': 0, u'comment_plugin_count': 0, u'share_count': 0, u'reaction_count': 0}
sorted_urls = sorted(urls, key=lambda x: x.get('engagement').get('reaction_count'), reverse=True)


def pretty_print():
    pp = pprint.PrettyPrinter(indent=4)
    for sorted_url in sorted_urls:
        pp.pprint(sorted_url)

def to_json():
    with open('likes_vastkusten.json', 'w') as outfile:
        print('dumping ....')
        json.dump(sorted_urls, outfile, indent=4, sort_keys=True)
        print('done')

to_json()
