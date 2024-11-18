#download train route names and principal destinations from the Amtrak website

amtrak_routes_url = 'https://www.amtrak.com/routes.html'

#store h3 tag class name that contains the route names
h3_route_name_class = 'feature-overview-card__text_title'

#store the h4 tag class name that contains the principal destinations
#not needed for this application but may come in handy later on
h4_destinations_class = 'feature-overview-info__paragraph_title'

#import web scraping modules
import bs4, requests, sys, csv

#download the amtrak routes page
webpage = requests.get(amtrak_routes_url)

#was download successful?
if webpage.status_code != 200:
    print("Web page failed to download.")
    sys.exit(-999)

#parse the page
parsed_data = bs4.BeautifulSoup(webpage.text, 'html.parser')

#get all the h3 tags in a list
route_name_list = list(parsed_data.findAll("h3", class_ = h3_route_name_class))

#to get the corresponding list of destination, navigate to <a> tag containing
#this <h3> tag, then get the nextSibling (which is a \n) and then get the nextSibling
#which is the <div> tag immediately below the <h3> tag, whose class is
#'feature-overview-card_text'. Then the <div> element below that, whose class is
#'feature-overview-info__paragraphText" contains the <h4> tag that has the list
#of destination cities


#now print out rhe results
for route in route_name_list:
    print('Train: {}'.format(route.text))
    #navigate to <h4> element below current <h3> element
    #and print the list of destination cities
    a_tag = route.parent
    sibling1 = a_tag.nextSibling # \n
    sibling2 = sibling1.nextSibling
    h4_div = sibling2.div
    cities = h4_div.h4.get_text()
    print("\tRoute: " + cities)



