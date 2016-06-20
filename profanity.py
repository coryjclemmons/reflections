import urllib

def read_text():
    quotes = open("/Users/coryclemmons/Downloads/movie_quotes.txt")
    contents_of_file = quotes.read()
#    print(contents_of_file)
#    bad ="shit"

#    quote_details = str(quotes)
#    print(quote_details)    

#    if bad in contents_of_file:
#        print("Profanity Alert!")
#    else:
#        print("no profanity in the document")

    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
        
read_text()

