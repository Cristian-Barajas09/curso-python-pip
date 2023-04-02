import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item:item['Continent'] == 'South America',data))
    print("escoja una de las opciones")
    print("1. escojer un pais")
    print("2. detodo el mundo")
    opcion = input("digite su opcion: ")
    match (opcion):
        case "1":
            country = input("indica el pais => ")

            result = utils.population_by_country(data,country)

            if len(result) > 0:
                country = result[0]
                labels,values = utils.get_population(country)

                charts.generate_bar_chart(country['Country/Territory'],labels,values)
        case "2":
            countries = list(map(lambda x: x['Country/Territory'],data))
            percentages = list(map(lambda x: x ['World Population Percentage'],data))
            charts.genereta_pie_chart(country['Country/Territory'],percentages)
if __name__ == "__main__":
    run()