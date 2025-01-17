import soundcloudfeed
import json

sc = soundcloudfeed.SoundCloud()

#296256364
user_id = 296256364

user_feed = sc.feed(
    user_id=user_id
)

user_oembed = sc.oembed(
    _url=user_feed["channel"]["image"]["link"]
)

print(json.dumps(obj=user_feed, indent=4))

print(json.dumps(obj=user_oembed, indent=4))
