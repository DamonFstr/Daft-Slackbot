# Daft Slackbot

This is a Slackbot that will scrape Daft.ie based on some criteria that you set, then alert you in Slack. The competitive housing market requires you to be quick and this will help you be notified of any new listings fast. I created this to get to grips with building Slackbots in Python.

The get listings method used in this repo is from https://github.com/AnthonyBloomer/daftlistings and the documentation for this lies here https://anthonybloomer.github.io/daftlistings/.

## Configuration
`settings.py` contains the configuration settings for the bot. 

## Slack Setup
Before using this bot, you'll need a Slack team, a channel for the bot to post into, and a Slack API key:

* [Create a Slack team](https://slack.com/create#email)
* [Create a channel](https://get.slack.help/hc/en-us/articles/201402297-Creating-a-channel) for the listings to be posted into. #daftsearch is the default name of the channel but this can be configured in `settings.py`
* [Get a Slack API token](https://api.slack.com/docs/oauth-test-tokens)