# This script is in charge to publish all the
# messages that are comming from standard input
# Author: Daniel Rodriguez

import os
import time

from google.cloud import pubsub_v1

PROYECT = "publisher-subscriber-lab"
TOPIC_NAME = "low-level-lab" 

ref = dict({"num_messages": 0})


def get_callback(api_future, data, ref):

    def callback(api_future):
        try: 
            print(
                "Published message {} now has message ID {}".format(
                    data, api_future.result()
                )
            )
            ref["num_messages"] += 1
        except Exception:
            print(
                "A problem ocurred when publishing {}: {}\n".format(
                    data, api_future.exception()
                )
            )
            raise

    return callback

def pub(message):
    client = pubsub_v1.PublisherClient()
    topic_path = client.topic_path(PROYECT, TOPIC_NAME)

    data = message.encode()


    api_future = client.publish(topic_path, data=data)
    api_future.add_done_callback(get_callback(api_future, data, ref))

    while api_future.running():
        time.sleep(0.5)
        print("Published {} message(s).".format(ref["num_messages"]))

# This method is going to listen for messages in
# the standard input
def read_input():
    while (True):
        message = input("Publish a message: ")
        if (message == "exit"):
            return
        pub(message)

if __name__ == '__main__':
    read_input()
    