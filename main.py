# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 04:43:21 2019

@author: acham
"""
import pandas as pd
import os
from flask import Flask, request, redirect, flash, render_template, send_from_directory, url_for
from os.path import exists
#from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag

import time
import json
from flask import jsonify
import copy

import numpy as np
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)



with open('./data/movie_list.json') as f:
    rec = json.load(f)


with open('./data/show_list.json') as f:
    show = json.load(f)

with open('./data/music_list.json') as f:
    musical = json.load(f)
    
with open('./data/random_list.json') as f:
    other = json.load(f)
    
@app.route("/", methods=["GET", "POST"])
def start():
    return render_template("index.html")
    
@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")
    
@app.route("/shows", methods=["GET", "POST"])
def shows():

    final = []
    rec1 = ''
    for key, value in show.items():
    # #print(value)
        for k,v in value.items():
            if k == "description":
                final.append(value)
            
        show1 = json.dumps(final)
        
    show1 = json.loads(show1)
    return render_template("shows.html", table_results = show1)
    
    
    
@app.route("/music", methods=["GET", "POST"])
def music():
    final = []
    rec1 = ''
    for key, value in musical.items():
    # #print(value)
        for k,v in value.items():
            if k == "description":
                final.append(value)
            
        music1 = json.dumps(final)
        
    music1 = json.loads(music1)
    return render_template("music.html", table_results = music1)

@app.route("/random", methods=["GET", "POST"])
def random():
    final = []
    rec1 = ''
    for key, value in other.items():
    # #print(value)
        for k,v in value.items():
            if k == "description":
                final.append(value)
            
        random1 = json.dumps(final)
        
    random1 = json.loads(random1)

    return render_template("random.html", table_results=random1)

@app.route("/movies", methods=["GET", "POST"])
def movies():
    final = []
    rec1 = ''
    for key, value in rec.items():
    # #print(value)
        for k,v in value.items():
            if k == "description":
                final.append(value)
            
        rec1 = json.dumps(final)
        
    rec1 = json.loads(rec1)
    
    return render_template("movies.html", table_results = rec1)



if __name__ == "__main__":
    app.run()
