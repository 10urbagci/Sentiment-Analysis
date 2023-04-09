# Sentiment Analysis 

<p>The tweets about the John Wick 4 movie were collected using the Twitter API. Data came as JSON. The JSON was parsed and the desired data was retrieved. JSON data has been converted to CSV files. This data was then written to a single CSV file.</p>

<p>The data_parse.py script does the json-csv conversion. The merge.py script writes data from all CSV files into a single CSV file.</p>

<p>A small dataset was used for this project. The tweets about #JohnWick from the Twitter API were analyzed. Then data cleaning was done. The #, @ expressions and images were cleaned and removed from the data set.</p>

<p>For sentiment analysis, Hugging Face Transformers model <a href="https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment" target="_blank">nlptown/bert-base-multilingual-uncased-sentiment</a> was used.</p>

<p>A pre-trained model was used for sentiment analysis. The model was not retrained.</p>

<p>While the model gave good results for some tweets, it did not work well for some tweets. I have a small dataset, there are missing and low quality data in some places. In the following stages, I will try this model and different models with a larger and higher quality dataset.</p>
