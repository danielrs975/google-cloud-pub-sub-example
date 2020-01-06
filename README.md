# Simple publisher-subscriber app using Google Cloud

This is a simple app written in python that has two scripts:

1. publisher.py: that is in charge to take a message from the standard input and published to the cloud

2. subscriber.py: listen endlessly for messages from the publisher

This app use Google Cloud publisher-subscriber tool to save the messages in the cloud and let all the subscriber
read this messages not matter when they start to listen

## Set up the app

Just run the file configure.sh with the next command
```source ./configure.sh```

## Author

Daniel Rodriguez
