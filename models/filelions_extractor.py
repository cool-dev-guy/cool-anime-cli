import cloudscraper
import re
def get(url):
    scraper = cloudscraper.create_scraper()
    resp = scraper.get('https://alions.pro/v/hblwmmnbe25z')
    matches = re.search(r'return p}\((.+)\)', resp.text)
    def unpack(p, a, c, k, e=None, d=None) -> str:
        for i in range(c - 1, -1, -1):
          if k[i]: p = re.sub("\\b" + int_2_base(i, a) + "\\b", k[i], p)
        return p
    def int_2_base(x: int, base: int) -> str:
        charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"
        if x < 0:
            sign = -1
        elif x == 0:
            return 0
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(charset[int(x % base)])
            x = int(x / base)
            
        if sign < 0:
            digits.append('-')
        digits.reverse()

        return ''.join(digits)
    split_matches = matches.group(1).split(",")
    corrected_split_matches = [",".join(split_matches[:-3])
                                   ] + split_matches[-3:]
    processed_matches=[]
    for val in corrected_split_matches:
      val = val.strip()
      val = val.replace(".split('|'))", "")
      if val.isdigit() or (val[0] == "-" and val[1:].isdigit()):
        processed_matches.append(int(val))
      elif val[0] == "'" and val[-1] == "'":
        processed_matches.append(val[1:-1])

    processed_matches[-1] = processed_matches[-1].split("|")
    unpacked = unpack(*processed_matches)
    hls_url = re.search(r'file:"([^"]*)"', unpacked).group(1)
    return hls_url
