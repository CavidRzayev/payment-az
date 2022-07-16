import base64
import datetime
import hashlib
import time
from hmac import HMAC


def microtime(get_as_float=False):
    d = datetime.datetime.now()
    t = time.mktime(d.timetuple())
    if get_as_float:
        return t
    else:
        ms = d.microsecond / 1000000.0
        return "%f %d" % (ms, t)


def convert_string_to_hash(word):
    digest = hashlib.sha1(word.encode())
    result = base64.b64encode(digest.digest())
    return result


def substr(string, start, length=None):
    if start < 0:
        start = start + len(string)
    if not length:
        return string[start:]
    elif length > 0:
        return string[start : start + length]
    else:
        return string[start:length]


def gmdate(format: str, seconds: float = None) -> str:
    if seconds is None:
        return time.strftime(format, time.gmtime())

    return time.strftime(format, time.gmtime(seconds))


def hex2bin(hexdata):
    bindata = ""
    i = 0
    while i < len(str(hexdata)):
        try:
            string = substr(hexdata, i, 2)
            hexdec = int(bin(int(string, 16)), 2)
            bindata += chr(hexdec)
            i += 2
        except:
            pass
    return bindata.encode("latin-1")


def lowercase(obj):
    if isinstance(obj, dict):
        return {k.lower(): lowercase(v) for k, v in obj.items()}
    elif isinstance(obj, (list, set, tuple)):
        t = type(obj)
        return t(lowercase(o) for o in obj)
    elif isinstance(obj, str):
        return obj.lower()
    else:
        return obj


def hash_hmac(algo: str, data: str, key: bytes) -> HMAC:
    return HMAC(key=key, msg=data.encode(), digestmod=algo).hexdigest()
