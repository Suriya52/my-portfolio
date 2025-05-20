"""a=10
b=20
c=a+b
print(c)
print("This is sample file....")
print (id(a))
print (id(b))

s=input("Enter your Name:")
print("Your Name is {}".format(s))"""

import requests

def search_google(query, api_key, cx):
    # Google Custom Search API URL
    url = "https://www.googleapis.com/customsearch/v1"
    
    # Parameters for the API request
    params = {
        "q": query,
        "key": api_key,
        "cx": cx
    }
    
    # Send the request to Google Custom Search API
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract search results
    results = []
    if 'items' in data:
        for item in data['items']:
            title = item.get('title')
            snippet = item.get('snippet')
            link = item.get('link')
            results.append(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
    else:
        results.append("No results found.")
    
    return "\n".join(results)

# Example usage
api_key = "YOUR_GOOGLE_API_KEY"      # we want to add our api key here
cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"  # we want to add search engine id here
query = input("Enter a query to search on Google: ") # add our query here...
result = search_google(query, api_key, cx)
print("\nGoogle Search Results:\n")
print(result)
