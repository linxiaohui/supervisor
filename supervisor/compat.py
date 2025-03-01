from __future__ import absolute_import

import sys

PY2 = sys.version_info[0] == 2

if PY2: # pragma: no cover
    long = long
    raw_input = raw_input
    unicode = unicode
    unichr = unichr
    basestring = basestring

    def as_bytes(s, encoding='utf-8'):
        if isinstance(s, str):
            return s
        else:
            return s.encode(encoding)

    def as_string(s, encoding='utf-8'):
        if isinstance(s, unicode):
            return s
        else:
            return s.decode(encoding)

    def is_text_stream(stream):
        try:
            if isinstance(stream, file):
                return 'b' not in stream.mode
        except NameError:  # python 3
            pass

        try:
            import _io
            return isinstance(stream, _io._TextIOBase)
        except ImportError:
            import io
            return isinstance(stream, io.TextIOWrapper)

else: # pragma: no cover
    long = int
    basestring = str
    raw_input = input
    unichr = chr

    class unicode(str):
        def __init__(self, string, encoding, errors):
            str.__init__(self, string)

    def as_bytes(s, encoding='utf8'):
        if isinstance(s, bytes):
            return s
        else:
            return s.encode(encoding)

    def as_string(s, encoding='utf8'):
        if isinstance(s, str):
            return s
        else:
            return s.decode(encoding, errors='ignore')

    def is_text_stream(stream):
        import _io
        return isinstance(stream, _io._TextIOBase)

try: # pragma: no cover
    import xmlrpc.client as xmlrpclib
except ImportError: # pragma: no cover
    import xmlrpclib

try: # pragma: no cover
    import urllib.parse as urlparse
    import urllib.parse as urllib
except ImportError: # pragma: no cover
    import urlparse
    import urllib

try: # pragma: no cover
    from hashlib import sha1
except ImportError: # pragma: no cover
    from sha import new as sha1

try: # pragma: no cover
    import syslog
except ImportError: # pragma: no cover
    syslog = None

try: # pragma: no cover
    import ConfigParser
except ImportError: # pragma: no cover
    import configparser as ConfigParser

try: # pragma: no cover
    from StringIO import StringIO
except ImportError: # pragma: no cover
    from io import StringIO

try: # pragma: no cover
    from sys import maxint
except ImportError: # pragma: no cover
    from sys import maxsize as maxint

try: # pragma: no cover
    import http.client as httplib
except ImportError: # pragma: no cover
    import httplib

try: # pragma: no cover
    from base64 import decodebytes as decodestring, encodebytes as encodestring
except ImportError: # pragma: no cover
    from base64 import decodestring, encodestring

try: # pragma: no cover
    from xmlrpc.client import Fault
except ImportError: # pragma: no cover
    from xmlrpclib import Fault

try: # pragma: no cover
    from string import ascii_letters as letters
except ImportError: # pragma: no cover
    from string import letters

try: # pragma: no cover
    from hashlib import md5
except ImportError: # pragma: no cover
    from md5 import md5

try: # pragma: no cover
    import thread
except ImportError: # pragma: no cover
    import _thread as thread

try: # pragma: no cover
    from types import StringTypes
except ImportError: # pragma: no cover
    StringTypes = (str,)

try: # pragma: no cover
    from html import escape
except ImportError: # pragma: no cover
    from cgi import escape

try: # pragma: no cover
    import html.entities as htmlentitydefs
except ImportError: # pragma: no cover
    import htmlentitydefs

try: # pragma: no cover
    from html.parser import HTMLParser
except ImportError: # pragma: no cover
    from HTMLParser import HTMLParser
