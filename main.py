#!/bin/python3

#   MODULE IMPORTATION
import argparse, os, time, sys
from module.color import color
from module.finder import finder
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

#   ARGUMENTS
parser = argparse.ArgumentParser(prog='PySubFinder', description='Find subdomain on a web server')
parser.add_argument('-u', '--url', type=str, required=True, dest='URL')
parser.add_argument('-f', '--file', type=str, required=False, dest='FILE', help='Enter the path of the subdomain wordlist you want use. If it not specify, the script will take the "subdomains-top1million-110000.txt" present in the root of the program folder.')
args = parser.parse_args()
#   ---
url = args.URL
wl_path = args.FILE



#   BANNER & DECORATION
with open('banner.txt', 'r') as f:
    banner = f.read()

#   MAIN
if __name__ == '__main__':
    try:
        print(f'{color.fr_purple}{banner}{color.reset}')
        if url == None:
            print('[!]  You need to enter an url')
            sys.exit()
        elif url != None:
            if str(url).startswith('http://') or str(url).startswith('https://'):
                try:
                    with urlopen(url) as ping:
                        finder(url, wl_path)
                except URLError or HTTPError:
                    print(f'\n{color.fr_red}[!] The client cannot connect to the server{color.reset}')
            elif str(url) != str(url).startswith('http://') or str(url) != str(url).startswith('http://'):
                print(color.fr_red+'[!] You need to enter a correct url\nFORMAT: http://{DOMAIN}.{TOP LEVEL DOMAIN}'+color.reset)
                sys.exit()

    except KeyboardInterrupt:
        print(f"\n{color.fr_red}Keyboard Interrupt keys press, if it's not voluntary try again and do not press your keyboard interupt keys\nNOTES: Keyboard Interrupt keys = CTRL+C{color.reset}")
        sys.exit()