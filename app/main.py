import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')

    data = list(filter(lambda item : item['Continent'] == 'South America', data))

    country = input('Type Country => ')
    # print(utils.population_by_country(data, country))
    # result = utils.population_by_country(data, country)
    # print(data)
    labels, data_world = utils.get_column(data, "Country/Territory", "World Population Percentage")
    charts.generate_pie_chart(country, labels, data_world)
    # if len(result) > 0:
    #     country = result[0]
    #     labels, values = utils.get_population(country)
    #     charts.generate_bar_chart(labels, values)

if __name__ == '__main__': # Name project and name execute since the terminal e.g. python3 main.py , then __main__ = main.py
    run()
