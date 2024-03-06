import os
import json
from banking_system.repository.base import Repo



class FileRepo(Repo):
    def __init__(self, file_db=None) -> None:
        self.file_db = os.path.join(os.getcwd(), 'file_db.json') if not file_db else file_db

    def create(self, account_details):
        try:
            data = []
            with open(self.file_db, 'r+') as f:
                try:
                    data = json.load(f)
                except Exception as ex:
                    pass
            with open(self.file_db, 'w') as f:
                data.append(account_details)
                json.dump(data, f)
        except Exception as ex:
            raise ex

    def update(self, account_id, key, value):

        try:
            data = []
            with open(self.file_db, 'r+') as f:
                try:
                    ret_data = {}
                    data = json.load(f)
                    for each in data:
                        if each.get('customer_account_number') == account_id:
                            each[key] = each[key]+value
                            ret_data.update(each)
                except Exception as ex:
                    pass
            with open(self.file_db, 'w') as f:
                json.dump(data, f)

            return ret_data
        except Exception as ex:
            raise ex

    def list(self, account_id):
        with open(self.file_db, 'r') as f:
            for each in json.load(f):
                if each.get('customer_account_number') == account_id:
                    return each

    def delete(self):
        pass

def get_file_db():
    return FileRepo()