import requests
# get here https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb
token = 'y0_AgAAAABk6bkUAATuwQAAAADP8rZhOVvYPgChTwWrMpci4kUvDmeFcQU'
# get here https://console.cloud.yandex.ru/folders
folder_id = 'b1g0h7hn7vnocpbcgc8q'

def get_iam_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"yandexPassportOauthToken":"' + token + '"}'

    response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', headers=headers, data=data)
    IAM_TOKEN = response.json()['iamToken']
    return IAM_TOKEN


def main():
    IAM_TOKEN = get_iam_token()
    target_language = 'ru'
    texts = ["Hello", "World"]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )

    print(response.text)


if __name__ == '__main__':
    main()
