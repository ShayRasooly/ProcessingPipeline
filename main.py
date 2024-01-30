from Parser import JSONParser
from Enricher import Enricher

def main():
    records_list = JSONParser('sample_data.json').parse()
    Enricher().enrich(records_list)
    print(records_list[-1])


if __name__ == '__main__':
    main()
