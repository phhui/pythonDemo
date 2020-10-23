

import asyncio
import websockets
import logging
import json

logging.basicConfig()
STATE={"value":0}
ulist=set()
ulist=[]
unum=0

def state_event():
    return json.dumps({"type":"state",**STATE})

def users_event():
    return json.dumps({"type":"users","count":len(ulist)})

def msg_event(msg):
    return json.dumps({"type":"toUser","msg":msg})

async def notify_state():
    if ulist:
        message=state_event()
        await asyncio.wait([user.send(message) for user in ulist])

async def notify_users():
    if ulist:
        message=users_event()
        await asyncio.wait([user.send(message) for user in ulist])

async def notify_msg(msg):
    if ulist:
        message=msg_event(msg)
        await asyncio.wait([ulist[0].send(message)])

async def register(websocket):
    ulist.append(websocket)
    await notify_users()

async def unregister(websocket):
    ulist.pop(websocket)
    await notify_users()

async def counter(websocket,path):
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data=json.loads(message)
            if data["action"]=="minus":
                STATE["value"]-=1
                await notify_state()
            elif data["action"]=="plus":
                STATE["value"]+=1
                await notify_state()
            elif data["action"]=="toUser":
                await notify_msg(data["msg"])
            else:
                logging.error("unsupported event:{}",data)
    finally:
        await unregister(websocket)

start_server=websockets.serve(counter,"localhost",6789)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
