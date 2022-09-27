# yandex_translate
Simple yandex translate func

***I strongly recommend write tokens to environment variables***

### Instruction:
1. On the Billing page, make sure that the payment account is in the status of Active or Trial_active. If there is no payment account, create it.
2. Get an IAM-token necessary for authentication. Go to [link](https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb) and copy value to 'token' variable.
3. Get the identifier of any catalog on which your account has the role of Editor or higher. Got to [link](https://console.cloud.yandex.ru/folders) and select folder. Check url.

`https://console.cloud.yandex.ru/folders/b1gd129pp9ha0vnvf5g7`

Where: b1gd129pp9ha0vnvf5g7 — folder_id variable.
  
