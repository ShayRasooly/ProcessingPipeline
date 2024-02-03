import json
from collections import defaultdict


class Publisher:
    def publish(self):
        pass


class PrintPublisher(Publisher):
    def publish(self, entries_list: list[defaultdict]):
        for entry in entries_list:
            print(json.dumps(entry, indent=4))
