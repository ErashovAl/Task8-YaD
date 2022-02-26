from pathlib import Path
import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path, file_name):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                    'Authorization': self.token}
        params = {'path': file_path, 'overwrite': 'true'}
        href = requests.get(upload_url, headers=headers, params=params)
        resp = requests.put(href.json().get('href', ''), data=open(file_name, 'rb'))
        resp.raise_for_status()
        if resp.status_code == 201:
            print('Success')

if __name__ == '__main__':

    def launch(user_path):
        path_to_file = Path(user_path)
        token = ''
        uploader = YaUploader(token)
        # print(path_to_file.name)
        name_to_disk = 'test/'+ path_to_file.name
        uploader.upload(name_to_disk, path_to_file)

launch('C:\Books\Фрэнк Саммерс - за пределами самости.txt')