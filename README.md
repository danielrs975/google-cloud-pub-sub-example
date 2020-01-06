# Simple publisher-subscriber app using Google Cloud

This is a simple app written in python that has two scripts:

1. publisher.py: that is in charge to take a message from the standard input and published to the cloud

2. subscriber.py: listen endlessly for messages from the publisher

This app use Google Cloud publisher-subscriber tool to save the messages in the cloud and let all the subscriber
read this messages not matter when they start to listen

## Set up the app

1. Run the file configure.sh with the next commands ```source ./configure.sh``` and ```source ./set_env.sh```.

2. Log in you google cloud account and create a topic with the name 'low-level-lab'.

3. Inside that topic create a subscriber and call it 'subscriber'.

4. Create a key to access to your project from python. This is done inside accounts services.

5. Put the key in the root of the app and change the name to 'key.json'.

6. In the two scripts change the value of the project variable to the name of your project in your google cloud console

7. Test the scripts.

## Author

Daniel Rodriguez
