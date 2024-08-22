from flask import Flask, jsonify, request
from db_queries import (
    get_indicators, get_sexes, get_groue_age, get_regions,
    get_departments, get_sous_prefectures, get_region_name,
    get_department_name, get_sous_prefecture_name, get_geographical_entity_name
)
import config as cf


from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)






