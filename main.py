from Parser import JSONParser

def main():
    parser = JSONParser('sample_data.json')
    data = parser.parse()

if __name__ == '__main__':
    main()
