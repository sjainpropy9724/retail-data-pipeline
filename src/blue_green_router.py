import json
import pipeline_v1
import pipeline_v2

def route_traffic():
  with open("config/traffic_router.json", "r") as f:
    config = json.load(f)

  active = config["active_slot"]
  print(f"--- Routing Prediction Traffic to: {active.upper()} --- ")

  if active == "blue":
    return pipeline_v1.run_pipeline()
  elif active == "green":
    return pipeline_v2.run_pipeline()
  else:
    raise ValueError(f"Unknown slot: {active}")

if __name__ == "main":
  route_traffic()
