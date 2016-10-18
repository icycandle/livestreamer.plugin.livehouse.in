import re
from livestreamer import StreamError
from livestreamer.plugin import Plugin
from livestreamer.stream import HLSStream

print("livehouse.py plugin is loading.")

regex_pattern = r"livehouse.in/channel/(\w+)"

class LiveHouse(Plugin):
    @classmethod
    def can_handle_url(cls, url):
        match = re.findall(regex_pattern, url)
        return match

    def _get_streams(self):
        match = re.findall(regex_pattern, self.url)
        if match:
            _id = match[0]
            url = 'https://rtctw-rtcp-tw-1.livehouse.in/{id}/video/playlist.m3u8'.format(
                id=_id)
            streams = HLSStream.parse_variant_playlist(self.session, url)
            return streams
        else:
            raise StreamError("Error open playlist, maybe it's not live stream ")

__plugin__ = LiveHouse
