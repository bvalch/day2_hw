united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# united_kingdom[1]['capital']='Cardiff'
# print(united_kingdom[1])


# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# n_i={"name": "NI","population": 1811000,"capital": "Belfast"}
# united_kingdom.append(n_i)
# print(united_kingdom)



# 3. Use a loop to print the names of all the countries in the UK.
# for i in range(len(united_kingdom)):
#   print(united_kingdom[i]['name'])


# 4. Use a loop to find the total population of the UK.
# population_list=[]
# for i in range(len(united_kingdom)):
#   population_list.append(united_kingdom[i]['population'])
# print(sum(population_list))