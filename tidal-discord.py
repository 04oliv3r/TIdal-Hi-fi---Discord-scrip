from pypresence import Presence
import subprocess
import time

client_id = "" # ID discord
RPC = Presence(client_id)
RPC.connect()

PLAYER = "chromium.instance2"  # Playerctl name

def get_metadata(field):
    try:
        result = subprocess.check_output(["playerctl", "-p", PLAYER, "metadata", field])
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None

def get_status():
    try:
        result = subprocess.check_output(["playerctl", "-p", PLAYER, "status"])
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None

while True:
    status = get_status()
    if status == "Playing":
        title = get_metadata("title")
        artist = get_metadata("artist")
        if title and artist:
            RPC.update(
                details=f"🎧 {title}",
                state=f"de {artist}",
                large_image="tidal",  # Debes haber subido una imagen con nombre 'tidal' en Discord Dev Portal
                large_text="Escuchando en Tidal"
            )
    else:
        RPC.clear()

    time.sleep(15)

