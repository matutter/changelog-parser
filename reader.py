import sys
import re

VERSION_RE = re.compile(r"""
^[#]{2}\s+?\[(?P<version>[^\]]+).*
""", re.VERBOSE)

def parse(changelog):

  version_map = {}
  latest_ver = None
  this_ver = None
  for line in changelog.splitlines():
    match = VERSION_RE.match(line)
    if match:
      this_ver = match.groupdict()['version']
      version_map[this_ver] = line
      if latest_ver is None:
        latest_ver = this_ver
    elif this_ver is not None:
      version_map[this_ver] += line +'\n'

  return latest_ver, version_map

def get_latest(changelog):
  latest, ver_map = parse(changelog)
  return ver_map[latest]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as fd:
      parse(fd.read())
