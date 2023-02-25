import charts
import read_csv


def run():
  #BAR CHART
  data = read_csv.read_csv("data.csv")
  country = input("INGRESE UN PAÍS")
  country_selected = read_csv.country_selected(data, country)
  labels_bar, values_bar = read_csv.population_by_year(country_selected)
  charts.generate_bar_chart(labels_bar, values_bar, country)

  # PIE CHART
  
  data = list(filter(lambda item: item["Continent"] == "South America", data))
  labels_pie, values_pie = read_csv.get_country_info(data)
  charts.generate_pie_chart(labels_pie, values_pie)

if __name__ == "__main__":
  run()
