import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import re
text = "Nick likes to play football, however he is not too fond of tennis."
import re
text = re.sub(r'[^\w\s]', '', text)
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)