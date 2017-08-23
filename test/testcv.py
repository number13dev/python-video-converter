import sys

from converter import Converter

conv = Converter(sys.argv[1], sys.argv[2]).convert(sys.argv[3], sys.argv[4], {
    'format': 'mkv',
    'audio': {'codec': 'aac'},
    'video': {'codec': 'h265', 'preset' : 'ultrafast', 'bitrate' : '2800', 'width': '320', 'height': '240', 'scale': '320:240'}
}, twopass=False)

for status_dict in conv:
    print("Converting (%s) ...\r" % status_dict)
