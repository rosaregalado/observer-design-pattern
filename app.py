class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# WeatherData now implements the subject interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)
    
    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
        self.measurementsChanged()
    
    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Current conditions:", self.temperature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
        
# TODO: implement StatisticsDisplay class and ForecastDisplay class.

class StatisticsDisplay(Observer):
  def __init__(self, weatherData):
      self.temperatures = []
      self.humidities = []
      self.pressures = []
      
      self.weatherData = weatherData
      weatherData.registerObserver(self)
      
  def update(self, temperature, humidity, pressure):
      self.temperatures.append(temperature)
      self.humidities.append(humidity)
      self.pressures.append(pressure)
      self.display()
      
  def display(self):
      print("Avg/Max/Min temperature = {:.1f}/{:.1f}/{:.1f}".format(
          sum(self.temperatures)/len(self.temperatures),
          max(self.temperatures),
          min(self.temperatures)
      ))
      print("Avg/Max/Min humidity = {:.1f}/{:.1f}/{:.1f}".format(
          sum(self.humidities)/len(self.humidities),
          max(self.humidities),
          min(self.humidities)
      ))
      print("Avg/Max/Min pressure = {:.1f}/{:.1f}/{:.1f}".format(
          sum(self.pressures)/len(self.pressures),
          max(self.pressures),
          min(self.pressures)
      ))


class ForecastDisplay(Observer):
  def __init__(self, weatherData):
      self.forecast_temperature = 0
      self.forecast_humidity = 0
      self.forecast_pressure = 0
      
      self.weatherData = weatherData
      weatherData.registerObserver(self)
      
  def update(self, temperature, humidity, pressure):
      self.forecast_temperature = temperature + 0.11 * humidity + 0.2 * pressure
      self.forecast_humidity = humidity - 0.9 * humidity
      self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
      self.display()
      
  def display(self):
      print("Forecast conditions:", self.forecast_temperature, 
            "F degrees and", self.forecast_humidity,"[%] humidity",
            "and pressure", self.forecast_pressure)



    
class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        
        # TODO: Create two objects from StatisticsDisplay class and 
        # ForecastDisplay class. Also, register them to the concrete instance
        # of the Subject class so they get the measurements' updates.
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)
        
        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.
        
        # The ForecastDisplay class shows the weather forecast based on the current
        # temperature, humidity and pressure. Use the following formulas :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        
        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)
        
        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()

