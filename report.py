import sys
import asyncio
import time
import random
from telethon import TelegramClient, events, functions, types

peers = sys.argv[4:]

api_id = sys.argv[1]
api_hash = sys.argv[2]
message = sys.argv[3]

async def main():
  client = TelegramClient('session_name', api_id, api_hash)

  await client.start()

  for p in peers:
    result = None

    try:
      result = await client(functions.account.ReportPeerRequest(
        peer=p,
        reason=types.InputReportReasonOther(),
        message=message
      ))

      print(p, result)

      sleep_for = random.randint(10, 20)

      print('sleep for {}s...'.format(sleep_for))
      time.sleep(sleep_for)
    except:
      print('no user', p)
      continue

if __name__ == "__main__":
  asyncio.run(main())