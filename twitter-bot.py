import tweepy
import datetime
import json
from pathlib import Path

print("Starting Twitter Script")

contents = Path('config.json').read_text()
parsed_json = json.loads(contents)

CONSUMER_KEY = parsed_json["consumer-key"]
CONSUMER_SECRET = parsed_json["consumer-secret"]
ACCESS_KEY = parsed_json["access-key"]
ACCESS_SECRET = parsed_json["access-secret"]


def createTalkText(talks):
    countTalks = str(len(talks))

    talkTerm = 'talks'
    if countTalks == 1:
        talkTerm = 'talk'

    text = '\nWe will have ' + countTalks + ' ' + talkTerm + ': '

    for talk in talks:
        text = text + '\n * ' + talk["speaker"] + ' with "' + talk["talk"] + '".'
    return text


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

current_date = datetime.datetime.now()

day = parsed_json["day-of-meetup"]
month = parsed_json["month-of-meetup"]
year = parsed_json["year-of-meetup"]
meetupDate = datetime.datetime(year, month, day)

URL = parsed_json["url"]
LOCATION = parsed_json["location"]
CITY = parsed_json["city"]

talks = parsed_json["talks"]

TALKS_SENTENCE = createTalkText(talks)

print(current_date)
print(meetupDate)

message = ''
if current_date.year == meetupDate.year:
    if current_date < meetupDate:
        currentCalendarWeek = current_date.isocalendar()[1]
        meetupCalendarWeek = meetupDate.isocalendar()[1]

        if current_date.day == meetupDate.day:
            message = 'Today is the day of the #meetup here in {CITY} at {LOCATION}. {TALKS_SENTENCE} \nFeel free to join us!'
        elif current_date.day == 1:
            message = 'This month we will have #meetup here in {CITY} at {LOCATION}. {TALKS_SENTENCE} \nWe hope to see you there!'
        elif current_date.weekday() == 3 and currentCalendarWeek == meetupCalendarWeek:
            message = 'This week we will have our #meetup here in {CITY} at {LOCATION}. {TALKS_SENTENCE}'

if '' != message:
    message = (message + ' \n\nRegister on: ' + URL)
    message = message.replace('{TALKS_SENTENCE}', TALKS_SENTENCE)
    message = message.replace('{LOCATION}', LOCATION)
    message = message.replace('{CITY}', CITY)

    api.update_status(message)

