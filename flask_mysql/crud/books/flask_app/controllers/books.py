from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.author import Author
from flask_app.models.book import Book