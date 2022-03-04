import sys
import asyncio
import time
import random
import platform
from telethon import TelegramClient, events, functions, types
from argparse import ArgumentParser, FileType

def create_parser():
    """Initializes parser with all parameters"""

    parser = ArgumentParser(prog="report_telegram_channels")
    parser.add_argument('api_id', help='Your API id')
    parser.add_argument('api_hash', help='Your API hash')
    parser.add_argument('message', help='Report message')
    
    # this controls that one of this arguments (-c or -f)
    # must be specified, but not both at a time
    mutual_group = parser.add_mutually_exclusive_group(required=True)
    mutual_group.add_argument('-c', '--channels', nargs='*', dest='channels', 
                              help='Channels to report')
    mutual_group.add_argument('-f', '--file', dest='filepath', type=FileType('r'),
                              help='File with channels to report')
    return parser

async def main():
    parser = create_parser()
    args, _ = parser.parse_known_args()
    # initialize variables
    api_id = args.api_id
    api_hash = args.api_hash
    message = args.message
    
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    if args.filepath is not None:
        # channels are taken from file
        peers = args.filepath.read().splitlines()
    else:
        # channels are taken from command line
        peers = args.channels
    for idx, p in enumerate(peers):
        result = None

        try:
            result = await client(functions.account.ReportPeerRequest(
                peer=p,
                reason=types.InputReportReasonOther(),
                message=message
                ))

            print(p, result)

            if idx > 0 and not idx % 10:
                sleep_for = random.randint(50, 60)

                print('sleep for {}s before the next batch of 10'.format(sleep_for))
                time.sleep(sleep_for)
            else:
                sleep_for = random.randint(10, 20)

                print('sleep for {}s...'.format(sleep_for))
                time.sleep(sleep_for)
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
