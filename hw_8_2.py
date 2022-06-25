import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
         }

    def _upload_link(self, yadisk_path):
        disk_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": yadisk_path, "overwrite": "true"}
        response = requests.get(disk_url, headers=headers, params=params)
        return response.json()

    def upload(self, yadisk_path, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._upload_link(yadisk_path).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    token_ = ''
    uploader = YaUploader(token_)
    file_names = ['test_ya.txt', 'test_ya2.txt']
    sub_folders = 'netology/'
    for file_name_ in file_names:
        result = uploader.upload(sub_folders+file_name_, file_name_)
