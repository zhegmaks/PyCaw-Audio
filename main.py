from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from fastapi import FastAPI, Body, status, Query
from fastapi.responses import JSONResponse, FileResponse

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
app = FastAPI()

@app.get("/")
async def main():
    return FileResponse("index.html")

@app.get("/api/getvolume")
async def getvolume():
    pycaw = PyCawAudio()
    return pycaw.getvolume()

@app.get("/api/mute")
async def mute():
    pycaw = PyCawAudio()
    pycaw.setmute(1, None)
    return {"muted": True}

@app.get("/api/unmute")
async def unmute():
    pycaw = PyCawAudio()
    pycaw.setmute(0, None)
    return {"unmuted": True}

@app.get("/api/setvolume")
async def set_volume(volume: int = Query(le = 100, ge = 0)):
    obj = PyCawAudio()
    obj.setvolume(volume)
    return {"volume": volume}

@app.get("/api/getmute")
async def get_mute(volume: int = Query(le=100, ge=0)):
    obj = PyCawAudio()
    obj.getmute(volume)
    return {"volume": volume}

class PyCawAudio:
    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PyCawAudio, cls).__new__(cls)
        return cls.instance

    def setvolume(self, value):  # value from 0.0 to -64 (100 - 0 volume)
        scalarVolume = int(value) / 100
        volume.SetMasterVolumeLevelScalar(scalarVolume, None)
        return value
    
    def getvolume(self):
        self.volume = int(round(volume.GetMasterVolumeLevelScalar() * 100))
        return self.volume

    def setmute(self, arg1, arg2):
        volume.SetMute(arg1, arg2) # 1 - mute, 0 - unmute

    def getmute(self):
        volume.GetMute()
