# report_telegram_channels
Easily report multiple telegram channels
Легко оскаржуйте декілька телеграм каналів одночасно

## ENG
Attention: use on your own risk - While the script will sleep 10 to 20 seconds between requests and 50 to 60 seconds between each 10 requests, telegram might ban your account if you will use this app to report huge amount of accounts in short time.
It's better to use separate telegram account to use this app.

Follow instructions [here](https://core.telegram.org/api/obtaining_api_id) 
to obtain your `api_id` and `api_hash` for telegram client

### Command Line
A script to easily report multiple telegram channels at once. Instruction:

1. Install python3 on your PC (if you do this on Windows, check Add To PATH on installation)
2. Download zip folder from github, unpack.
3. Open cmd/terminal got the unpacked folder and install required dependencies (`pip3 install -r requirements.txt`).
4. You can specify channels manually using flags -c or --channels, or provide path to the .txt file where id of channels are stored with -f or --file flags.<br />Example with specifying channels manually (for api_id: 01234567, and api_hash: 0123456789abcdefghijklmnopqrstuw)
```shell
python3 report.py 01234567 0123456789abcdefghijklmnopqrstuw "Propaganda of the war in Ukraine. Propaganda of the murder of Ukrainians and Ukrainian soldiers." -c @channel1 @channel2 @channel3 https://t.me/channel
```

### Text file support
Application supports loading channels to report from `.txt` file.

Text file example (`channels.txt`):
```text
@channel1
@channel2
@channel3
```
Command (for api_id: 01234567, and api_hash: 0123456789abcdefghijklmnopqrstuw)
```shell
python3 report.py 01234567 0123456789abcdefghijklmnopqrstuw "Propaganda of the war in Ukraine. Propaganda of the murder of Ukrainians and Ukrainian soldiers." -f ./channels.txt
```
### Docker

1. Install [Docker](https://www.docker.com/)
2. Build image: 
    ```shell
    docker build . -t report-telegram
    ```
3. Run:
    ```shell
    docker run -it --rm report-telegram <api_id> <api_hash> "<report_message>" -c @channel1 @channel2 @channel3 https://t.me/channel
    ```
    Or:
    ```shell
    docker run -it --rm report-telegram <api_id> <api_hash> "<report_message>" -f ./channels.txt
    ```
## UKR:

Увага: використовуйте на свій страх і ризик - Програма буде очікувати від 10 до 20 секунд між кожним запитом та від 50 до 60 секунд кожні 10 запитів щоб змешити ризики, але телеграм може заблокувати ваш аккаунт якщо ви будете повідомляти про велику кількість аккаунтів за малий час.
Краще зробити окремий телеграм акканунт для використання цієї програми.

Слідуйте інструкціям [тут](https://core.telegram.org/api/obtaining_api_id)
для того щоб отримати `api_id` та `api_hash` для telegram клієнту

### Інтерфейс командного рядка:
Python скрипт для оскаржування декількох телеграм каналів одночасно.

1. Встановіть python3 на вашому комп'ютері (якщо ви на Windows, відмітьте Add To PATH при інсталяції)
2. Скачайте архів з проектом з гітхабу, розпакуйте
3. Відкрийте командний рядок(cmd)/термінал, перейдіть у розпаковану папку з проектом і встановіть потрібні залежності (`pip3 install -r requirements.txt`).
4. Ви можете вводити канали самостійно, вказавши параметри -c або --channels, або ввести шлях до .txt файлу, вказавши параметри -f or --file, де зберігаються id потрібних телеграм каналів.
<br />Приклад з введенням каналів самостійно(де api_id: 01234567, а api_hash: 0123456789abcdefghijklmnopqrstuw)
```shell
python3 report.py 01234567 0123456789abcdefghijklmnopqrstuw "Пропаганда війни в Україні. Пропаганда вбивства українців і українських солдат." -с @channel1 @channel2 @channel3 https://t.me/channel
```
(повідомлення можливо краще відправляти на англ)

### Підтримка текстового файлу
Додаток дозволяє завантажувати список аккаунтів з текстових файлів.

Приклад текстового файлу (`channels.txt`):
```text
@channel1
@channel2
@channel3
```

Команда (де api_id: 01234567, а api_hash: 0123456789abcdefghijklmnopqrstuw)
```shell
python3 report.py 01234567 0123456789abcdefghijklmnopqrstuw "Пропаганда війни в Україні. Пропаганда вбивства українців і українських солдат." -f ./channels.txt
```

### Docker

1. Встановіть [Docker](https://www.docker.com/)
2. Білд докер образу:
    ```shell
    docker build . -t report-telegram
    ```
3. Запуск:
    ```shell
    docker run -it --rm report-telegram <api_id> <api_hash> "<зміст_повідомлення>" -c @channel1 @channel2 @channel3 https://t.me/channel
    ```
    Або:
    ```shell
    docker run -it --rm report-telegram <api_id> <api_hash> "<зміст_повідомлення>" -f ./channels.txt
    ```
