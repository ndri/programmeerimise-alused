from pyowm import OWM

owm = OWM("sinutoken")
mgr = owm.weather_manager()

observation = mgr.weather_at_place("Tartu, Estonia")
w = observation.weather

print(w.detailed_status)