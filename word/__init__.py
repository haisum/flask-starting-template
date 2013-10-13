from flask import Blueprint

bp_word = Blueprint('bp_word', __name__, template_folder="templates")
import word.views