#!/usr/bin/env python
import re
from livestreamer.plugin import Plugin
from livestreamer.plugin.api import http, validate
from livestreamer.stream import RTMPStream

_url_re = re.compile(r"https://www.cavelis.net/live/(.+)")
_playlist_re = re.compile("\"(https://[^\"]*/video/playlist\.m3u8)")

class CaveTube(Plugin):
    def _getPlayList(self, url):
        resp = http.get(url)
        result = CaveTube.get_rtmp_link(resp.text)
        if result:
            return result


    @classmethod
    def _get_field(cls, field_name, content):
        a_re = re.compile('%s: \'([^\']+)\'' % (field_name))
        search_result = a_re.search(content)
        if search_result:
            return (search_result.group(1))


    @classmethod
    def get_rtmp_link(cls, html_content):
        hostUrl = CaveTube._get_field('hostUrl', html_content)
        streamName = CaveTube._get_field('streamName', html_content)

        if hostUrl and streamName:
            return '%s/%s' % (hostUrl, streamName)
    
    @classmethod
    def can_handle_url(cls, url):
        match = _url_re.match(url)
        return match
   
    def _get_streams(self):
        url_match = _url_re.match(self.url)
        if url_match:
            stream_url = self._getPlayList(self.url)
            stream_params = {
                "rtmp": stream_url,
                "live": True
            }
            stream = RTMPStream(self.session, stream_params)
            yield "live", stream

__plugin__ = CaveTube

