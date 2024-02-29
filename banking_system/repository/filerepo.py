import os
import json
from banking_system.repository.base import Repo

FILE_DB = os.path.join(os.getcwd(), 'file_db.json')

class FileRepo(Repo):
    def __init__(self, account_obj) -> None:
        self.account_obj = account_obj

    def create(self):
        try:
            data = []
            with open(FILE_DB, 'r+') as f:
                try:
                    data = json.load(f)
                except Exception as ex:
                    pass
            with open(FILE_DB, 'w') as f:
                data.append(self.account_obj.to_dict())
                json.dump(data, f)
        except Exception as ex:
            raise ex

    def update(self):
        pass

    def list(self):
        pass

    def delete(self):
        pass

