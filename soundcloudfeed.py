import requests
import xmltodict
import shared

class SoundCloud:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
    def request(self, config :dict=None):
        if config != None and isinstance(config, dict):
            return self.rss.request(
                *self.shared.convert_json_to_values(
                    config=config
                )
            )
    def feed(self, user_id :int=None):
        if user_id != None and isinstance(user_id, int):
            config = {
                "method": "get",
                "url": f"https://feeds.soundcloud.com/users/soundcloud:users:{user_id}/sounds.rss"
            }
            req = self.request(
                config=config
            )
            if req != None:
                data = xmltodict.parse(
                    xml_input=req.content
                )
                if data != None and isinstance(data, dict):
                    if "rss" in data and data["rss"] != None and isinstance(data["rss"], dict):
                        return data["rss"]
    def oembed(
        self,
        _url :str=None,
        _maxwidth :int=500,
        _maxheight :int=166,
        _authoplay :bool=False,
        _color :str="ff0066",
        _show_comments :bool=True,
        _callback :str=None,
        _format :str="json"
    ):
        if _url != None and isinstance(_url, str) and \
        _maxwidth != None and isinstance(_maxwidth, int) and \
        _maxheight != None and isinstance(_maxheight, int) and \
        _authoplay != None and isinstance(_authoplay, bool) and \
        _color != None and isinstance(_color, str) and \
        _show_comments != None and isinstance(_show_comments, bool) and \
        _format != None and isinstance(_format, str) and _format.lower() in ["json", "js", "xml"]:
            config ={
                "method": "get",
                "url": "https://soundcloud.com/oembed",
                "params": {
                    "url": _url,
                    "maxwidth": _maxwidth,
                    "maxheight": _maxheight,
                    "authoplay": _authoplay,
                    "color": _color,
                    "show_comments": _show_comments,
                    "format": _format.lower(),
                    **({"callback": _callback} if _callback != None and isinstance(_callback, str) and _format.lower() == "js" else {})
                }
            }
            req = self.request(
                config=config
            )
            return req.json() if _format.lower() == "json" else req.text