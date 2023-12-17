highest_rated = data.sort_values(by=["Star Rating"], 
                                 ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])