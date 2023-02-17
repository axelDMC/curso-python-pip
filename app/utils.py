def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def get_column(data, name_column_a, name_column_b):
    data_label = list(map(lambda x: x[name_column_a], data))
    data_column = list(map(lambda x: x[name_column_b], data))
    
    # data_label = [item[name_column_a] for item in data]
    # data_column = [float(item[name_column_b]) for item in data]
    # data_column = []
    # for item in data:
        # data_column.append(item[name_column])
    print(data_label, data_column)
    return data_label, data_column

