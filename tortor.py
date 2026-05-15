import datetime
import sys
import random
from lib.color import color
from lib.tor import Tor

def main():
    counter = 0
    try:
        while counter < max_attempts:
            tor = Tor()
            if not tor.tor_installed():
                print u'{}[!]{} Tor is not installed. Exiting...'.format(color.RED, color.END)
                sys.exit(1)
            else:
                # Initial timestamp and increment the counter
                start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
                counter += 1

                # Baca proxy dari file
                with open('proxy.txt', 'r') as f:
                    proxies = [line.strip() for line in f if line.strip()]
                proxy = random.choice(proxies)
                proxies = {
                    'http': proxy,
                    'https': proxy
                }

                # Init a new Tor session dengan proxy
                session = tor.new_session(proxies=proxies)
                print u'{}[!]{} New Tor session initialized...'.format(color.BLUE, color.END)
                print u'\n{}[+]{} Target: {}{}{}'.format(color.PURPLE, color.END, color.PURPLE, target, color.END)

                # Getting
