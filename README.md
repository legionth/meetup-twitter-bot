# Meetup Twitter Bot

A simple bot which post messages on a twitter account.
The scripts purpose is to be used in a Cron-like environment.

## Quick usage 

Just adapt the `config.json` with the relevant data.

```json
{
  "consumer-key": "<copy-the-key-from-your-twitter-api>",
  "consumer-secret": "<copy-the-key-from-your-twitter-api>",
  "access-key": "<copy-the-key-from-your-twitter-api>",
  "access-secret": "<copy-the-key-from-your-twitter-api>",
  "day-of-meetup": 1,
  "month-of-meetup": 5,
  "year-of-meetup": 2020,
  "url": "https://www.meetup.com/Web-Engineering-Aachen/events/263961813/",
  "location": "@home",
  "city": "#Aachen",
  "talks": [
    {
      "speaker": "@legionth",
      "talk": "Are there hats?"
    },
    {
      "speaker": "@WebEngAc",
      "talk": "Why your colleagues could be vampires"
    }
  ]
}
```


## General

This project is used to create tweets for meetup events like
[Web Engineering Aachen](https://www.meetup.com/Web-Engineering-Aachen/)
based on the talks, location and time.

The script will create tweets for different time with time-related messages:

* At the beginning of the month for the event
* At the beginning of the week for the event
* At the day of the event

The script should be used in a `daily` cron job.


## Contribution

Want to contribute? Great!

Feel free to open a Pull Request or an Issue to get in touch.

## License

See [license file](/LICENSE)