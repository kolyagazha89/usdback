import asyncio
import os
import time

import cv2

from av import VideoFrame

from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer, MediaRelay, MediaBlackhole

from fastapi import APIRouter
from ultralytics import YOLO

from rtc import ntt
from rtc.schemas import Offer

ROOT = os.path.dirname(__file__)
router = APIRouter(
    prefix="/rtc",
    tags=["Rtc"]
)
model = YOLO("C:\\Users\Шнырь\Desktop\\usd\yolo8\\runs\detect\\train\weights\\best.pt")
pcs = set()
pc = RTCPeerConnection()
pcs.add(pc)
recorder = MediaBlackhole()
relay = MediaRelay()


class VideoTransformTrack(MediaStreamTrack):
    kind = "video"

    def __init__(self, track):
        super().__init__()
        self.track = track

    async def recv(self):
        frame = await self.track.recv()
        img = frame.to_ndarray(format="bgr24")
        results = model(img, save_crop=True)
        if(results[0]):
            if(dc.readyState=="open"):
                new_frame = VideoFrame.from_ndarray(img, format="bgr24")
                new_frame.pts = frame.pts
                new_frame.time_base = frame.time_base
                dc.send(ntt.text_rec(r"C:/Users/Шнырь/Desktop/usd/backend/runs/detect/predict/crops/num/image0.jpg"))
                await pc.close()
                pcs.discard(pc)
                return new_frame
        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame



@router.post("/offer_cv")
async def offer(params: Offer):
    offer = RTCSessionDescription(sdp=params.sdp, type=params.type)

    @pc.on("datachannel")
    async def on_datachannel(evt, message=None):
        if(evt.readyState=="open"):
            global dc
            dc=evt


    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        print("Connection state is %s" % pc.connectionState)
        if pc.connectionState == "failed":
            await pc.close()
            pcs.discard(pc)

    @pc.on("track")
    def on_track(track):
        if track.kind == "video":
            pc.addTrack(
                VideoTransformTrack(relay.subscribe(track))
            )

        @track.on("ended")
        async def on_ended():
            await recorder.stop()

    # handle offer
    await pc.setRemoteDescription(offer)
    await recorder.start()

    # send answer
    answer = await pc.createAnswer()
    await pc.setRemoteDescription(offer)
    await pc.setLocalDescription(answer)

    return {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}


args = ''

@router.on_event("shutdown")
async def on_shutdown():
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()
