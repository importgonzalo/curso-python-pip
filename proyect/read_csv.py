import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    array = []
    for row in reader:
      iter = zip(header, row)
      dict_country = dict(iter)
      array.append(dict_country)
    return array


def get_country_info(data):
  country_name = list(map(lambda item: item["Country/Territory"], data))
  country_percentage = list(
    map(lambda item: item["World Population Percentage"], data))
  labels = country_name
  values = country_percentage
  return labels, values

def population_by_year(country_selected):
  dict_population = {
  "2022":int(country_selected["2022 Population"]),
  "2020":int(country_selected["2020 Population"]),
  "2015":int(country_selected["2015 Population"]),
  "2010":int(country_selected["2010 Population"]),
  "2000":int(country_selected["2000 Population"]),
  "1990":int(country_selected["1990 Population"]),
  "1980":int(country_selected["1980 Population"]),
  "1970":int(country_selected["1970 Population"])
  }
  labels = dict_population.keys()
  values = dict_population.values()
  return labels, values

def country_selected(data, country):
  country_selected = list(filter(lambda item: item["Country/Territory"] == country, data))
  return country_selected[0]

if __name__ == "__main__":
  path = "./proyect/data.csv"
  data = read_csv(path)
  country = "Colombia"
  labels, values = get_country_info(data, country)
  print(labels, values)
