import requests


class YaUploader:
    base_path = "https://cloud-api.yandex.net/"
    upload_command_path = "v1/disk/resources/upload"
    resources_command_path = "v1/disk/resources"

    def __init__(self, file_token_name: str):
        self.token = self.__get_token_from_file__(file_token_name)
        self.headers = {"Authorization": f"OAuth {self.token}",
                        "Content-Type": "application/json"}

    def __get_token_from_file__(self, file_token_name):
        with open(file_token_name, "r", encoding="utf-8") as file:
            return file.readline()

    def create_catalog(self, name):
        params = {"path": name}
        res = requests.put(self.base_path + self.resources_command_path,
                           headers=self.headers,params=params).status_code
        return res

    def delete_catalog(self, name):
        params = {'path': name,
                  'permanently': 'true'}

        res = requests.delete(self.base_path + self.resources_command_path, headers=self.headers,
                              params=params).status_code
        return res


if __name__ == '__main__':
    ...
