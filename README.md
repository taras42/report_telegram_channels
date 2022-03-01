# report_telegram_channels
Easily report multiple telegram channels
Легко оскаржуйте декілька телеграм каналів одночасно

## ENG
### Command Line
A script to easily report multiple telegram channels at once. Instruction:

1. Install python3 on your PC (if you do this on Windows, check Add To PATH on installation)
1.1 Open cmd/terminal and install telethon (pip3 install telethon) telegram client
2. Follow instrutions [here](https://core.telegram.org/api/obtaining_api_id) to obtain your api_id and api_hash for telegram client
3. Once you get your `api_id` and `api_hash`, run the python file attached to this message like this:
```shell
python3 report.py <api_id> <api_hash> "<report_message>" @channel1 @channel2 @channel3
```


to report multiple channels at once.

## UKR:
### Інтерфейс командного рядка:
Python скрипт для оскаржування декількох телеграм каналів одночасно.

1. Встановіть python3 на вашому комп'ютері (якщо ви на Windows, відмітьте Add To PATH при інсталяції)
1.1 Відкрийте командний рядок(cmd)/термінал і встановіть telethon (pip3 install telethon) telegram клієнт
2. Слідуйте інстукціям [тут](https://core.telegram.org/api/obtaining_api_id) для того щоб отримати `api_id` та `api_hash` для telegram клієнту
3. Коли ви отримаєте свій `api_id` та `api_hash`, запустіть python скрипт з цього репозиторію (скачайте і запустіть з командного рядка):
```shell
python3 report.py <api_id> <api_hash> "<report_message>" @channel1 @channel2 @channel3
```

для того щоби поскаржитися на декілька каналів одночасно.