class BaseConverter(object):
  conversions = {}

  def convert(self, from_unit, to_unit, amount):
    return float(amount) / float(self.conversions[from_unit]) * float(self.conversions[to_unit])

class TemperatureConverter(BaseConverter):

  # conversions is not used for conversion since temperature
  # is not converted with a scalar
  conversions = {
    'K': 1.0
  }

  def convert(self, from_unit, to_unit, amount):
    temperature_kevin = 0

    if from_unit == 'K':
      temperature_kevin = amount
    elif from_unit == 'C':
      temperature_kevin = amount + 273.15
    elif from_unit == 'F':
      temperature_kevin = (amount + 459.67) * 9.0 / 5.0
    else:
      return None

    if to_unit == 'K':
      return temperature_kevin
    elif to_unit == 'C':
      return temperature_kevin - 273.15
    elif to_unit == 'F':
      return temperature_kevin * 9.0 / 5.0 - 459.67
    else:
      return None

class DistanceConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'ym': 1000000000000000000000000,
    'zm': 1000000000000000000000,
    'am': 1000000000000000000,
    'fm': 1000000000000000,
    'pm': 1000000000000,
    'nn': 1000000000,
    '\u03BCm': 1000000,
    'mm': 1000,
    'cm': 100,
    'dm': 10,
    'm': 1.0,
    'dam': 0.1,
    'hm': 0.01,
    'km': 0.001,
    'Mm': 0.000001,
    'Gm': 0.000000001,
    'Tm': 0.000000000001,
    'Pm': 0.000000000000001,
    'Em': 0.000000000000000001,
    'Zm': 0.000000000000000000001,
    'Ym': 0.000000000000000000000001,

    'th': 39370.078740157,
    'inch': 39.3701,
    'li': 4.9709595959548,
    'ft': 3.28094,
    'yd': 1.09361,
    'rd': 1.0 / 5.0292,
    'ch': 1.0 / 20.1168,
    'fur': 1.0 / 201.168,
    'mi': 0.000621371,

    'ly': 1.0 / (9.4607304725808 * (10**15))
  }

class VolumeConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'yl': 1000000000000000000000000,
    'zl': 1000000000000000000000,
    'al': 1000000000000000000,
    'fl': 1000000000000000,
    'pl': 1000000000000,
    'nl': 1000000000,
    '\u03BCl': 1000000,
    'ml': 1000,
    'cl': 100,
    'dl': 10,
    'l': 1.0,
    'dal': 0.1,
    'hl': 0.01,
    'kl': 0.001,
    'Ml': 0.000001,
    'Gl': 0.000000001,
    'Tl': 0.000000000001,
    'Pl': 0.000000000000001,
    'El': 0.000000000000000001,
    'Zl': 0.000000000000000000001,
    'Yl': 0.000000000000000000000001,

    'floz': 33.8140226,
    'gi': 8.4535056755,
    'pt': 2.1133764099325,
    'qt': 1.05668821,
    'gal': 1.0 / 3.7854118
  }

class MassConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'yg': 1000000000000000000000000,
    'zg': 1000000000000000000000,
    'ag': 1000000000000000000,
    'fg': 1000000000000000,
    'pg': 1000000000000,
    'ng': 1000000000,
    '\u03BCg': 1000000,
    'mg': 1000,
    'cg': 100,
    'dg': 10,
    'g': 1.0,
    'dag': 0.1,
    'hg': 0.01,
    'kg': 0.001,
    'Mg': 0.000001,
    'Gg': 0.000000001,
    'Tg': 0.000000000001,
    'Pg': 0.000000000000001,
    'Eg': 0.000000000000000001,
    'Zg': 0.000000000000000000001,
    'Yg': 0.000000000000000000000001,

    'gr': 15.4323583529,
    'dr': 8.4535056755,
    'oz': 1.0 / 29.5735596875,
    'lb': 1.0 / 453.59237,
    'st': 1.0 / 6350.29318,
    'qtr': 1.0 / 12700.58636,
    'cwt': 1.0 / 50802.34544,
    't': 1.0 / 907185
  }

class TimeConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'ys': 1000000000000000000000000,
    'zs': 1000000000000000000000,
    'as': 1000000000000000000,
    'fs': 1000000000000000,
    'ps': 1000000000000,
    'ns': 1000000000,
    '\u03BCs': 1000000,
    'ms': 1000,
    'cs': 100,
    'ds': 10,
    's': 1.0,
    'das': 0.1,
    'hs': 0.01,
    'ks': 0.001,
    'Ms': 0.000001,
    'Gs': 0.000000001,
    'Ts': 0.000000000001,
    'Ps': 0.000000000000001,
    'Es': 0.000000000000000001,
    'Zs': 0.000000000000000000001,
    'Ys': 0.000000000000000000000001,

    'min': 1.0 / 60,
    'hour': 1.0 / 60 / 60,
    'day': 1.0 / 60 / 60 / 24,
    'week': 1.0 / 60 / 60 / 24 / 7
  }


class PressureConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'at': 1.0197162129779,
    'bar': 1.0,
    'mbar': 1000.0,
    '\u03BCbar': 1000000.0,
    'Pa': 100000.0,
    'hPa': 1000.0,
    'kPa': 100.0,
    'MPa': 0.1,
    'kgcm2': 1.0197162129779,
    'atm': 0.98692326671601,
    'mmHg': 750.06156,
    'mmH2O': 10197.162129779,
    'mH2O': 10.197162129779,
    'psi': 14.503773800722,
    'ftH2O': 33.455256555148,
    'inH2O': 401.46307866177,
    'inHg': 29.529983071445,
    'Torr': 750.061682704
  }

class EnergyConverter(BaseConverter):
  # watt is the standard unit
  conversions = {
    'yW': 1000000000000000000000000,
    'zW': 1000000000000000000000,
    'aW': 1000000000000000000,
    'fW': 1000000000000000,
    'pW': 1000000000000,
    'nW': 1000000000,
    '\u03BCW': 1000000,
    'mW': 1000,
    'cW': 100,
    'dW': 10,
    'W': 1.0,
    'daW': 0.1,
    'hW': 0.01,
    'kW': 0.001,
    'MW': 0.000001,
    'GW': 0.000000001,
    'TW': 0.000000000001,
    'PW': 0.000000000000001,
    'EW': 0.000000000000000001,
    'ZW': 0.000000000000000000001,
    'YW': 0.000000000000000000000001,
    'BTU/s': 3.41214 / 60 / 60,
    'BTU/min': 3.41214 / 60,
    'BTU/hr': 3.41214,
    'hp(E)': 1.0/746.0,
    'hp(M)': 1.0/735.49875,
    'hp(I)': 1.0/745.69987,
    'hp': 1.0/745.69987,
    'hp(S)': 1/9812.5,
    'cal/s': 0.239000573613767,
    'cal/min': 14.34,
    'cal/hr': 860.42,
    'kCal/s': 0.0002388458966275,
    'kCal/min':  0.01433075379765,
    'kCal/hr': 0.85984522785899,
    'erg/s': 10000000,
    'erg/min': 60000000,
    'erg/hr': 36000000000,
    'ftlb/sec': 0.73756215242247,
    'ftlb/min': 44.25,
    'ftlb/hr': 2655.22,
    'J/s': 1,
    'J/min': 60,
    'J/hr': 3600,
    'kgf-m/s': 0.10197162129779,
    'kgf-m/min': 0.10197162129779 * 60,
    'kgf-m/hr': 0.10197162129779 * 60 * 60,
    'Nm/s': 1,
    'Nm/min':  60,
    'Nm/hr': 3600,
  }

class DigitalStorageConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'b': 8,
    'kb': 8e-3,
    'Mb': 8e-6,
    'Gb': 8e-9,
    'Tb': 8e-12,
    'Pb': 8e-15,
    'Eb': 8e-18,
    'Zb': 8e-21,
    'Yb': 8e-24,
    'kib': 128,
    'Mib': 128 * 1024,
    'Gib': 128 * (1024 ** 2),
    'Tib': 128 * (1024 ** 3),
    'Pib': 128 * (1024 ** 4),
    'Eib': 128 * (1024 ** 5),
    'Zib': 128 * (1024 ** 6),
    'Yib': 128 * (1024 ** 7),
    'B': 1.0,
    'kB': 1e-3,
    'MB': 1e-6,
    'GB': 1e-9,
    'TB': 1e-12,
    'PB': 1e-15,
    'EB': 1e-18,
    'ZB': 1e-21,
    'YB': 1e-24,
    'kiB': 1024 ** -1,
    'MiB': 1024 ** -2,
    'GiB': 1024 ** -3,
    'TiB': 1024 ** -4,
    'PiB': 1024 ** -5,
    'EiB': 1024 ** -6,
    'ZiB': 1024 ** -7,
    'YiB': 1024 ** -8
  }

class SpeedConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'm/s': 0.3048,
    'km/h': 1.09728,
    'mph': 0.681818,
    'kn': 0.592484,
    'ft/s': 1
  }

class ForceConverter(BaseConverter):
  # meter is the standard unit
  conversions = {
    'N': 1.0,
    'kN': 1.0 / 1000.0,
    'MN': 1.0 / 1000000.0,
    'GN': 1.0 / 1000000000.0,
    'gf': 1.019716213e+2,
    'kgf': 1.019716213e-1,
    'dyn': 1e+5,
    'J/m': 1.0,
    'J/cm': 100.0,
    'shortTonF': 1.1240445e-4,
    'longTonF': 1.003611e-4,
    'kipf': 2.248089e-4,
    'lbf': 2.248089431e-1,
    'ozf': 3.5969430896,
    'pdl': 7.2330138512
  }

