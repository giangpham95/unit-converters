from flask import Flask, render_template, request, jsonify
from unit_converter import UnitConverterManager
from units import UNITS

app = Flask(__name__)

unit_converter_manager = UnitConverterManager()

@app.route('/')
def index():
  unit_categories = UNITS
  return render_template('content.html', categories=unit_categories)

@app.route('/convert', methods=['POST'])
def convert():
  category = request.form.get('unit_category')
  from_unit = request.form.get('from_unit')
  to_unit = request.form.get('to_unit')
  amount = request.form.get('amount')
  converter = unit_converter_manager.get_converter(category)
  result = converter.convert(from_unit, to_unit, amount)
  ans = {
    "from_unit": from_unit,
    "to_unit": to_unit,
    "original_amount": amount,
    "converted_amount": result
  }
  return jsonify(ans)

if __name__ == '__main__':
  app.run()