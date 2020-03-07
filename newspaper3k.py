import newspaper

volkskrant = newspaper.build('https://www.volkskrant.nl/', language='nl')

print(volkskrant.size())

for category in volkskrant.category_urls():
    print(category)

for article in volkskrant.articles:
    print(article.url)

print('\n')

print(newspaper.hot(), end='\n\n')
print(newspaper.popular_urls(), end='\n\n')

print(newspaper.languages())

# url = 'https://www.volkskrant.nl/nieuws-achtergrond/eerste-dode-in-nederland-maar-wat-is-eigenlijk-de-kans-om-aan-corona-te-overlijden~bf716564/'
# article = newspaper.Article(url)
# article.download()

# article.parse()
# print(article.authors)
# article.publish_date
# article.text
# article.top_image

# article.nlp()
# article.keywords
# article.summary