

# 8-4
def describe_city (city, country ='usa'):
    """Describe a city"""
    msg = f"{city.title()} is in {country.title()}"
    print(msg)

describe_city('new york')
describe_city('reykjavik', 'iceland')
describe_city('albany')
 