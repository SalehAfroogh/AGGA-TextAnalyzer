import nltk
import ssl

# Disable SSL verification to fix SSL errors
ssl._create_default_https_context = ssl._create_unverified_context

# Download the stopwords resource
nltk.download('stopwords')

print("Stopwords downloaded successfully!")

from nltk.corpus import stopwords
print(stopwords.words('english')[:10])  # Should print the first 10 stopwords
