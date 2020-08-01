from covid import Covid
covid = Covid()
print("Total active cases: {0}".format(covid.get_total_active_cases()))
print("Total deaths: {0} ".format(covid.get_total_deaths()))
print("Total confirmed cases: {0}".format(covid.get_total_confirmed_cases()))

print(covid.get_status_by_country_name("Mexico"))

print(covid.get_status_by_country_name('US'))
