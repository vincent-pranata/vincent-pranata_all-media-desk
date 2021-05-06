from flask import Flask, jsonify, render_template, request, redirect, session, url_for
import requests,os,json
from app import app, mainEngine

@app.route('/')
def index():
    return render_template("mainlogin.html")
