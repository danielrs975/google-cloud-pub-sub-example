# This script is the subscriber that is going to listen
# to the messages from the publisher
# Author: Daniel Rodriguez

from google.cloud import pubsub_v1

PROJECT = "publisher-subscriber-lab"
SUBS_NAME = "subscriber"

def sub():
    client = pubsub_v1.SubscriberClient()

    subscription_path = client.subscription_path(PROJECT, SUBS_NAME)

    def callback(message):
        print(
            "Publisher says: {}\n".format(
                message.data.decode(),
            )
        )

        message.ack()
        print("Acknowledged message {}\n".format(message.message_id))

    streaming_pull_future = client.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on {}..\n".format(subscription_path))

    try:
        streaming_pull_future.result()
    except:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    sub()
