from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymongo
mongo_uri= "mongodb://localhost:27017/rasaUser"
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

def storedata(sender_id,name,email):
    myclient = pymongo.MongoClient(mongo_uri)
    mydb = myclient["rasaUser"]
    mycol = mydb["userData"]
    myquery = {"sender_id":sender_id}
    newvalue = {"$set" : {"name":name},"$set" : {"email":email}}
    mycol.update_one(myquery,newvalue,upsert=True)

class SubmitUserDetail(Action):

    def name(self) -> Text:
        return "action_submit_user_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender_id = tracker.sender_id
        name= tracker.get_slot("name")
        email= tracker.get_slot("email")

        storedata(sender_id,name,email)
        dispatcher.utter_message(text="We are connecting you to our agent")

        return []
