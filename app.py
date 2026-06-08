from fastapi import FastAPI
import uuid
import pandas as pd

app = FastAPI()

signals = []

def generate_trace_id():
    return "TRACE_" + str(uuid.uuid4())[:8]

try:

    df = pd.read_csv("data/traffic.csv")

    for index, row in df.iterrows():

        signal = {
            "trace_id": generate_trace_id(),
            "zone_id": row["zone_id"],
            "domain": "traffic",
            "timestamp": "2026-01-01",

            "metrics": {
                "traffic_density": int(row["traffic_density"]),
                "violations": int(row["violations"])
            }
        }

        signals.append(signal)

        print("Signal Generated")
        print("Trace:", signal["trace_id"])
        print("Payload:", signal)

except Exception as e:

    print({
        "error": "INVALID_INPUT",
        "message": str(e)
    })

water_signal = {
    "trace_id": generate_trace_id(),
    "zone_id": "zone_4",
    "domain": "water",
    "timestamp": "2026-01-01",

    "metrics": {
        "water_level": 80
    }
}

flood_signal = {
    "trace_id": generate_trace_id(),
    "zone_id": "zone_5",
    "domain": "flood",
    "timestamp": "2026-01-01",

    "metrics": {
        "risk_level": "high"
    }
}

signals.append(water_signal)
signals.append(flood_signal)

@app.get("/")
def home():
    return {"message": "Signal Layer Running"}

@app.get("/signals")
def get_signals():
    return signals

@app.get("/signal")
def get_signal(zone_id: str):

    for signal in signals:

        if signal["zone_id"] == zone_id:
            return signal

    return {
        "error": "INVALID_INPUT",
        "trace_id": generate_trace_id()
    }
    
    
    
    
    
    
    
    