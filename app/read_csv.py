import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        # print(header)
        for row in reader:
            iterable = zip(header, row) # join
            # print(list(iterable))
            country_dict = {key: value for key, value in iterable} # List comprenhension
            data.append(country_dict)
            # print(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])