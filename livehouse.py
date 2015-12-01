#!/usr/bin/env python
import re

from livestreamer.plugin import Plugin
from livestreamer.plugin.api import http, validate
from livestreamer.stream import HLSStream

_url_re = re.compile(r"https://livehouse.in/channel/(.+)")

class LiveHouse(Plugin):
    @classmethod
    def can_handle_url(cls, url):
        match = _url_re.match(url)
        return match

    def _get_streams(self):
        url_match = _url_re.match(self.url)
        if url_match:
            _id = url_match.group(1)
            url = 'https://rtctw-rtcp-tw-1.livehouse.in/%s/video/playlist.m3u8' % (_id)
            streams = HLSStream.parse_variant_playlist(self.session, url)
            return streams
        else:
             raise StreamError("Error open playlist, maybe it's not live stream ")         
            
__plugin__ = LiveHouse

