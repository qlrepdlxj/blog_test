from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/VoiceKit-7faf87d99333.json"
def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    content = u'전체적으로 같은 장면을 두고도 장점과 아쉬움이 맞붙어있다.'
    
    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))
