#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from os import getenv
from models.engine.db_storage import DBStorage



class test_all_db(unittest.TestCase):

    def setUp(self):
        """ """
        self.storage = DBStorage()
        self.storage.reload()


    def test_create(self):
        state = State(name="Arizona")
        states_start = self.storage.all(State)
        self.storage.new(state)
        self.storage.save()
        states_end = self.storage.all(State)
        self.assertEqual(len(states_end) - len(states_start), 1)

        city = City(state_id=state.id, name="San Francisco")
        cities_start = self.storage.all(City)
        self.storage.new(city)
        self.storage.save()
        cities_end = self.storage.all(City)
        self.assertEqual(len(cities_end) - len(cities_start), 1)

        user = User(email="john@snow.com", password="johnpwd")
        users_start = self.storage.all(User)
        self.storage.new(user)
        self.storage.save()
        users_end = self.storage.all(User)
        self.assertEqual(len(users_end) - len(users_start), 1)

        place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")





if __name__ == "__main__":
    unittest.main()
