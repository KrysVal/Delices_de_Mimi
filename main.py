# coding: utf-8


import contextlib
from flask import abort, Flask, redirect, render_template, request, url_for, jsonify, make_response
from os.path import dirname, join
import sqlite3
import json
import os, subprocess
import csv
import sys
import fnmatch
import re
from time import time
from multiprocessing import Process


app = Flask(__name__)
#DB_NAME = join(dirname(__file__), "database/tb_transmission.db")



################################################
# 		Définition des vues du site
################################################




@app.route("/",methods=['GET', 'POST'])
def root():

	''' Vue de la page d'acceuil '''
	return render_template("root.html")

@app.route("/panier", methods=['GET', 'POST'])
def panier():

	''' Vue de la page du panier '''
	return render_template("panier.html")

@app.route("/compte", methods=['GET', 'POST'])
def compte():

	''' Vue de la page de comptes '''
	return render_template("compte.html")

@app.route("/gateaux", methods=['GET', 'POST'])
def gateaux():

	''' Vue de la page des gateaux '''
	return render_template("gateaux.html")

@app.route("/buches", methods=['GET', 'POST'])
def buches():

	''' Vue de la page des gateaux '''
	return render_template("buches.html")

