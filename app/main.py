import utils
import read_csv
import charts
import pandas as pd
def run():
    data = read_csv.read_csv('data.csv')
    # data = list(filter(lambda item:item['Continent'] == 'South America',data))
    print("escoja una de las opciones")
    print("1. escojer un pais")
    print("2. detodo el mundo")
    opcion = input("digite su opcion: ")
    if opcion == "1":
        country = input("indica el pais => ")
        result = utils.population_by_country(data,country)
        if len(result) > 0:
            country = result[0]
            labels,values = utils.get_population(country)
            charts.generate_bar_chart(country['Country/Territory'],labels,values)
    elif "2":
        # countries = list(map(lambda x: x['Country/Territory'],data))
        # percentages = list(map(lambda x: x ['World Population Percentage'],data))
        df = pd.read_csv('data.csv')
        df = df[df['Continent'] == 'South America']
        countries = df['Country/Territory'].values
        percentages = df['World Population Percentage'].values
        charts.genereta_pie_chart(countries,percentages)
if __name__ == "__main__":
    run()