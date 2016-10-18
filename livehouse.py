import re
from livestreamer import StreamError
from livestreamer.plugin import Plugin
from livestreamer.stream import HLSStream

_url_re = re.compile(r"livehouse.in/channel/(\w+)")

class LiveHouse(Plugin):
    @classmethod
    def can_handle_url(cls, url):
        match = _url_re.match(url)
        return match

    def _get_streams(self):
        url_match = _url_re.match(self.url)
        if url_match:
            _id = url_match.group(1)
            url = 'https://rtctw-rtcp-tw-1.livehouse.in/{id}/video/playlist.m3u8'.format(
            	id=_id)
            streams = HLSStream.parse_variant_playlist(self.session, url)
            return streams
        else:
            raise StreamError("Error open playlist, maybe it's not live stream ")         
            
__plugin__ = LiveHouse
