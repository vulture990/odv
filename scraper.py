from requests_html import HTMLSession
class Scraper():
    def scrapedata(self,tag):
        url=f'https://quotes.toscrape.com/tag/{tag}'
        # send a request to this url and get the response in html format
        session = HTMLSession()
        r = session.get(url)
        # find all the divs with class quote
        quotes = r.html.find('div.quote')
        # create a list to store the quotes
        quotes_list = []
        # loop through the quotes and extract the text and author
        for quote in quotes:
            text = quote.find('span.text', first=True).text

            author = quote.find('small.author', first=True).text
            # create a dictionary with the keys text and author
            # and append it to the list
            quotes_list.append({'text': text, 'author': author})
        # return the list of quotes
        return quotes_list


# LETS test out an example
s=Scraper()
print(s.scrapedata('life'))