from flask import Flask, render_template
from unit_converter import UnitConverterManager
from units import UNITS

app = Flask(__name__)

unit_converter_manager = UnitConverterManager()

@app.route('/')
def index():
  unit_categories = UNITS
  return render_template('content.html', categories=unit_categories)

@app.route('/updateUnitOnCategoryChange')
def get_unit():
  return "Hello"