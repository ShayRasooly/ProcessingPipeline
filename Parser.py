from collections import defaultdict
import json


class Parser:
    def __init__(self):
        pass

    def parse(self) -> defaultdict:
        pass


class JSONParser(Parser):

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def parse(self):
        data_dict = defaultdict(lambda: None)
        with open(self.file_path, 'r') as f:
            data_dict.update(json.load(f)[0])
        return data_dict
