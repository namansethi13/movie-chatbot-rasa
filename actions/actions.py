from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.shared.nlu.constants import ENTITIES
import requests
import json
import random
from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv('api_key')
class ActionGetMovieDetails(Action):

    def name(self) -> Text:
        return "action_get_movie_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        r = random.randint(0,999)
        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"
        ## http://www.omdbapi.com/?apikey=83060e55&s=hitman
        myResponse = requests.get(url)
        # print(json.loads(myResponse.text))
        movie_info = json.loads(myResponse.text)
        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie names {movie_name}")
            return [SlotSet("movie_name", None)]
        
        title = movie_info["Title"]
        dispatcher.utter_message(text=f"Here is some info about {title}")
        if(movie_info["Poster"] != "NA"):
            dispatcher.utter_message(image=movie_info["Poster"])

        response_parts = [title ]

        if movie_info["Released"] != "NA":
            response_parts.append(f" was released on {movie_info['Released']}.")

        if movie_info["Genre"] != "NA":
            response_parts.append(f" Genre of the movie is {movie_info['Genre']}.")

        if movie_info["Director"] != "NA":
            response_parts.append(f" Directed by {movie_info['Director']}.")

        dispatcher.utter_message(text=f"".join(response_parts))
        if movie_info["Plot"] != "NA":
            dispatcher.utter_message(text=f"{movie_info['Plot']}")
        dispatcher.utter_message(text=f"Let me know if you need any more info about {title}")



        return []
    



class ActionGetDirector(Action):

    def name(self) -> Text:
        return "action_get_movie_director"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"
        ## http://www.omdbapi.com/?apikey=83060e55&s=hitman
        myResponse = requests.get(url)
        # print(json.loads(myResponse.text))
        movie_info = json.loads(myResponse.text)
        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie names {movie_name}")
            return [SlotSet("movie_name", None)]
        
        title = movie_info["Title"]
        dispatcher.utter_message(text=f"Director of the {title} is {movie_info['Director']}")



        return []
    

class ActionGetMovieYear(Action):

    def name(self) -> Text:
        return "action_get_movie_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]
        
        title = movie_info["Title"]
        release_year = movie_info["Year"]
        dispatcher.utter_message(text=f"The movie '{title}' was released in {release_year}")

        return []
    


class ActionGetMovieRated(Action):

    def name(self) -> Text:
        return "action_get_movie_rated"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]
        
        title = movie_info["Title"]
        movie_rated = movie_info["Rated"]
        dispatcher.utter_message(text=f"The movie '{title}' is rated '{movie_rated}'")

        return []


class ActionGetMovieGenre(Action):

    def name(self) -> Text:
        return "action_get_movie_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]
        
        title = movie_info["Title"]
        genre = movie_info["Genre"]
        dispatcher.utter_message(text=f"The movie '{title}' belongs to the genre: {genre}")

        return []


class ActionGetMovieWriter(Action):

    def name(self) -> Text:
        return "action_get_movie_writer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')

        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        writer = movie_info["Writer"]
        dispatcher.utter_message(text=f"The movie '{title}' was written by {writer}")

        return []


class ActionGetMovieDirector(Action):

    def name(self) -> Text:
        return "action_get_movie_director"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')

        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        director = movie_info["Director"]
        dispatcher.utter_message(text=f"The movie '{title}' was directed by {director}")

        return []


class ActionGetMovieActors(Action):

    def name(self) -> Text:
        return "action_get_movie_actors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        actors = movie_info["Actors"]
        dispatcher.utter_message(text=f"The movie '{title}' features the following actors: {actors}")

        return []


class ActionGetMoviePlot(Action):

    def name(self) -> Text:
        return "action_get_movie_plot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        plot = movie_info["Plot"]
        dispatcher.utter_message(text=f"The plot of the movie '{title}' is: {plot}")

        return []


class ActionGetMovieLanguage(Action):

    def name(self) -> Text:
        return "action_get_movie_language"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        language = movie_info["Language"]
        dispatcher.utter_message(text=f"The languages of the movie '{title}' are: {language}")

        return []

class ActionGetMovieCountry(Action):

    def name(self) -> Text:
        return "action_get_movie_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        title = movie_info["Title"]
        country = movie_info["Country"]
        dispatcher.utter_message(text=f"The movie '{title}' is from the following country: {country}")

        return []


class ActionGetMoviePoster(Action):

    def name(self) -> Text:
        return "action_get_movie_poster"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        movie_name = tracker.get_slot('movie_name')

        url = f"http://www.omdbapi.com/?apikey={key}&t={movie_name}"

        myResponse = requests.get(url)
        movie_info = json.loads(myResponse.text)

        if movie_info['Response'] == "False":
            dispatcher.utter_message(text=f"Can't find any movie named {movie_name}")
            return [SlotSet("movie_name", None)]

        Image = movie_info["Poster"]
        dispatcher.utter_message(image=f"{Image}")

        return []


class ActionNewMovie(Action):



    def name(self) -> Text:
        return "action_get_new_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            return [SlotSet("movie_name", None)]
    

entities_to_search_for = ["director" , "year" , "rated" , "genre", "writer" , "actor", "plot" , "language" , "country" , "poster" ]


class ActionFindEntities(Action):

    def name(self) -> Text:
        return "action_find_entities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the latest user message
        user_prompt = tracker.latest_message.get("text", "")

        # Process the user prompt using the NLU interpreter
        result = self._get_nlu_interpreter().parse(user_prompt)

        # Extracted entities from NLU result
        extracted_entities = result.get(ENTITIES, [])

        # Filter recognized entities based on the given list
        filtered_entities = [entity for entity in extracted_entities if entity["entity"] in entities_to_search_for]

        # Handle the filtered entities (e.g., send responses)
        if filtered_entities:
            dispatcher.utter_message(text="Found the following relevant entities:")
            for entity in filtered_entities:
                dispatcher.utter_message(text=f"Entity: {entity['entity']}, Value: {entity['value']}")

        return []
