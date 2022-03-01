import sys
import asyncio
from telethon import TelegramClient, events, functions, types

peers = sys.argv[3:]

api_id = sys.argv[1]
api_hash = sys.argv[2]

async def main():
  client = TelegramClient('session_name', api_id, api_hash)

  await client.start()

  for p in peers:
    result = await client(functions.account.ReportPeerRequest(
      peer=p,
      reason=types.InputReportReasonOther(),
      message='Propaganda of the war in Ukraine. Propaganda of the murder of Ukrainians and Ukrainian soldiers.'
    ))

    print(p, result)

if __name__ == "__main__":
  asyncio.run(main())