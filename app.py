from flask import Flask, jsonify
import requests

API_KEY = "1d847b5c18754cefbf0bdbb6e59bfa30"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-07-04&sortBy=publishedAt&apiKey=1d847b5c18754cefbf0bdbb6e59bfa30"
app = Flask(__name__)


# define function here

@app.route('/api/news', methods = ['GET'])
def get_news():

    response = requests.get(url)

    if response.status_code == 200:

        ##Copying all the codes from google collab
        news_data = response.json() #Convert json data to python dictionary

        #extracting information
        total_articles = len(news_data['articles'])
        first_article = news_data['articles'][0]
        author = first_article['author']
        title = first_article['title']
        publishedAt = first_article['publishedAt']

        output_data = {"Total Article Count":total_articles,
                    "Title":title,
                    "Author":author,
                    "Published Date":publishedAt}
        
        return jsonify(output_data)
    
    else:
        return jsonify({"msg":"Invalid API key."})



if __name__=='__main__':
    app.run(debug=True)