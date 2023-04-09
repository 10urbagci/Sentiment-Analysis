import json
import csv

def convert_json_to_csv(json_file, csv_file, headers):
  
    #Open CSV file
    with open(csv_file, "w", newline="", encoding="utf-8") as output_file:
        
        #specifying the column headers of the CSV file
        csv_writer = csv.writer(output_file)
        
        #A list called "headers" is created to hide the order of the data to be written to the CSV file.
        csv_writer.writerow(headers)
        
        # Open JSON file
        with open(json_file, "r", encoding="utf-8") as input_file:
            data = json.load(input_file)

            # get tweet object
            tweets = data["globalObjects"]["tweets"]
            
            # loop for each tweet
            for tweet_id in tweets:
                tweet = tweets[tweet_id]
                # get tweet data
                created_at = tweet["created_at"]
                id = tweet["id"]
                full_text = tweet["full_text"]
                lang = tweet["lang"]
               
                # write csv file
                csv_writer.writerow([created_at,id,full_text,lang])
#Write the name of the json file you want to return csv
json_file = "1681041550018797700.json"
#specify the name of the newly created CSV file
csv_file = "1681041550018797700.csv"
headers = ["created_at","id","full_text","lang",]

#call function
convert_json_to_csv(json_file, csv_file, headers)