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

    def update(self, account_id, key, value):

        try:
            data = []
            with open(FILE_DB, 'r+') as f:
                try:
                    data = json.load(f)
                    for each in data:
                        if each.get('customer_account_number') == account_id.get('customer_account_number'):
                            each[key] = each[key]+value
                except Exception as ex:
                    pass
            with open(FILE_DB, 'w') as f:
                json.dump(data, f)
        except Exception as ex:
            raise ex

    def list(self, account_id):
        with open(FILE_DB, 'r') as f:
            for each in json.load(f):
                if each.get('customer_account_number') == account_id:
                    return each

    def delete(self):
        pass

