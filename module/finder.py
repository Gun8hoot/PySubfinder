#   SUBDOMAIN FINDER MODULE
from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from module.color import color
import sys, time


def finder(url, wl):
    # Parse the URL
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path
    show_sample = f"{scheme}://SUBD.{netloc}{path}"
    show_sample_w = show_sample.replace('www.', '')
    print(f'\n{color.fr_yellow}[!] The script will test : {color.underline}{show_sample_w}{color.reset}')

    #   WORDLIST SELECTOR
    try:
        if wl == None:
            with open('subdomains-top1million-110000.txt', 'r') as f:
                WL = f.readlines()
        elif wl != None:
            with open(wl, 'r') as f:
                WL = f.readlines()
    except FileNotFoundError:
        WL = 'null'
        print(f'{color.fr_red}[!] The wordlist was not found : {wl} {color.reset}')

    #   SEE ALL REQUEST 

    for word in WL:
        tester = f"{scheme}://{word}.{netloc}{path}".replace('www.', '')
        ml = tester.replace('\n', '')
        try:
            with urlopen(ml, timeout=5) as response:
                http_code = response.status
                print(f'{color.fr_green}[{color.blink_on}+{color.blink_off}] Subdomain found: {color.bold_on}{ml}{color.reset}')
                
        except URLError or HTTPError:
            pass