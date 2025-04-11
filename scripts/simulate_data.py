'''import paho.mqtt.client as mqtt
import json
import random
from datetime import datetime
import time

# Configuration MQTT pour ThingsBoard
THINGSBOARD_HOST = "localhost"
ACCESS_TOKEN = "jNA39JEye5v45HHgF1Rd"  # Remplacer par votre token

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

# Génération de données aléatoires
for _ in range(100):
    data = {
        "timestamp": datetime.now().isoformat(),
        "animal_id": random.randint(1, 50),
        "weight": round(random.uniform(50, 200), 2),
        "health_status": random.choice(["healthy", "sick", "recovering"]),
        "reproduction_status": random.choice(["pregnant", "not_pregnant"])
    }
    client.publish("v1/devices/me/telemetry", json.dumps(data))
    time.sleep(1)  # Envoi toutes les secondes

client.disconnect()'''

import paho.mqtt.client as mqtt
import json
import random
import time

# Remplacez ces valeurs par celles fournies par ThingsBoard Cloud
MQTT_BROKER = "demo.thingsboard.io"  # Exemple pour ThingsBoard Cloud demo
MQTT_PORT = 1883                     # Ou 8883 pour TLS
ACCESS_TOKEN = "jNA39JEye5v45HHgF1Rd"  # Token du périphérique dans ThingsBoard Cloud

def on_connect(client, userdata, flags, rc):
    print("Connecté à MQTT Broker avec le code de retour:", rc)
    client.subscribe("v1/devices/me/telemetry")

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# Pour simuler l'envoi de données aléatoires
is_active = [True, False]

try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 1)  # Température entre 20.0 et 30.0°C
        age = random.randint(1, 10)         # Âge entre 1 et 10 ans
        poids = round(random.uniform(40.0, 400.0), 1)  # Poids entre 40.0 et 400.0 kg
        active = random.choice(is_active)
        current_time = int(time.time())
        id = str(random.randint(1, 4))  # Exemple d'ID aléatoire
        payload = json.dumps({
            "temperature": temperature,
            "age": age,
            "poids": poids,
            "active": active,
            "id": id,
            "time": current_time
        })
        
        client.publish("v1/devices/me/telemetry", payload)
        print("Message envoyé :", payload)
        
        time.sleep(10)

except KeyboardInterrupt:
    print("Arrêt de la simulation...")
    client.loop_stop()
    client.disconnect()
import logging
logging.basicConfig(level=logging.INFO)

def run_mqtt_client():
    try:
        logging.info("Connexion au broker MQTT...")
        # ... (votre code)
    except Exception as e:
        logging.error(f"Échec MQTT : {e}")