   import requests
   import json
   import time
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   # Replace with your actual API key from a geolocation service like ipstack or ipinfo
   GEOLOCATION_API_KEY = 'c270276f05df285a15ef0cc3da2b9eed'
   GEOLOCATION_API_URL = 'http://api.ipstack.com/'

   # Function to get geolocation data based on IP address
   def get_geolocation(ip_address):
       response = requests.get(f'{GEOLOCATION_API_URL}{ip_address}?access_key={GEOLOCATION_API_KEY}')
       if response.status_code == 200:
           data = response.json()
           return {
               'ip': data.get('ip'),
               'city': data.get('city'),
               'region_name': data.get('region_name'),
               'country_name': data.get('country_name'),
               'latitude': data
