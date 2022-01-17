import converters

class UnitConverterManager():
  def __init__(self) -> None:
    self._creators = {
      "Distance" : converters.DistanceConverter,
      "Mass": converters.MassConverter,
      "Time": converters.TimeConverter,
      "Force": converters.ForceConverter,
      "Pressure": converters.PressureConverter,
      "Temperature": converters.TemperatureConverter,
      "Speed": converters.SpeedConverter,
      "Volume": converters.VolumeConverter,
      "Energy": converters.EnergyConverter,
      "Digital Storage": converters.DigitalStorageConverter
    }

  def register_format(self, format, converter):
    self._creators[format] = converter
  
  def get_converter(self, format) -> converters.BaseConverter:
    converter = self._creators.get(format)
    if not converter:
      raise ValueError(format)
    return converter()