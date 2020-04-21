# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionCovidState(Action):

    def name(self) -> Text:
        return "action_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        response = requests.get("https://api.covid19india.org/data.json").json()
        entities = tracker.latest_message['entities']
        print(entities)
        
        name = []        
        for e in entities:
           if e['entity'] == 'state':
              name = e['value']
 
        for data in response['statewise']:
           if data['state'] == name.title():
               print(data)
               message = "Active: "+data['active']+"Confirmed: "+data['confirmed']+"Deaths: "+data['deaths']+"Delta Confirmed: "+data['deltaconfirmed']+"Delta Deaths: "+data['deltadeaths']+"Delta Recovered: "+data['deltarecovered']+"Last update time: "+data['lastupdatedtime']+"Recovered: "+data['recovered']+"state notes: "+data['statenotes']

        dispatcher.utter_message(text=message)

        return []
