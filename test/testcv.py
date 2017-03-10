import sys

from converter import Converter

conv = Converter(sys.argv[1], sys.argv[2]).convert(sys.argv[3], sys.argv[4], {
    'format': 'mkv',
    'audio': {'codec': 'aac'},
    'video': {'codec': 'h265'}
}, twopass=True)

for status_dict in conv:
    print("Converting (%s) ...\r" % status_dict)
