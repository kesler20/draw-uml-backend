import string
import random
from typing import Callable, Optional
from pub_sub._types import MQTTMessage
from config import *
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class MQTTClient(object):
    """AWS IoT MQTT Clients using TLSv1.2 Mutual Authentication

    to implement the client you cna subscribe to a channel and 
    implement some logic within a loop i.e.:

    ```python   

    client = MQTTClient() 
    client.subscribe_to_topic("device/control",cb)
    flag = 0
    while True:
        try:
            # application running in the loop
            if flag:
                client.publish_data("device/data","hello world")
            ...
        except AWSIoTPythonSDK.exception.AWSIoTExceptions.subscribeTimeoutException:
            pass
    ```

    The client is connected when the constructor is called, and can be disconnected using the tear_down method
    """

    def __init__(self) -> None:
        self._clientID = self._generate_clientID()
        self._client: AWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(self._clientID)
        self._connect_client()

    @property
    def clientID(self) -> str:
        return self._clientID

    def _generate_clientID(self, length: int = 8) -> str:
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def _connect_client(self) -> None:
        self._client.configureEndpoint(END_POINT, 8883)
        self._client.configureCredentials(
            PATH_TO_ROOT_CA, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)
        self._client.connect(keepAliveIntervalSecond=900)

    def _tear_down(self, *topics) -> None:
        for topic in topics:
            self._client.unsubscribe(topic)
        self._client.disconnect()

    def publish_data(self, topic: str, payload: str, quos: Optional[int] = 0) -> None:
        """publish to the given topic

        Params
        ---
        topic: str
            the topic which the client listens too
        payload: str
            the payload which will be sent
        quos: int
            Quality of Service set to 0 (at most once) as default

        Returns
        ---
        None 

        Note
        ---
        if you want to pass a dictionary as payload

        ```python
        import json

        json.dumps(my_dict)
        ```
        if you want to pass a pandas data frame

        ```python
        import pandas as pd
        df = pd.DataFrame([1,2])
        df.to_json()
        ```
        """
        self._client.publish(topic, payload, quos)

    def subscribe_to_topic(self, topic: str, custom_callback, quos: Optional[int] = 1) -> None:
        """subscribe to the given topic

        Params
        ---
        topic: str 
            the topic which the client listens too
        custom_callback: func
            the function which will be called anytime a new message arrives
        quos: int
            Quality of Service set to 1 (At least once) as default

        Returns
        ---
        None 

        Note
        ---
        Callback functions should be of the following form:
        ```python
        ```
        where message has properties message.payload and message.topic"""

        self._client.subscribe(topic, quos, custom_callback)
