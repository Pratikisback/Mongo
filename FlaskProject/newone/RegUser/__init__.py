from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api
import pymongo

from newone import api, app