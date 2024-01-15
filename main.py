import asyncio
import contextlib
import os
import json
import importlib
import sys
from highrise import ResponseError
import contextlib
import random
import logging
import socket
from random import randrange
from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *
from typing import Any, Dict, Union
from keep_alive import keep_alive

keep_alive()
from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
    AnchorPosition,
    BaseBot,
    Position,
    Reaction,
    ResponseError,
    User,
    CurrencyItem,
    GetMessagesRequest,
    Item,
)
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
)
{}
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import time

moderators = ["BeIgium", "Shyxbaby"]


# ...
async def on_chat(message):
  time.sleep(20)
  # ... rest of your code ...


class Bot(BaseBot):
  continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}
  user_data: Dict[int, Dict[str, Any]] = {}
  EMOTE_DICT = {
      "charging": "emote-charging",
      "energyball": "emote-energyball",
      "fashionista": "emote-fashionista",
      "flex": "emoji-flex",
      "flirtywave": "emote-lust",
      "float": "emote-float",
      "frog": "emote-frog",
      "gravedance": "dance-weird",
      "gravity": "emote-gravity",
      "greedy": "emote-greedy",
      "hello": "emote-hello",
      "hot": "emote-hot",
      "icecream": "dance-icecream",
      "kiss": "emote-kiss",
      "kpop": "dance-blackpink",
      "lambi": "emote-superpose",
      "laugh": "emote-laughing",
      "letsgo": "dance-shoppingcart",
      "maniac": "emote-maniac",
      "model": "emote-model",
      "no": "emote-no",
      "ogdance": "dance-macarena",
      "pennydance": "dance-pennywise",
      "pose1": "emote-pose1",
      "pose2": "emote-pose3",
      "pose3": "emote-pose5",
      "pose4": "emote-pose7",
      "pose5": "emote-pose8",
      "punkguitar": "emote-punkguitar",
      "raisetheroof": "emoji-celebrate",
      "russian": "dance-russian",
      "sad": "emote-sad",
      "savage": "dance-tiktok8",
      "shuffle": "dance-tiktok10",
      "shy": "emote-shy",
      "singalong": "idle_singing",
      "sit": "idle-loop-sitfloor",
      "snowangel": "emote-snowangel",
      "snowball": "emote-snowball",
      "swordfight": "emote-swordfight",
      "telekinesis": "emote-telekinesis",
      "teleport": "emote-teleporting",
      "thumbsup": "emoji-thumbsup",
      "tired": "emote-tired",
      "tummyache": "emoji-gagging",
      "viral": "dance-tiktok9",
      "wave": "emote-wave",
      "weird": "dance-weird",
      "worm": "emote-snake",
      "wrong": "dance-wrong",
      "yes": "emote-yes",
      "zombierun": "emote-zombierun",
      "ANGRY": "emoji-angry",
      "BOW": "emote-bow",
      "CASUAL": "idle-dance-casual",
      "CHARGING": "emote-charging",
      "CONFUSION": "emote-confused",
      "CURSING": "emoji-cursing",
      "CURTSY": "emote-curtsy",
      "CUTEY": "emote-cutey",
      "DONT": "dance-tiktok2",
      "EMOTECUTE": "emote-cute",
      "ENERGYBALL": "emote-energyball",
      "ENTHUSED": "idle-enthusiastic",
      "FASHIONISTA": "emote-fashionista",
      "FLEX": "emoji-flex",
      "FLIRTYWAVE": "emote-lust",
      "FLOAT": "emote-float",
      "FROG": "emote-frog",
      "GRAVEDANCE": "dance-weird",
      "GRAVITY": "emote-gravity",
      "GREEDY": "emote-greedy",
      "HELLO": "emote-hello",
      "HOT": "emote-hot",
      "ICECREAM": "dance-icecream",
      "KISS": "emote-kiss",
      "KPOP": "dance-blackpink",
      "LAMBI": "emote-superpose",
      "LAUGH": "emote-laughing",
      "LETSGO": "dance-shoppingcart",
      "MANIAC": "emote-maniac",
      "MODEL": "emote-model",
      "NO": "emote-no",
      "OGDANCE": "dance-macarena",
      "PENNYDANCE": "dance-pennywise",
      "POSE1": "emote-pose1",
      "POSE2": "emote-pose3",
      "POSE3": "emote-pose5",
      "POSE4": "emote-pose7",
      "POSE5": "emote-pose8",
      "PUNKGUITAR": "emote-punkguitar",
      "RAISETHEROOF": "emoji-celebrate",
      "RUSSIAN": "dance-russian",
      "SAD": "emote-sad",
      "SAVAGE": "dance-tiktok8",
      "SHUFFLE": "dance-tiktok10",
      "SHY": "emote-shy",
      "SINGALONG": "idle_singing",
      "SIT": "idle-loop-sitfloor",
      "SNOWANGEL": "emote-snowangel",
      "SNOWBALL": "emote-snowball",
      "SWORDFIGHT": "emote-swordfight",
      "TELEKINESIS": "emote-telekinesis",
      "TELEPORT": "emote-teleporting",
      "THUMBSUP": "emoji-thumbsup",
      "TIRED": "emote-tired",
      "TUMMYACHE": "emoji-gagging",
      "VIRAL": "dance-tiktok9",
      "WAVE": "emote-wave",
      "WEIRD": "dance-weird",
      "WORM": "emote-snake",
      "WRONG": "dance-wrong",
      "YES": "emote-yes",
      "ZOMBIERUN": "emote-zombierun",
      "Angry": "emoji-angry",
      "Bow": "emote-bow",
      "Casual": "idle-dance-casual",
      "Charging": "emote-charging",
      "Confusion": "emote-confused",
      "Cursing": "emoji-cursing",
      "Curtsy": "emote-curtsy",
      "Cutey": "emote-cutey",
      "Dont": "dance-tiktok2",
      "Emotecute": "emote-cute",
      "Energyball": "emote-energyball",
      "Enthused": "idle-enthusiastic",
      "Fashionista": "emote-fashionista",
      "Flex": "emoji-flex",
      "Flirtywave": "emote-lust",
      "Float": "emote-float",
      "Frog": "emote-frog",
      "Gravedance": "dance-weird",
      "Gravity": "emote-gravity",
      "Greedy": "emote-greedy",
      "Hello": "emote-hello",
      "Hot": "emote-hot",
      "Icecream": "dance-icecream",
      "Kiss": "emote-kiss",
      "Kpop": "dance-blackpink",
      "Lambi": "emote-superpose",
      "Laugh": "emote-laughing",
      "Letsgo": "dance-shoppingcart",
      "Maniac": "emote-maniac",
      "Model": "emote-model",
      "No": "emote-no",
      "Ogdance": "dance-macarena",
      "Pennydance": "dance-pennywise",
      "Pose1": "emote-pose1",
      "Pose2": "emote-pose3",
      "Pose3": "emote-pose5",
      "Pose4": "emote-pose7",
      "Pose5": "emote-pose8",
      "Punkguitar": "emote-punkguitar",
      "Raisetheroof": "emoji-celebrate",
      "Russian": "dance-russian",
      "Sad": "emote-sad",
      "Savage": "dance-tiktok8",
      "Shuffle": "dance-tiktok10",
      "Shy": "emote-shy",
      "Singalong": "idle_singing",
      "Sit": "idle-loop-sitfloor",
      "Snowangel": "emote-snowangel",
      "Snowball": "emote-snowball",
      "Swordfight": "emote-swordfight",
      "Telekinesis": "emote-telekinesis",
      "Teleport": "emote-teleporting",
      "Thumbsup": "emoji-thumbsup",
      "Tired": "emote-tired",
      "Tummyache": "emoji-gagging",
      "Viral": "dance-tiktok9",
      "Wave": "emote-wave",
      "Weird": "dance-weird",
      "Worm": "emote-snake",
      "Wrong": "dance-wrong",
      "Yes": "emote-yes",
      "Zombierun": "emote-zombierun",
      "sayso": "idle-dance-tiktok4",
      "Sayso": "idle-dance-tiktok4",
      "SAYSO": "idle-dance-tiktok4",
      "uwu": "idle-uwu",
      "UWU": "idle-uwu",
      "Uwu": "idle-uwu",
      "zerogravity": "emote-astronaut",
      "Zerogravity": "emote-astronaut",
      "zero gravity": "emote-astronaut",
      "Zero gravity": "emote-astronaut",
      "boxer": "emote-boxer",
      "ditzy": "emote-pose9",
      "Boxer": "emote-boxer",
      "Ditzy": "emote-pose9",
      "surprise": "emote-pose6",
      "celebration": "emote-celebrationstep",
      "Surprise": "emote-pose6",
      "Celebration": "emote-celebrationstep",
      "airguitar": "idle-guitar",
      "Airguitar": "idle-guitar",
      "Saunter sway": "dance-anime",
      "saunter sway": "dance-anime",
      "Penguin": "dance-pinguin",
      "penguin": "dance-pinguin",
      "Creepy puppet": "dance-creepypuppet",
      "creepy puppet": "dance-creepypuppet",
      "Watch your back": "emote-creepycute",
      "Watch your back": "emote-creepycute",
      "Creepy puppet": "dance-creepypuppet",
      "creepy puppet": "dance-creepypuppet",
      "Revelations": "emote-headblowup",
      "revelations": "emote-headblowup",
      "Stargazing": "emote-stargazer",
      "stargazing": "emote-stargazer",
      "Star gazing": "emote-stargazer",
      "star gazing": "emote-stargazer",
      "Star": "emote-stargazer",
      "star": "emote-stargazer",
      "Bashful": "emote-shy2",
      "bashful": "emote-shy2",
      "Party time": "emote-celebrate",
      "party time": "emote-celebrate",
  }
  continuous_emote_task = None

  def __init__(self):
    super().__init__()
    # Initialize user data dictionary
    self.joined_users = []  # List to store joined user data
    self.user_reactions = {}
    self.command_modules = {}  # A dictionary to store the loader
    self.spamming = False
    self.room_dictionary = {
        "room_1": "646dce94304425f9e19f5c42",
        "room_2": "64c56b3f93191a44cc2aaa53",
    }
    self.developer_usernames = ["JustSneak", "onlyHELL"]
    self.allowed_usernames = ["JustSneak", "onlyHELL"]
    self.moderators = ["JustSneak", "onlyHELL"]  
    self.invite_message = ''# Add more usernames to this list if needed

  OUTFITS = [[
      Item('clothing', 1, 'body-flesh', True, 26),
      Item('clothing', 1, 'eye-n_basic2018malesquaresleepy', False, 7),
      Item('clothing', 1, 'eyebrow-n_basic2018newbrows07', False, 7),
      Item('clothing', 1, 'nose-n_basic2018newnose05', False, 7),
      Item('clothing', 1, 'mouth-basic2018chippermouth', False, 7),
      Item('clothing', 1, 'watch-n_room32019blackwatch', False, 7),
      Item('clothing', 1, 'glasses-n_room12019circleshades', False, 7),
      Item('clothing', 1, 'earrings-n_room12019goldhoops', False, 7),
      Item('clothing', 1, 'hair_back-n_basic2018wavypulledback', False, 7),
      Item('clothing', 1, 'hair_front-n_malenew07', False, 7),
      Item('clothing', 1, 'shirt-n_2016fallblackkknottedtee', True, 7),
      Item('clothing', 1, 'pants-n_room32019highwasittrackshortsblack', False,
           7),
      Item('clothing', 1, 'shoes-n_room22019kneehighsblack', False, 7),
  ]]

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("BOT IN THE ROOM")
    # Create tasks for all three loops
    rizz_loop_task = self.highrise.tg.create_task(self.rizz_loop())
    note_loop_task = self.highrise.tg.create_task(self.note_loop())
    emote_loop_task = self.highrise.tg.create_task(self.emote_loop())

    # Teleport and start all three loops concurrently
    await asyncio.gather(
        self.highrise.teleport(session_metadata.user_id, Position(16.25, 8.55, 4.5, "FrontLeft")),
        rizz_loop_task,
        note_loop_task,
        emote_loop_task
    )

    # If needed, you can wait for the completion of the tasks
    await asyncio.gather(rizz_loop_task, note_loop_task, emote_loop_task)

  async def on_message(self, user_id: str, conversation_id: str,
                       is_new_conversation: bool) -> None:
    response = await self.highrise.get_messages(conversation_id)
    message = ""

    if isinstance(response, GetMessagesRequest.GetMessagesResponse):
      if response.messages:
        message = response.messages[0].content
        print(message)

    if message:
      if message.lower() == "Hey" in message or "hey" in message or "hello" in message or "Hello" in message or "hi" in message or "Hi" in message or "hlo" in message or "Hlo" in message or "hola" in message or "Hola" in message:
        commands = ["Hey!", "Hola!"]
        for command in commands:
          await self.highrise.send_message(conversation_id, command)

      elif message.lower() == "join" in message or "Join" in message or "(join)" in message or "(Join)" in message or "( join )" in message or "( Join )" in message:
        commands = ["You Joined!", "Wait for the RESULT!"]
        for command in commands:
          await self.highrise.send_message(conversation_id, command)

      elif message.lower() == "lista":
        command_list = [
            "Here is the list of commands...", "Emotelist", "Líneas poéticas",
            "Piropos", "Broma", "Asar", "Hecho de la diversión", "año de muerte",
            "porcentaje de amor", "porcentaje de odio", "Iq", "rico",
            "año de boda",
        ]
        for command in command_list:
          await self.highrise.send_message(conversation_id, command)

      elif message.lower() == "emotelista":
        await self.highrise.send_message(conversation_id, "emotelist...")
        await self.highrise.send_message(
            conversation_id,
            "angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\npennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun"
        )

      elif message == "I love you":
        await self.highrise.send_message(conversation_id, "👀")

      else:
        await self.highrise.send_message(conversation_id, "Hola?")

  async def on_user_move(self, user: User, pos: Position) -> None:
    print(f"{user.username} moved to {pos}")

  async def on_user_join(self, user: User,
                         position: Union[Position, AnchorPosition]) -> None:
    await self.highrise.send_whisper(
      user.id, f"\nBienvenido {user.username}\n❤️Escribe ( Join ) en pm‼️ \ntenga la oportunidad de ganar ORO 1K\nNOTA: ¡No envíe mensajes en la sala ni envíe mensajes solo en PM para Join! ❤️") 
    #print(f"{user.username} joined the room standing at {position}")
    await self.highrise.send_emote("emote-lust", user.id)
    await self.send_random_reactions(user.id, num_reactions=1, delay=1.55)

    # tip new users 1g when they join the room
    # await self.tip_new_user(user, 1)

  async def on_tip(self, sender: User, receiver: User,
                   tip: CurrencyItem | Item) -> None:
    print(
        f"{sender.username} tipped {receiver.username} an amount of {tip.amount}"
    )
    await self.highrise.chat(
        f"\n@{sender.username} ᴛɪᴘᴘᴇᴅ {receiver.username}  \n{tip.amount} ɢᴏʟᴅ"
    )

  async def on_emote(self, user: User, emote_id: str,
                     receiver: User | None) -> None:
    print(f"{user.username} emoted: {emote_id}")

  async def on_whisper(self, user: User, message: str) -> None:
    print(f"{user.username} whispered: {message}")
    if message.lower().startswith("/") and user.username in [
        "BeIgium", "Shyxbaby"
    ]:
      text = message.replace("/", "").strip()
      
    if message.lstrip().startswith('on'):
      await self.send_invite_to_all_conversations('655de30c56f4e606dea97f47')
        
    if "Floor 1" in message.lower():
      try:
        await self.highrise.teleport(
            f"{user.id}", Position(7.0, 0.0, 16.0, facing='BackRight'))
      except Exception as e:
        print("error 3:", e)
    elif "333" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}", Position(11.5, 14.25, 9.5))
      except Exception as e:
        print("error 3:", e)
    elif "111" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}", Position(13.5, 6.0, 12.5))
      except Exception as e:
        print("error 3:", e)
    elif "offline" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}",
                                     Position(999.5, 999.75, 999.5))
      except Exception as e:
        print("error 3:", e)

  async def on_reaction(self, user: User, reaction: Reaction,
                        receiver: User) -> None:
    print(f"{user.username} sended the reaction {reaction} to {receiver.username}")
    if receiver.username == "CarlaCantinera":
      if reaction == "heart":
          await self.highrise.react("heart", user.id)
      if reaction == "wink":
        await self.highrise.react("wink", user.id)
      if reaction == "wave":
        await self.highrise.react("wave", user.id)
      if reaction == "clap":
        await self.highrise.react("clap", user.id)
      if reaction == "thumbs":
        await self.highrise.react("thumbs", user.id)
    # text_to_emoji = {
    #     "wink": "¿Un poco travieso, eh? 😉",
    #     "wave": "¡Claro, me encantaría! 👋🍸😉",
    #     "thumbs": "¡Gracias, guapo! 👍😉",
    #     "heart": "Tu amor me hace sonreír y mi corazón latir más fuerte. ❤️😉",
    #     "clap": "¡Aplausos para ti, mi cariño! 👏😘",
    # }
    # await self.highrise.chat(f"\n{receiver.username} {text_to_emoji[reaction]} ")

  async def on_user_leave(self, user: User) -> None:
    print(f"{user.username} Left the Room")
    await self.stop_continuous_emote(user.id)

  async def on_chat(self, user: User, message: str) -> None:
    print(f"{user.username}:{message}")

      
    if message in self.EMOTE_DICT:
      emote_id = self.EMOTE_DICT[message]
      await self.highrise.send_emote(emote_id, user.id)

    if message.startswith("Loop"):
      emote_name = message[5:].strip()
      if emote_name in self.EMOTE_DICT:
        emote_id = self.EMOTE_DICT[emote_name]
        delay = 1
        if " " in emote_name:
          emote_name, delay_str = emote_name.split(" ")
          if delay_str.isdigit():
            delay = float(delay_str)

        if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
            user.id].cancelled():
          await self.stop_continuous_emote(user.id)

        task = asyncio.create_task(
            self.send_continuous_emote(emote_id, user.id, delay))
        self.continuous_emote_tasks[user.id] = task

    elif message.startswith("Stop"):
      if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
          user.id].cancelled():
        await self.stop_continuous_emote(user.id)

        await self.highrise.chat("Continuous emote has been stopped.")
      else:
        await self.highrise.chat("You don't have an active loop_emote.")

    elif message.lower().startswith("Bank"):
      wallet = (await self.highrise.get_wallet()).content
      await self.highrise.chat(
          f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")
    elif message.lower().startswith("Users"):
      room_users = (await self.highrise.get_room_users()).content
      await self.highrise.chat(f"There are {len(room_users)} users in the room"
                               )

    if message.lower().lstrip().startswith(
        ("anime", "fight", "penguin", "flirt", "stars", "gravity", "uwu",
         "zero", "fashion", "icecream", "punk", "wrong", "sayso", "zombie",
         "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance",
         "shuffle", "viral", "weird", "russian", "curtsy", "snowball",
         "sweating", "snowangel", "cute", "worm", "lambi", "celebration",
         "frog", "energyball", "maniac", "teleport", "float", "telekinesis",
         "enthused", "confused", "charging", "shopping", "bow", "savage",
         "kpop", "model", "dont", "pennywise", "flex", "gagging", "greedy",
         "cursing", "kiss")):
      response = await self.highrise.get_room_users()
      users = [content[0] for content in response.content]
      usernames = [user.username.lower() for user in users]
      parts = message[1:].split()
      args = parts[1:]

      if len(args) < 1:
        await self.highrise.send_whisper(user.id,
                                         f"Usage: {parts[0]} <@username>")
        return
      elif args[0][0] != "@":
        await self.highrise.send_whisper(
            user.id, "Invalid user format. Please use '@username'.")
        return
      elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id,
                                         f"{args[0][1:]} is not in the room.")
        return

      user_id = next(
          (u.id for u in users if u.username.lower() == args[0][1:].lower()),
          None)
      if not user_id:
        await self.highrise.send_whisper(user.id,
                                         f"User {args[0][1:]} not found")
        return

      if message.lower().lstrip().startswith("fight"):
        await self.highrise.chat(
            f"\njajajaja \n@{user.username} y @{args[0][1:]}\nBoxeadores/Boxeadoras...🌚"
        )
        await self.highrise.send_emote("emote-boxer", user.id)
        await self.highrise.send_emote("emote-boxer", user_id)

      elif message.lower().lstrip().startswith("penguin"):
        await self.highrise.chat(
            f"\n🫂 @{user.username} y @{args[0][1:]} ambos son pingüinos🐧❤️")
        await self.highrise.send_emote("dance-pinguin", user.id)
        await self.highrise.send_emote("dance-pinguin", user_id)

      elif message.lower().lstrip().startswith("flirt"):
        await self.highrise.chat(
            f"\n Hola @{user.username} y @{args[0][1:]} ambos son pingüinos... 😏❤️"
        )
        await self.highrise.send_emote("emote-lust", user.id)
        await self.highrise.send_emote("emote-lust", user_id)

      elif message.lower().lstrip().startswith("stars"):
        await self.highrise.send_emote("emote-stargazer", user.id)
        await self.highrise.send_emote("emote-stargazer", user_id)

      elif message.lower().lstrip().startswith("zero"):
        await self.highrise.send_emote("emote-astronaut", user.id)
        await self.highrise.send_emote("emote-astronaut", user_id)

      elif message.lower().lstrip().startswith("gravity"):
        await self.highrise.send_emote("emote-gravity", user.id)
        await self.highrise.send_emote("emote-gravity", user_id)

      elif message.lower().lstrip().startswith("uwu"):
        await self.highrise.send_emote("idle-uwu", user.id)
        await self.highrise.send_emote("idle-uwu", user_id)

      elif message.lower().lstrip().startswith("fashion"):
        await self.highrise.send_emote("emote-fashionista", user.id)
        await self.highrise.send_emote("emote-fashionista", user_id)

      elif message.lower().lstrip().startswith("icecream"):
        await self.highrise.send_emote("dance-icecream", user.id)
        await self.highrise.send_emote("dance-icecream", user_id)

      elif message.lower().lstrip().startswith("punk"):
        await self.highrise.send_emote("emote-punkguitar", user.id)
        await self.highrise.send_emote("emote-punkguitar", user_id)

      elif message.lower().lstrip().startswith("wrong"):
        await self.highrise.send_emote("dance-wrong", user.id)
        await self.highrise.send_emote("dance-wrong", user_id)

      elif message.lower().lstrip().startswith("sayso"):
        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

      elif message.lower().lstrip().startswith("zombie"):
        await self.highrise.send_emote("emote-zombierun", user.id)
        await self.highrise.send_emote("emote-zombierun", user_id)

      elif message.lower().lstrip().startswith("cutey"):
        await self.highrise.send_emote("emote-cutey", user.id)
        await self.highrise.send_emote("emote-cutey", user_id)

      elif message.lower().lstrip().startswith("anime"):
        await self.highrise.send_emote("dance-anime", user.id)
        await self.highrise.send_emote("dance-anime", user_id)

      elif message.lower().lstrip().startswith("pose3"):
        await self.highrise.send_emote("emote-pose3", user.id)
        await self.highrise.send_emote("emote-pose3", user_id)

      elif message.lower().lstrip().startswith("pose1"):
        await self.highrise.send_emote("emote-pose1", user.id)
        await self.highrise.send_emote("emote-pose1", user_id)

      elif message.lower().lstrip().startswith("pose7"):
        await self.highrise.send_emote("emote-pose7", user.id)
        await self.highrise.send_emote("emote-pose7", user_id)

      elif message.lower().lstrip().startswith("pose8"):
        await self.highrise.send_emote("emote-pose8", user.id)
        await self.highrise.send_emote("emote-pose8", user_id)

      elif message.lower().lstrip().startswith("dance"):
        await self.highrise.send_emote("idle-dance-casual", user.id)
        await self.highrise.send_emote("idle-dance-casual", user_id)

      elif message.lower().lstrip().startswith("shuffle"):
        await self.highrise.send_emote("dance-tiktok10", user.id)
        await self.highrise.send_emote("dance-tiktok10", user_id)

      elif message.lower().lstrip().startswith("weird"):
        await self.highrise.send_emote("emote-weird", user.id)
        await self.highrise.send_emote("emote-weird", user_id)

      elif message.lower().lstrip().startswith("viralgroove"):
        await self.highrise.send_emote("dance-tiktok9", user.id)
        await self.highrise.send_emote("dance-tiktok9", user_id)

      elif message.lower().lstrip().startswith("cute"):
        await self.highrise.send_emote("emote-cute", user.id)
        await self.highrise.send_emote("emote-cute", user_id)

      elif message.lower().lstrip().startswith("frog"):
        await self.highrise.send_emote("emote-frog", user.id)
        await self.highrise.send_emote("emote-frog", user_id)

      elif message.lower().lstrip().startswith("lambi"):
        await self.highrise.send_emote("emote-superpose", user.id)
        await self.highrise.send_emote("emote-superpose", user_id)

      elif message.lower().lstrip().startswith("celebration"):
        await self.highrise.send_emote("emote-celebrationstep", user.id)
        await self.highrise.send_emote("emote-celebrationstep", user_id)

      elif message.lower().lstrip().startswith("worm"):
        await self.highrise.send_emote("emote-snake", user.id)
        await self.highrise.send_emote("emote-snake", user_id)

      elif message.lower().lstrip().startswith("bow"):
        await self.highrise.send_emote("emote-bow", user.id)
        await self.highrise.send_emote("emote-bow", user_id)

      elif message.lower().lstrip().startswith("energyball"):
        await self.highrise.send_emote("emote-energyball", user.id)
        await self.highrise.send_emote("emote-energyball", user_id)

      elif message.lower().lstrip().startswith("maniac"):
        await self.highrise.send_emote("emote-maniac", user.id)
        await self.highrise.send_emote("emote-maniac", user_id)

      elif message.lower().lstrip().startswith("teleport"):
        await self.highrise.send_emote("emote-teleporting", user.id)
        await self.highrise.send_emote("emote-teleporting", user_id)

      elif message.lower().lstrip().startswith("float"):
        await self.highrise.send_emote("emote-float", user.id)
        await self.highrise.send_emote("emote-float", user_id)

      elif message.lower().lstrip().startswith("telekinesis"):
        await self.highrise.send_emote("emote-telekinesis", user.id)
        await self.highrise.send_emote("emote-telekinesis", user_id)

      elif message.lower().lstrip().startswith("enthused"):
        await self.highrise.send_emote("idle-enthusiastic", user.id)
        await self.highrise.send_emote("idle-enthusiastic", user_id)

      elif message.lower().lstrip().startswith("confused"):
        await self.highrise.send_emote("emote-confused", user.id)
        await self.highrise.send_emote("emote-confused", user_id)

      elif message.lower().lstrip().startswith("shopping"):
        await self.highrise.send_emote("dance-shoppingcart", user.id)
        await self.highrise.send_emote("dance-shoppingcart", user_id)

      elif message.lower().lstrip().startswith("charging"):
        await self.highrise.send_emote("emote-charging", user.id)
        await self.highrise.send_emote("emote-charging", user_id)

      elif message.lower().lstrip().startswith("snowangel"):
        await self.highrise.send_emote("emote-snowangel", user.id)
        await self.highrise.send_emote("emote-snowangel", user_id)

      elif message.lower().lstrip().startswith("sweating"):
        await self.highrise.send_emote("emote-hot", user.id)
        await self.highrise.send_emote("emote-hot", user_id)

      elif message.lower().lstrip().startswith("snowball"):
        await self.highrise.send_emote("emote-snowball", user.id)
        await self.highrise.send_emote("emote-snowball", user_id)

      elif message.lower().lstrip().startswith("curtsy"):
        await self.highrise.send_emote("emote-curtsy", user.id)
        await self.highrise.send_emote("emote-curtsy", user_id)

      elif message.lower().lstrip().startswith("russian"):
        await self.highrise.send_emote("dance-russian", user.id)
        await self.highrise.send_emote("dance-russian", user_id)

      elif message.lower().lstrip().startswith("pennywise"):
        await self.highrise.send_emote("dance-pennywise", user.id)
        await self.highrise.send_emote("dance-pennywise", user_id)

      elif message.lower().lstrip().startswith("dont"):
        await self.highrise.send_emote("dance-tiktok2", user.id)
        await self.highrise.send_emote("dance-tiktok2", user_id)

      elif message.lower().lstrip().startswith("kpop"):
        await self.highrise.send_emote("dance-blackpink", user.id)
        await self.highrise.send_emote("dance-blackpink", user_id)

      elif message.lower().lstrip().startswith("model"):
        await self.highrise.send_emote("emote-model", user.id)
        await self.highrise.send_emote("emote-model", user_id)

      elif message.lower().lstrip().startswith("savage"):
        await self.highrise.send_emote("dance-tiktok8", user.id)
        await self.highrise.send_emote("dance-tiktok8", user_id)

      elif message.lower().lstrip().startswith("flex"):
        await self.highrise.send_emote("emoji-flex", user.id)
        await self.highrise.send_emote("emoji-flex", user_id)

      elif message.lower().lstrip().startswith("gagging"):
        await self.highrise.send_emote("emoji-gagging", user.id)
        await self.highrise.send_emote("emoji-gagging", user_id)

      elif message.lower().lstrip().startswith("greedy"):
        await self.highrise.send_emote("emote-greedy", user.id)
        await self.highrise.send_emote("emote-greedy", user_id)

      elif message.lower().lstrip().startswith("cursing"):
        await self.highrise.send_emote("emoji-cursing", user.id)
        await self.highrise.send_emote("emoji-cursing", user_id)

      elif message.lower().lstrip().startswith("zero"):
        await self.highrise.send_emote("emote-astronaut", user.id)
        await self.highrise.send_emote("emote-astronaut", user_id)

      elif message.lower().lstrip().startswith("kiss"):
        await self.highrise.send_emote("emote-kiss", user.id)
        await self.highrise.send_emote("eote-kiss", user_id)

  #TO_BUY ROOM boost

    if message.lower().startswith(
        "boost") and user.username in self.allowed_usernames:
      response = await self.highrise.buy_room_boost(payment="bot_wallet_only",
                                                    amount=1)
      print(response)
      await self.highrise.send_whisper(user.id, f"The bot have:\n{response}")

    #to buy room voice

    if message.lower().startswith(
        "voice") and user.username in self.allowed_usernames:
      response = await self.highrise.buy_voice_time(payment="bot_wallet_only")
      print(response)
      await self.highrise.send_whisper(user.id, f"The bot have:\n{response}")

    if message.lower().startswith("/come") and user.username in [
        "BeIgium", "Shyxbaby"
    ]:
      response = await self.highrise.get_room_users()
      your_pos = None
      for content in response.content:
        if content[0].id == user.id:
          if isinstance(content[1], Position):
            your_pos = content[1]
            break
      if not your_pos:
        await self.highrise.send_whisper(user.id, "Invalid coordinates!")
        return
      await self.highrise.chat(f"@{user.username} I'm coming Homie...")
      await self.highrise.walk_to(your_pos)

    if message == "!tip1":
      if user.username == "AmISeIfish":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.tip_user(roomUser.id, "gold_bar_1")

    if message.lower().startswith("/g ") and user.username in [
        "BeIgium", "Shyxbaby"
    ]:
      parts = message.split(" ")
      if len(parts) != 2:
        await self.highrise.send_message(user.id, "Invalid command")
        return
      try:
        amount = int(parts[1])
      except:
        await self.highrise.chat("Invalid amount")
      bot_wallet = await self.highrise.get_wallet()
      bot_amount = bot_wallet.content[0].amount
      if bot_amount <= amount:
        await self.highrise.chat("I don't have Hehe")
        return
      bars_dictionary = {
          10000: "gold_bar_10k",
          5000: "gold_bar_5000",
          1000: "gold_bar_1k",
          500: "gold_bar_500",
          100: "gold_bar_100",
          50: "gold_bar_50",
          10: "gold_bar_10",
          5: "gold_bar_5",
          1: "gold_bar_1"
      }
      fees_dictionary = {
          10000: 1000,
          5000: 500,
          1000: 100,
          500: 50,
          100: 10,
          50: 5,
          10: 1,
          5: 1,
          1: 1
      }
      tip = []
      total = 0
      for bar in bars_dictionary:
        if amount >= bar:
          bar_amount = amount // bar
          amount = amount % bar
          for i in range(bar_amount):
            tip.append(bars_dictionary[bar])
            total = bar + fees_dictionary[bar]
      if total > bot_amount:
        await self.highrise.chat("i don't have hehe")
        return
      for bar in tip:
        await self.highrise.tip_user(user.id, bar)

    if message.lower().startswith("heart ") and user.username in [
        "BeIgium", "Shyxbaby"
    ]:
      try:
        # استخراج العدد المطلوب واسم المستخدم من الرسالة
        parts = message.split()
        num_hearts = int(parts[-1])
        target_username = parts[1].strip('@').lower()

        if 1 <= num_hearts <= 100:
          for _ in range(num_hearts):
            target_user = None
            response = await self.highrise.get_room_users()
            for user_info in response.content:
              if user_info[0].username.lower() == target_username:
                target_user = user_info[0]
                break

            if target_user:
              await self.highrise.react("heart", target_user.id)

        else:

          await self.highrise.chat("1  _ 100  only ")
      except ValueError:
        await self.highrise.chat("heart @user")

    if message.lower().startswith("scan ") and user.username in [
        "BeIgium", "Shyxbaby"
    ]:
      parts = message.split(" ")
      if len(parts) != 2:
        await self.highrise.chat(
            "Incorrect format, please use (scan <@username>) Dont give space at last"
        )
        return
      #Removes the @ from the username if it exists
      if parts[1].startswith("@"):
        username = parts[1][1:]
      else:
        username = parts[1]
      #Get the user id from the username
      user = await self.webapi.get_users(username=username, limit=1)
      if user:
        user_id = user.users[0].user_id
      else:
        await self.highrise.chat("User not found, please specify a valid user")
        return

      #Get the user info
      userinfo = await self.webapi.get_user(user_id)
      number_of_followers = userinfo.user.num_followers
      number_of_friends = userinfo.user.num_friends
      number_of_folowing = userinfo.user.num_following
      joined_at = (userinfo.user.joined_at).strftime("%d/%m/%Y %H:%M:%S")
      try:
        last_login = (
            userinfo.user.last_online_in).strftime("%d/%m/%Y %H:%M:%S")
      except:
        last_login = "Last login not available"
      #Get the number of posts and the most liked post
      userposts = await self.webapi.get_posts(author_id=user_id)
      number_of_posts = 0
      most_likes_post = 0
      try:
        while userposts.last_id != "":
          for post in userposts.posts:
            if post.num_likes > most_likes_post:
              most_likes_post = post.num_likes
            number_of_posts += 1
          userposts = await self.webapi.get_posts(
              author_id=user_id, starts_after=userposts.last_id)
      except Exception as e:
        print(e)

      #Send the info to the chat
      await self.highrise.chat(
          f"""\nUser: {username}\nNumber of followers: {number_of_followers}\nNumber of friends: {number_of_friends}\nNumber of following: {number_of_folowing}\nJoined at: {joined_at}\nLast login: {last_login}\nNumber of posts: {number_of_posts}\nMost likes in a post: {most_likes_post}"""
      )

    if message.lower().startswith("!sps"):
      choices = ['stone', 'paper', 'scissors']
      client_chosen = random.choice(choices)
      option = message[5:].strip().lower()

      text_to_emoji = {"stone": "✊", "paper": "✋", "scissors": "✌️"}
      if option not in choices:
        response = f"Invalid command usage:\nExample: !sps <{client_chosen}>\nAvailable Options:\n{', '.join(choices)}"
        await self.highrise.send_whisper(user.id, response)
        return
      elif option == client_chosen:
        response = "No One Wins Draw 🤝"
      elif (option == "stone" and client_chosen == "scissors") or (
          option == "paper"
          and client_chosen == "stone") or (option == "scissors"
                                            and client_chosen == "paper"):
        response = f"\nWell done, you won! 🎉\nYou: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
      else:
        response = f"\nyou lost 😢\nYou: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"

      await self.highrise.chat(response)

    emote_mapping = {
        "/charging": "emote-charging",
        "/energyball": "emote-energyball",
        "/fashionista": "emote-fashionista",
        "/flex": "emoji-flex",
        "/flirtywave": "emote-lust",
        "/float": "emote-float",
        "/frog": "emote-frog",
        "/gravedance": "dance-weird",
        "/gravity": "emote-gravity",
        "/greedy": "emote-greedy",
        "/hello": "emote-hello",
        "/hot": "emote-hot",
        "/icecream": "dance-icecream",
        "/kiss": "emote-kiss",
        "/kpop": "dance-blackpink",
        "/lambi": "emote-superpose",
        "/laugh": "emote-laughing",
        "/letsgo": "dance-shoppingcart",
        "/maniac": "emote-maniac",
        "/model": "emote-model",
        "/no": "emote-no",
        "/ogdance": "dance-macarena",
        "/pennydance": "dance-pennywise",
        "/pose1": "emote-pose1",
        "/pose2": "emote-pose3",
        "/pose3": "emote-pose5",
        "/pose4": "emote-pose7",
        "/pose5": "emote-pose8",
        "/punkguitar": "emote-punkguitar",
        "/raisetheroof": "emoji-celebrate",
        "/russian": "dance-russian",
        "/sad": "emote-sad",
        "/savage": "dance-tiktok8",
        "/shuffle": "dance-tiktok10",
        "/shy": "emote-shy",
        "/singalong": "idle_singing",
        "/sit": "idle-loop-sitfloor",
        "/snowangel": "emote-snowangel",
        "/snowball": "emote-snowball",
        "/swordfight": "emote-swordfight",
        "/telekinesis": "emote-telekinesis",
        "/teleport": "emote-teleporting",
        "/thumbsup": "emoji-thumbsup",
        "/tired": "emote-tired",
        "/tummyache": "emoji-gagging",
        "/viral": "dance-tiktok9",
        "/wave": "emote-wave",
        "/weird": "dance-weird",
        "/worm": "emote-snake",
        "/wrong": "dance-wrong",
        "/yes": "emote-yes",
        "/zombierun": "emote-zombierun",
        "/ANGRY": "emoji-angry",
        "/BOW": "emote-bow",
        "/CASUAL": "idle-dance-casual",
        "/CHARGING": "emote-charging",
        "/CONFUSION": "emote-confused",
        "/CURSING": "emoji-cursing",
        "/CURTSY": "emote-curtsy",
        "/CUTEY": "emote-cutey",
        "/DONT": "dance-tiktok2",
        "/EMOTECUTE": "emote-cute",
        "/ENERGYBALL": "emote-energyball",
        "/ENTHUSED": "idle-enthusiastic",
        "/FASHIONISTA": "emote-fashionista",
        "/FLEX": "emoji-flex",
        "/FLIRTYWAVE": "emote-lust",
        "/FLOAT": "emote-float",
        "/FROG": "emote-frog",
        "/GRAVEDANCE": "dance-weird",
        "/GRAVITY": "emote-gravity",
        "/GREEDY": "emote-greedy",
        "/HELLO": "emote-hello",
        "/HOT": "emote-hot",
        "/ICECREAM": "dance-icecream",
        "/KISS": "emote-kiss",
        "/KPOP": "dance-blackpink",
        "/LAMBI": "emote-superpose",
        "/LAUGH": "emote-laughing",
        "/LETSGO": "dance-shoppingcart",
        "/MANIAC": "emote-maniac",
        "/MODEL": "emote-model",
        "/NO": "emote-no",
        "/OGDANCE": "dance-macarena",
        "/PENNYDANCE": "dance-pennywise",
        "/POSE1": "emote-pose1",
        "/POSE2": "emote-pose3",
        "/POSE3": "emote-pose5",
        "/POSE4": "emote-pose7",
        "/POSE5": "emote-pose8",
        "/PUNKGUITAR": "emote-punkguitar",
        "/RAISETHEROOF": "emoji-celebrate",
        "/RUSSIAN": "dance-russian",
        "/SAD": "emote-sad",
        "/SAVAGE": "dance-tiktok8",
        "/SHUFFLE": "dance-tiktok10",
        "/SHY": "emote-shy",
        "/SINGALONG": "idle_singing",
        "/SIT": "idle-loop-sitfloor",
        "/SNOWANGEL": "emote-snowangel",
        "/SNOWBALL": "emote-snowball",
        "/SWORDFIGHT": "emote-swordfight",
        "/TELEKINESIS": "emote-telekinesis",
        "/TELEPORT": "emote-teleporting",
        "/THUMBSUP": "emoji-thumbsup",
        "/TIRED": "emote-tired",
        "/TUMMYACHE": "emoji-gagging",
        "/VIRAL": "dance-tiktok9",
        "/WAVE": "emote-wave",
        "/WEIRD": "dance-weird",
        "/WORM": "emote-snake",
        "/WRONG": "dance-wrong",
        "/YES": "emote-yes",
        "/ZOMBIERUN": "emote-zombierun",
        "/Angry": "emoji-angry",
        "/Bow": "emote-bow",
        "/Casual": "idle-dance-casual",
        "/Charging": "emote-charging",
        "/Confusion": "emote-confused",
        "/Cursing": "emoji-cursing",
        "/Curtsy": "emote-curtsy",
        "/Cutey": "emote-cutey",
        "/Dont": "dance-tiktok2",
        "/Emotecute": "emote-cute",
        "/Energyball": "emote-energyball",
        "/Enthused": "idle-enthusiastic",
        "/Fashionista": "emote-fashionista",
        "/Flex": "emoji-flex",
        "/Flirtywave": "emote-lust",
        "/Float": "emote-float",
        "/Frog": "emote-frog",
        "/Gravedance": "dance-weird",
        "/Gravity": "emote-gravity",
        "/Greedy": "emote-greedy",
        "/Hello": "emote-hello",
        "/Hot": "emote-hot",
        "/Icecream": "dance-icecream",
        "/Kiss": "emote-kiss",
        "/Kpop": "dance-blackpink",
        "/Lambi": "emote-superpose",
        "/Laugh": "emote-laughing",
        "/Letsgo": "dance-shoppingcart",
        "/Maniac": "emote-maniac",
        "/Model": "emote-model",
        "/No": "emote-no",
        "/Ogdance": "dance-macarena",
        "/Pennydance": "dance-pennywise",
        "/Pose1": "emote-pose1",
        "/Pose2": "emote-pose3",
        "/Pose3": "emote-pose5",
        "/Pose4": "emote-pose7",
        "/Pose5": "emote-pose8",
        "/Punkguitar": "emote-punkguitar",
        "/Raisetheroof": "emoji-celebrate",
        "/Russian": "dance-russian",
        "/Sad": "emote-sad",
        "/Savage": "dance-tiktok8",
        "/Shuffle": "dance-tiktok10",
        "/Shy": "emote-shy",
        "/Singalong": "idle_singing",
        "/Sit": "idle-loop-sitfloor",
        "/Snowangel": "emote-snowangel",
        "/Snowball": "emote-snowball",
        "/Swordfight": "emote-swordfight",
        "/Telekinesis": "emote-telekinesis",
        "/Teleport": "emote-teleporting",
        "/Thumbsup": "emoji-thumbsup",
        "/Tired": "emote-tired",
        "/Tummyache": "emoji-gagging",
        "/Viral": "dance-tiktok9",
        "/Wave": "emote-wave",
        "/Weird": "dance-weird",
        "/Worm": "emote-snake",
        "/Wrong": "dance-wrong",
        "/Yes": "emote-yes",
        "/Zombierun": "emote-zombierun",
        "/sayso": "idle-dance-tiktok4",
        "/Sayso": "idle-dance-tiktok4",
        "/SAYSO": "idle-dance-tiktok4",
        "/uwu": "idle-uwu",
        "/UWU": "idle-uwu",
        "/Uwu": "idle-uwu",
        "/zerogravity": "emote-astronaut",
        "/Zerogravity": "emote-astronaut",
        "/zero gravity": "emote-astronaut",
        "/Zero gravity": "emote-astronaut",
        "/boxer": "emote-boxer",
        "/ditzy": "emote-pose9",
        "/Boxer": "emote-boxer",
        "/Ditzy": "emote-pose9",
        "/surprise": "emote-pose6",
        "/celebration": "emote-celebrationstep",
        "/Surprise": "emote-pose6",
        "/Celebration": "emote-celebrationstep",
        "/airguitar": "idle-guitar",
        "/Airguitar": "idle-guitar",
        "/Saunter sway": "dance-anime",
        "/saunter sway": "dance-anime",
        "/Penguin": "dance-pinguin",
        "/penguin": "dance-pinguin",
        "/Creepy puppet": "dance-creepypuppet",
        "/creepy puppet": "dance-creepypuppet",
        "/Watch your back": "emote-creepycute",
        "/watch your back": "emote-creepycute",
        "/Creepy puppet": "dance-creepypuppet",
        "/creepy puppet": "dance-creepypuppet",
        "/Revelations": "emote-headblowup",
        "/revelations": "emote-headblowup",
        "/Stargazing": "emote-stargazer",
        "/stargazing": "emote-stargazer",
        "/Star gazing": "emote-stargazer",
        "/star gazing": "emote-stargazer",
        "/Star": "emote-stargazer",
        "/star": "emote-stargazer",
        "/Bashful": "emote-shy2",
        "/bashful": "emote-shy2",
        "/Party time": "emote-celebrate",
        "/party time": "emote-celebrate",
    }

    # تحقق من البداية وقم بإرسال الرقصة المناسبة لجميع المستخدمين في الغرفة
    for key, emote in emote_mapping.items():
      if message.startswith(key) and user.username in ["BeIgium", "Shyxbaby"]:
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          if isinstance(roomUser, User):
            await self.highrise.send_emote(emote, roomUser.id)
          else:
            print("Ignoring non-User object in roomUsers")
        break  # لا حاجة للاستمرار بعد العثور على النطاق المناس

    if message.lower().lstrip().startswith(("!invite", "/invite")):
      parts = message[1:].split()
      args = parts[1:]
      _bid = "64ffc862364339795ed97b61"  #Bot user.id here
      id = f"1_on_1:{_bid}:{user.id}"
      idx = f"1_on_1:{user.id}:{_bid}"
      rid = "64c56b3f93191a44cc2aaa53"  #Room ID Here

      if len(args) < 1:
        await self.highrise.send_whisper(
            user.id,
            "\nUsage: !invite <@username> This command will send room invite to targeted username. if they ever interact with our bot in past\n • Example: !invite @IIXOXOIIXOXOII"
        )
        return
      elif args[0][0] != "@":
        await self.highrise.send_whisper(
            user.id, "Invalid user format. Please use '@username'.")
        return

      url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
      response = requests.get(url)
      data = response.json()
      users = data['users']

      for user in users:
        user_id = user['user_id']
        __id = f"1_on_1:{_bid}:{user_id}"
        __idx = f"1_on_1:{user_id}:{_bid}"
        __rid = "64c56b3f93191a44cc2aaa53"  #Room ID Here
        try:
          await self.highrise.send_message(__id, "Join Room", "invite", __rid)
        except:
          await self.highrise.send_message(__idx, "Join Room", "invite", __rid)

    if "Piso 1" in message:
      await self.highrise.teleport(f"{user.id}", Position(7.0, 0.0, 16.0))

    if "Piso 2" in message:
      await self.highrise.teleport(f"{user.id}", Position(11.5, 6.75, 23.5))

    if "Piso 3" in message:
      await self.highrise.teleport(f"{user.id}", Position(12.5, 17.0, 15.5))

    if "Hola" in message or "hola" in message:
      await self.highrise.chat(
          f"\n@{user.username} ¡Hola! ¿Cómo puedo ayudarte hoy?\nAlgún problema Instagram: i.angry_"
      )

    if "¿Cómo estás?" in message or "Cómo estás" in message:
      await self.highrise.chat(
          f"\n@{user.username} ¡Gracias por preguntar! Como programa de computadora, no tengo sentimientos, pero estoy aquí y listo para ayudarte."
      )

    if "Lista" in message or "lista" in message:
      await self.highrise.chat(
        f"\nEmotelista\nLíneas poéticas\nPiropos\nBroma\nAsar\nHecho de la diversión"
    )

    if "Emotelista" in message or "emotes" in message or "Emotes" in message or "emotelista" in message:
      await self.highrise.send_whisper(
          user.id,
          "angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\n"
      )
      await self.highrise.send_whisper(
          user.id,
          "pennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun"
      )
      await self.highrise.send_whisper(
          user.id,
          "\nBoxer\nDitzy\nSurprise\nCelebration\nAirguitar\nPenguin\nWatch your back\nRevelations\nCreppy puppet\nStar gazer\nsaunter sway\nMore emotes Soon..."
      )

    if "Líneas poéticas" in message or "líneas poéticas" in message:
      poeticrizz = random.choice([
          "Si llevaras la maldición de Medusa, miraría en tus ojos para que mi piedra pudiera contemplar tu belleza por toda la eternidad.",
          "Si cada estrella fuera un recuerdo, pasaría una eternidad contándolas todas, solo para revivir los momentos que he compartido contigo.",
          "Cuando sale el sol, no tienes sombra, porque no hay nada que pueda replicar tu belleza.",
          "Cuando no puedo estar contigo, leo tu libro favorito, escucho tu canción favorita, veo tu película favorita, porque en ellos encuentro pequeños fragmentos de ti.",
          "Mis días más oscuros se desplazan con una ligera mirada a tus fascinantes miradas. Tus hermosos ojos oscuros son la última fibra que sostiene mi corazón destrozado.",
          "Si pudiera tejer un tapiz de nuestro amor, sería un caleidoscopio de colores, cada matiz un testimonio de la profundidad de nuestro afecto.",
          "Tu presencia es como un amanecer, un resplandor radiante que ahuyenta la oscuridad y llena mi mundo de luz.",
          "Si pudiera navegar por los mares del tiempo, trazaría un curso al momento en que nos conocimos, al instante en que nuestros corazones se entrelazaron.",
          "Tu amor es el ancla que me mantiene firme, un vínculo inquebrantable que me mantiene enraizado y seguro.",
          "Si pudiera reunir las arenas del desierto, crearía un monumento a tu belleza, un testimonio de tu encanto cautivador.",
          "Tu voz es el canto de una sirena, una melodía hipnotizadora que me atrae a las profundidades de tu amor.",
          "Si tú eres la luna, yo soy la marea, porque fluyo bajo tu comando, siempre ansiando estar contigo, ya que eres mi propósito.",
          "Si tuviera que esperar toda mi vida por tu amor, lo haría. Porque cuando me haya marchitado, estaré contento de haber experimentado el cielo antes de alcanzarlo.",
          "Por cada estrella en el cielo que se apagara, nunca lo sabría, porque siempre brillaste más que ellas.",
          "Si fueras un grano de arena, buscaría en cada playa y desierto en busca de ti y tu belleza, sin importar cuánto tiempo tenga que buscar.",
          "Si fueras el ángel de la muerte, estaría dispuesto a morir un millón de veces solo para ver tu belleza.",
          "Si quedara ciego en el momento en que pusiera mis ojos en ti, no lo lamentaría, porque en ese instante contemplé la perfección.",
          "Tú eres el sol de mi girasol, siempre estaré mirando tu hermosa luz mientras te sigo en medio de la brillante mañana.",
          "Si me desafiara a gritar al mundo cuánto te amo, simplemente te lo susurraría al oído.",
          "Tu amor es el faro que me guía a través de las tormentas más oscuras, un faro que ilumina la costa de mi corazón.",
          "Si tu corazón fuera un lienzo, lo pintaría con los colores de mil atardeceres, cada matiz un testimonio de mi amor por ti.",
          "Como una rosa en plena floración, tu belleza me cautiva, dejándome sin aliento y anhelando tu tierno abrazo.",
          "Si tuviera que esperar toda mi vida por tu amor, lo haría. Cuando me haya marchitado, estaré contento de haber experimentado el cielo antes de alcanzarlo.",
          "Si tuviera una flor por cada vez que pensara en ti, tendría solo una, porque no he dejado de pensar en la perfección que eres.",
          "Si pudiera reorganizar el cosmos, te reemplazaría al sol, porque tu belleza brilla más que cualquier estrella, querida mía.",
          "Las estrellas estaban tan celosas de lo brillante que eras que tuvieron que hacer que el sol se apagara solo para ser vistas, pero siempre las eclipsabas.",
          "Incluso si aprendiera todos los idiomas, no encontraría palabras para describir cuán hermosa eres.",
          "Tu risa es la melodía que danza a través de mi alma, una sinfonía de alegría que llena las cámaras de mi corazón.",
          "Si nuestro amor fuera un río, fluiría sin cesar, labrando un camino a través de las montañas del tiempo, imparable y eterno.",
          "Tus ojos son las ventanas a un mundo de maravillas, un universo de posibilidades infinitas que anhelo explorar.",
          "Si fuera un poeta, escribiría mil sonetos, cada verso sería un tributo al hechizo encantador que has lanzado sobre mí.",
          "Tu toque es como una suave brisa, acariciando mi piel y despertando mis sentidos, un testimonio del poder de tu amor.",
          "En el jardín de mi corazón, eres la flor más exquisita, una flor rara y preciosa que atesoraré para siempre.",
          "Tu amor es la brújula que me guía, un verdadero norte que me lleva a las costas de la felicidad y la satisfacción.",
          "Si pudiera capturar la esencia de tu belleza, la embotellaría y la llevaría como perfume, un recordatorio fragante de tu encantadora presencia.",
          "Tu voz es la canción de cuna más dulce, un bálsamo relajante que calma la tempestad de mi alma y me adormece en un estado de serenidad dichosa.",
          "Si nuestro amor fuera una tapicería, estaría tejida con hilos de oro y plata, una obra maestra de pasión y devoción.",
          "Tu sonrisa es el sol que atraviesa las nubes, un rayo radiante de luz que calienta mi corazón y ilumina mi día.",
          "Si fuera un escultor, cincelaría tu imagen en mármol, un tributo atemporal a la belleza que ha cautivado mi corazón.",
          "Tu amor es la llave que desbloquea el cofre del tesoro de mi corazón, revelando una abundancia de cariño y adoración.",
      ])
      await self.highrise.chat(f": {user.username} - {poeticrizz}")

    if "piropos" in message or "Piropos" in message:
      pickuplines = random.choice([
          "Si la belleza fuera tiempo, tú serías la eternidad.",
          "¿Eres un ángel? Porque has caído del cielo.",
          "Si besarte fuera pecado, caminaría feliz por el infierno.",
          "Tu sonrisa ilumina incluso la noche más oscura.",
          "¿Crees en el amor a primera vista, o debo pasar otra vez?",
          "Eres como un sueño, pero mejor, porque estás aquí en la vida real.",
          "Si la belleza fuera un delito, tendrías cadena perpetua.",
          "Me perdí en tus ojos, ¿puedes darme direcciones hacia tu corazón?",
          "Tienes una chispa que ilumina mi mundo.",
          "¿Puedo tomarte una foto? Quiero demostrar a mis amigos que los ángeles existen.",
          "Eres como un libro fascinante; no puedo dejar de mirar tus páginas.",
          "Si fueras una fruta, serías un melocotón, porque eres simplemente delicioso.",
          "Si fuera un gato, pasaría todas mis vidas a tu lado.",
          "¿Tienes un espejo en los bolsillos? Porque veo mi reflejo en tus ojos.",
          "Me gustaría ser el motivo de tu sonrisa todos los días.",
          "Eres como un diamante: raro, hermoso y valioso.",
          "¿Crees en el amor a primera vista, o debería volver a pasar?",
          "Tus ojos son como estrellas en el cielo nocturno.",
          "¿Eres un ladrón? Porque has robado mi corazón.",
          "¿Puedo seguirte a casa? Mis padres siempre me dijeron que siguiera mis sueños.",
          "Tú eres el sueño que nunca quiero despertar.",
          "Si la belleza fuera tiempo, tú serías la eternidad.",
          "¿Eres el sol? Porque iluminas mi día.",
          "Me perdí en tus ojos; ¿me puedes dar direcciones a tu corazón?",
          "Tienes un lugar en mi mente, ¿puedo tener un lugar en la tuya?",
          "Eres el mejor regalo que la vida me ha dado.",
          "Eres como un postre: dulce, irresistible y siempre quiero más.",
          "Tu sonrisa debe ser un reflejo de tu belleza interior.",
          "¿Tienes un nombre, o puedo llamarte mío?",
          "Tus ojos son dos luceros en un cielo estrellado.",
          "Eres como el sol en un día nublado; iluminas mi vida.",
          "Me haces sentir como si estuviera en un cuento de hadas.",
          "¿Crees en el amor a primera vista o debo pasar por aquí otra vez?",
          "Tienes el poder de hacer que mi día sea increíble con solo una mirada.",
          "Eres la razón por la que la luna brilla tan brillante en la noche.",
          "Tus labios son como un imán; no puedo dejar de mirarlos.",
          "Me gustaría ser un pájaro para posarme en tu hombro todos los días.",
          "Eres como una melodía encantadora que no puedo dejar de escuchar.",
          "¿Tienes un mapa? Me perdí en tus ojos.",
          "Eres como una estrella fugaz; rara y hermosa.",
          "Tú eres el sueño que nunca quiero abandonar.",
          "Cada día contigo es una página de un libro maravilloso.",
          "Eres como el café: irresistible y siempre me mantienes despierto.",
          "¿Eres una rosa? Porque haces que el mundo sea más hermoso.",
          "Si el amor fuera un crimen, estaría en prisión de por vida.",
          "Eres como una obra de arte; no puedo dejar de admirarte.",
          "Me gustaría ser el viento para acariciar tu rostro todos los días.",
          "¿Puedo tomarte una foto? Quiero demostrar que los ángeles existen.",
          "Tus ojos son como dos joyas preciosas.",
          "Eres el faro que guía mi camino en la oscuridad.",
          "Si el amor fuera un océano, tú serías mi marea alta.",
          "Cada día contigo es una aventura que nunca quiero que termine.",
          "Tus labios son como un poema que quiero recitar una y otra vez.",
          "¿Tienes un nombre, o puedo llamarte mío?",
          "Eres como un sueño del que nunca quiero despertar.",
          "Si fueras una estrella, serías la más brillante en el cielo nocturno.",
          "Eres el postre de mi vida: dulce, irresistible y siempre quiero más.",
      ])
      await self.highrise.chat(f": {user.username} - {pickuplines}")

    if "broma" in message or "Broma" in message:
      joke = random.choice([
          "¿Qué le dijo una iguana a su hermana gemela? Somos iguanitas.",
          "¿Qué hace una abeja en el gimnasio? Zumba.",
          "¿Cómo se dice pañuelo en japonés? Saka-moko.",
          "¿Cómo maldice un pollito a otro pollito? ¡Caldito seas!",
          "¿Qué hace una abeja en el baño? Pupú.",
          "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
          "¿Qué le dice un semáforo a otro? No me mires, me estoy cambiando.",
          "¿Qué le dice el número 1 al número 10? Para ser como yo, debes ser sincero.",
          "¿Qué le dijo el 2 al 9? Eres tan grande y redondo, como una rosquilla.",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice libro en japonés? ¡Tomol!",
          "¿Por qué no se puede fiar de los átomos? Porque componen todo.",
          "¿Qué le dice un jardinero a otro jardinero? Nos vemos cuando podamos.",
          "¿Qué hace una abeja en el baño? ¡Pupú!",
          "¿Cómo maldice un pollito a otro pollito? ¡Caldito seas!",
          "¿Qué hace una abeja en el baño? ¡Pipí!",
          "¿Cómo se dice mosquetero en japonés? ¡Mostoletero!",
          "¿Por qué las focas miran siempre hacia arriba? Porque ahí están los focos.",
          "¿Qué le dice el semáforo al coche? No me mires, me estoy cambiando.",
          "¿Qué le dice una iguana a su hermana gemela? ¡Somos iguanitas!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice pañuelo en japonés? ¡Saka-moko!",
          "¿Cómo se dice banana en chino? ¡Banana Cheng!",
          "¿Qué hace una abeja en el baño? ¡Pipí!",
          "¿Por qué no puedes confiar en un reloj? Porque ¡siempre te vuelven loco!",
          "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice libro en japonés? ¡Tomol!",
          "¿Por qué no se puede fiar de los átomos? Porque componen todo.",
          "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
          "¿Qué le dice un semáforo a otro? ¡No me mires, me estoy cambiando!",
          "¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!",
          "¿Qué le dice el número 1 al número 10? ¡Para ser como yo, debes ser sincero!",
          "¿Qué le dijo un semáforo a otro semáforo? ¡No me mires, me estoy cambiando!",
          "¿Qué le dijo el semáforo al coche? ¡No me mires, me estoy cambiando!",
          "¿Cómo se dice pañuelo en japonés? ¡Saka-moko!",
          "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!",
          "¿Por qué los esqueletos no pelean entre ellos? ¡Porque no tienen agallas!",
          "¿Por qué el libro de matemáticas se tiró por la ventana? ¡Porque tenía demasiados problemas!",
          "¿Qué le dijo una iguana a su hermana gemela? ¡Somos iguanitas!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice pañuelo en japonés? ¡Saka-moko!",
          "¿Cómo maldice un pollito a otro pollito? ¡Caldito seas!",
          "¿Qué hace una abeja en el baño? ¡Pupú!",
          "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
          "¿Qué le dice un semáforo a otro semáforo? ¡No me mires, me estoy cambiando!",
          "¿Qué le dijo el número 1 al número 10? ¡Para ser como yo, debes ser sincero!",
          "¿Qué le dijo el 2 al 9? ¡Eres tan grande y redondo, como una rosquilla!",
          "¿Qué hace una abeja en el baño? ¡Pipí!",
          "¿Cómo maldice un pollito a otro pollito? ¡Caldito seas!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice libro en japonés? ¡Tomol!",
          "¿Por qué no se puede fiar de los átomos? ¡Porque componen todo!",
          "¿Qué le dice un jardinero a otro jardinero? ¡Nos vemos cuando podamos!",
          "¿Qué hace una abeja en el baño? ¡Pupú!",
          "¿Cómo maldice un pollito a otro pollito? ¡Caldito seas!",
          "¿Qué hace una abeja en el baño? ¡Pipí!",
          "¿Cómo se dice mosquetero en japonés? ¡Mostoletero!",
          "¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!",
          "¿Qué le dice el semáforo al coche? ¡No me mires, me estoy cambiando!",
          "¿Qué le dice una iguana a su hermana gemela? ¡Somos iguanitas!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice pañuelo en japonés? ¡Saka-moko!",
          "¿Cómo se dice banana en chino? ¡Banana Cheng!",
          "¿Qué hace una abeja en el baño? ¡Pipí!",
          "¿Por qué no puedes confiar en un reloj? ¡Porque siempre te vuelven loco!",
          "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!",
          "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
          "¿Cómo se dice libro en japonés? ¡Tomol!",
      ])
      await self.highrise.chat(f": {user.username} - {joke}")

    if "hecho de la diversión" in message or "Hecho de la diversión" in message:
      funfact = random.choice([
          "Los pulpos tienen tres corazones.",
          "En un solo día, una planta de tomate puede absorber más de 30 galones de agua.",
          "El corazón de una ballena azul puede ser del tamaño de un automóvil pequeño.",
          "Los flamencos rosados no nacen con ese color; son grises al nacer y se vuelven rosados debido a su dieta.",
          "Los pingüinos tienen glándulas especiales para deshacerse del exceso de sal en sus cuerpos.",
          "El ronroneo de un gato puede ayudar a reducir el estrés y la ansiedad en las personas.",
          "El ojo de un avestruz es más grande que su cerebro.",
          "Un grupo de flamencos se llama 'parada'.",
          "El agujero en la parte superior de un bolígrafo se llama 'orificio de ventilación'.",
          "Las jirafas tienen lenguas azules y muy largas que pueden alcanzar hasta 45 centímetros de longitud.",
          "Las abejas son capaces de reconocer rostros humanos.",
          "Las vacas tienen mejores amigos y pueden sentirse estresadas cuando se separan de ellos.",
          "Los elefantes son los únicos mamíferos que no pueden saltar.",
          "El sonido que produce un pato no produce eco y no se sabe por qué.",
          "El corazón de un colibrí late hasta 1,200 veces por minuto.",
          "Un grupo de leones se llama 'manada'.",
          "La miel nunca se echa a perder. Se han encontrado recipientes de miel en tumbas egipcias con más de 3,000 años de antigüedad y aún estaba buena.",
          "Los flamencos obtienen su color rosado de su dieta rica en betacarotenos.",
          "Un pulpo tiene aproximadamente 500 millones de neuronas, más que un perro.",
          "Los pandas gigantes pueden comer hasta 38 kilos de bambú al día.",
          "Las arañas no son insectos; son arácnidos.",
          "El hígado es el único órgano que puede regenerarse por completo en el cuerpo humano.",
          "El pingüino emperador es el ave que puede sumergirse a mayores profundidades, alcanzando hasta 500 metros bajo el agua.",
          "El maní no es realmente un fruto seco, es una legumbre.",
          "El león marino es el único miembro de la familia de las focas que tiene orejas visibles.",
          "Las ballenas jorobadas cantan canciones complejas que pueden durar hasta 30 minutos.",
          "Los flamencos pueden dormir de pie sobre una pata.",
          "Los perros tienen un sentido del olfato 10,000 veces más agudo que el de los humanos.",
          "Los gatos pueden saltar hasta seis veces su longitud corporal en un solo salto.",
          "La piel de un oso polar es negra, y su pelaje es translúcido.",
          "Los delfines son uno de los pocos animales que pueden reconocerse a sí mismos en un espejo.",
          "El camello es conocido como 'el barco del desierto' debido a su capacidad para transportar grandes cargas de agua y alimentos en sus jorobas.",
          "Los colibríes son las únicas aves capaces de volar hacia atrás.",
          "El cerebro humano es más activo mientras dormimos que durante el día.",
          "Un solo rayo de sol viaja de la superficie del Sol a la Tierra en aproximadamente 8 minutos.",
          "El sonido no se propaga en el espacio, por lo que no se puede escuchar ningún ruido en el espacio exterior.",
          "El diente de león es una planta comestible y nutritiva, pero generalmente se considera una maleza.",
          "Las serpientes no tienen párpados, por lo que no pueden parpadear.",
          "Los escorpiones brillan bajo la luz ultravioleta.",
          "El murciélago es el único mamífero capaz de volar.",
          "El calamar gigante es el invertebrado más grande del mundo y puede alcanzar hasta 43 pies de longitud.",
          "La hormiga puede cargar objetos que pesan hasta 50 veces su propio peso.",
          "El león es el único gran felino que vive en grupos sociales conocidos como manadas.",
          "El oído humano es sensible a los sonidos en un rango de frecuencia de 20 a 20,000 hercios.",
          "El corazón de un caracol se encuentra en su cabeza.",
          "Un grupo de lobos se llama 'jauría'.",
          "La leche de hipopótamo es de color rosa.",
          "Las jirafas y los camellos tienen válvulas en sus arterias para evitar que la sangre retroceda cuando bajan la cabeza.",
          "Los cocodrilos no pueden masticar su comida; tragan su presa entera o la desgarran en pedazos más pequeños.",
          "El lémur de cola anillada es conocido por sus ojos grandes y saltarines.",
          "El venado de cola blanca es el mamífero más rápido en tierra, alcanzando velocidades de hasta 72 km/h.",
          "El pingüino es el ave con mejor capacidad de buceo, llegando a sumergirse hasta 500 metros bajo el agua.",
          "El perro es conocido como 'el mejor amigo del hombre' debido a su lealtad y compañía a lo largo de la historia.",
          "El ojo de un avestruz es más grande que su cerebro.",
          "El pingüino emperador es el ave que puede sumergirse a mayores profundidades, alcanzando hasta 500 metros bajo el agua.",
          "El delfín es conocido por su inteligencia y su capacidad para comunicarse a través de sonidos y gestos.",
          "Los murciélagos son los únicos mamíferos capaces de volar de manera activa.",
          "El canto de las ballenas jorobadas es uno de los sonidos más largos producidos por cualquier animal en la Tierra, con canciones que pueden durar hasta 30 minutos.",
      ])
      await self.highrise.chat(f": {user.username} - {funfact}")

    if "Asar" in message or "asar" in message:
      roastme = random.choice([
          "Si fueras más tonto, necesitarías un manual de instrucciones para abrir la boca.",
          "Tienes la inteligencia de una piedra, pero al menos las piedras no hablan.",
          "Eres tan lento que se te escaparía una tortuga coja.",
          "Tu nivel de atención es tan bajo que ni siquiera te diste cuenta de que este roast empezó hace un rato.",
          "No eres estúpido; solo tienes mala suerte pensando.",
          "Si fueras una galleta, serías la que se come el aburrimiento de los demás.",
          "Tienes una personalidad que haría que un emoji de berenjena parezca interesante.",
          "Tu sentido del humor está tan desequilibrado que incluso las balanzas se reirían de ti.",
          "Eres la razón por la que el botón de silencio es una bendición durante las videollamadas.",
          "No eres inútil, al menos sirves de mal ejemplo.",
          "Tienes el carisma de una caja de cartón mojada en un día lluvioso.",
          "Si el mundo fuera un concurso de belleza, serías la ganadora... del premio a la más fea.",
          "Eres tan feo que cuando te miras al espejo, el espejo se rompe.",
          "No eres gordo, solo estás cubriendo tu six-pack con una bolsa de papas.",
          "Tienes una mente tan cerrada que no pasas ni una molécula de aire.",
          "Eres como un PowerPoint en modo de espera: aburrido y nadie sabe por qué sigues aquí.",
          "Tienes más excusas que amigos.",
          "No tienes el síndrome del impostor; simplemente eres un impostor.",
          "Eres como un agujero negro de diversión, todo lo que tocas desaparece.",
          "Ni siquiera tu sombra quiere pasar tiempo contigo.",
          "Eres tan aburrido que hasta los emojis de WhatsApp te dejan en visto.",
          "Si el sarcasmo fuera un idioma, estarías hablando en tu lengua materna.",
          "Tu arrogancia no tiene límites, aunque tu inteligencia sí los tenga.",
          "No eres especial; solo eres una edición limitada de ti mismo.",
          "Incluso un GPS se perdería tratando de encontrar tu personalidad.",
          "Tienes menos encanto que un pez muerto.",
          "Eres tan básico que podrían escribir un libro sobre cómo ser tú, pero a nadie le importaría.",
          "Tus padres te querían hasta que descubrieron que no eras un reembolso de impuestos.",
          "No eres el primer idiota que conozco, pero definitivamente estás en el top 5.",
          "Tienes menos amigos que un emoji de caca.",
          "Eres tan inútil que ni siquiera un antivirus te protegería.",
          "Si la estupidez fuera energía, podrías abastecer una ciudad entera.",
          "Eres como un USB: nadie sabe qué haces, pero todos te necesitan para algo.",
          "No eres nadie hasta que alguien te ignora en las redes sociales.",
          "Eres como una película de terror: nadie quiere verte, pero todos hablan de ti.",
          "Tu nivel de atención es tan bajo que te perdiste el cambio de década.",
          "No tienes la culpa de ser tan inútil; es un regalo natural.",
          "Eres tan patético que hasta tus lágrimas están pensando en renunciar.",
          "Tienes menos gracia que una gallina en patineta.",
          "Si el esfuerzo fuera dinero, estarías en la bancarrota.",
          "Eres como un error de ortografía en un libro de gramática: molesto y nadie quiere admitir que existes.",
          "No tienes una personalidad, solo tienes actitudes.",
          "Tienes una mente tan pequeña que podrías usar un pañuelo de pulga como sombrero.",
          "Si la estupidez brillara, serías un sol de medianoche.",
          "Eres como una señal de tráfico: todos te ignoran hasta que te necesitan.",
          "Tienes la inteligencia de una tostadora, pero al menos la tostadora sabe cuándo detenerse.",
          "Tu presencia es tan molesta que hasta los espejos te evitan.",
          "No eres inmaduro, solo has estado viviendo demasiado tiempo.",
          "Si la paciencia fuera un superpoder, serías un supervillano.",
          "Eres tan raro que incluso Google Maps te diría: 'Gira a la izquierda hacia la irrelevancia'.",
          "Si la ignorancia fuera un deporte, estarías en las Olimpiadas.",
          "No eres feo; solo eres la razón por la que existen las bolsas para la cabeza.",
          "Tienes el carisma de una ameba.",
          "Tu personalidad es tan plana que un panqueque parece tridimensional en comparación.",
          "Eres como una canción de cuna: todos quieren que te detengas.",
          "No tienes fans, solo tienes espectadores compasivos.",
          "Eres como una película de bajo presupuesto: nadie quiere verte, pero algunos lo hacen por lástima.",
          "Si fueras un meme, serías un meme desactualizado.",
          "Tienes menos amigos que un contacto de emergencia de un hámster.",
          "Eres como un lunes por la mañana: todos te odian.",
          "No eres un completo idiota; algunas partes te faltan.",
          "Tu inteligencia es como una luz apagada; nadie la ve.",
          "Si la confianza en uno mismo fuera dinero, serías un mendigo.",
          "Eres tan raro que incluso las maniquíes te miran y piensan: 'No quiero ser eso'.",
          "No eres imposible de olvidar; simplemente no hay nada que valga la pena recordar de ti.",
          "Tienes la creatividad de una roca.",
          "Tu vida es tan emocionante como una alarma de incendio.",
          "Eres como una bicicleta oxidada: anticuado y a nadie le importa darle un paseo.",
          "Tienes menos posibilidades de éxito que una aspiradora sin energía.",
          "Si la estupidez fuera una epidemia, serías la paciente cero.",
          "Eres como una película mala: mala desde el principio y nadie quiere verla.",
      ])
      await self.highrise.chat(f": {user.username} - {roastme}")

    if "Deathyear" in message or "año de muerte" in message:
      death_year = random.randint(2023, 2100)
      await self.highrise.chat(
          f" {user.username} No sé cuando morirías pero tal vez alrededor: {death_year}"
      )

    if "año de boda" in message or "Weddingyear" in message:
      death_year = random.randint(2023, 2040)
      await self.highrise.chat(
          f"{user.username} No sé cuándo será la boda, pero tal vez alrededor: {death_year} Disfrutar🌚"
      )

    if "rica" in message or "rico" in message:
      iq = random.randint(6, 66)
      if iq <= 6:
        await self.highrise.chat(
            f" @{user.username} eres {iq}% ,Hermana/o eres pobre asf ,lol ")
      elif iq >= 66:
        await self.highrise.chat(
            f" @{user.username} eres {iq}% ,Eres más inteligente que la mayoría de los RICOS en esta sala."
        )
      elif iq > 6 and iq < 66:
        await self.highrise.chat(f" ( {user.username} ) eres : {iq}% RICO/A")

    if "Iq" in message or "iq" in message:
      iq = random.randint(0, 100)
      if iq <= 10:
        await self.highrise.chat(
            f" @{user.username} tu coeficiente intelectual es {iq}% ,Hermano/a eres tonto asf ,lol "
        )
      elif iq >= 90:
        await self.highrise.chat(
            f" @{user.username} tu coeficiente intelectual es {iq}% ,Eres más inteligente que la mayoría de las otras perras tontas en esta sala."
        )
      elif iq > 10 and iq < 90:
        await self.highrise.chat(f"Your ( {user.username} ) iq is : {iq}%")

    if "Lovepercentage" in message or "porcentaje de amor" in message:
      love_percentage = random.randint(0, 100)
      if love_percentage == 100:
        await self.highrise.chat(
            f" {user.username} {love_percentage}% Todas te aman")
      elif love_percentage == 0:
        await self.highrise.chat(
            f" {user.username} {love_percentage}% Nadie te ama, ve a llorar a ese rincón. "
        )
      elif love_percentage < 100 or love_percentage > 0:
        await self.highrise.chat(
            f" {user.username} Only {love_percentage}% la gente te ama!!")

    if "Hatepercentage" in message or "porcentaje de odio" in message:
      hate_percentage = random.randint(0, 100)
      if hate_percentage == 0:
        await self.highrise.chat(
            f" {user.username} {hate_percentage}% nadie te odia")
      elif hate_percentage == 100:
        await self.highrise.chat(
            f" {user.username} {hate_percentage}% Todas/Todos te odian, ve a llorar en ese rincón "
        )
      elif hate_percentage < 100 or hate_percentage > 0:
        await self.highrise.chat(
            f" {user.username} Solo {hate_percentage}% la gente te odia")

  async def stop_continuous_emote(self, user_id: int):
    if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
        user_id].cancelled():
      task = self.continuous_emote_tasks[user_id]
      task.cancel()
      with contextlib.suppress(asyncio.CancelledError):
        await task
      del self.continuous_emote_tasks[user_id]

  async def send_continuous_emote(self, emote_id: str, user_id: int,
                                  delay: float):
    try:
      while True:
        await self.highrise.send_emote(emote_id, user_id)
        await asyncio.sleep(delay)
    except ConnectionResetError:
      print(
          f"Failed to send continuous emote to user {user_id}. Connection was reset."
      )
    except asyncio.CancelledError:
      print(f"Continuous emote task for user {user_id} was cancelled.")
    except ResponseError as error:
      if str(error) == "Target user not in room":
        print(f"User {user_id} is not in the room.")
      else:
        raise  # Re-raise the exception if it's not the one we're handling.

  async def send_random_reactions(self,
                                  user_id: str,
                                  num_reactions: int = 1,
                                  delay: float = 1.1) -> None:
    reactions = ["heart", "wink", "wave", "thumbs", "clap"]
    for _ in range(num_reactions):
      reaction = random.choice(reactions)
      await self.highrise.react(reaction, user_id)
      await asyncio.sleep(delay)  # Add a delay between reactions

  async def on_user_move(self, user: User, pos: Position) -> None:
    """On a user moving in the room."""
    if user.username == "BeIgium":
      print(user.username, pos)

  async def send_invite_to_all_conversations(self, roomId: str) -> None:
    last_id = ''
    conversation_ids = []
    response = await self.highrise.get_conversations()
    conversations = response.conversations

  # loop through the conversations and send a room invite in each conversation
    while len(conversations) > 0:
      print(len(conversations))

      for conversation in conversations:
        conversation_ids.append(conversation.id)
        last_id = conversation.id
        print(f"{last_id}")

    # get next set of conversations
      response = await self.highrise.get_conversations(False, last_id)
      conversations = response.conversations

    for conversation_id in conversation_ids:
      # await self.highrise.send_message(
      # conversation_id,
      # "¡Hola amigo! 🌸¿Cómo estás? 😊 ¿Cómo va tu día? Si estás buscando hacer conexiones, únete a la sala para disfrutar de buenas vibraciones, lindas conversaciones y la oportunidad de encontrar una novia, un novio o amigos increíbles. 🌟")
      await self.highrise.send_message(conversation_id, "Join my room!", "invite", roomId)
      # await self.highrise.send_message(conversation_id, "Ú𝙣𝙖𝙨𝙚 𝙖𝙡 𝙨𝙤𝙧𝙩𝙚𝙤 𝙮 𝙜𝙖𝙣𝙚 𝙀𝙥𝙞𝙘 𝘾𝙤𝙣𝙨𝙪𝙡𝙩𝙚 @JustSneak 𝙋𝙪𝙗𝙡𝙞𝙘𝙖𝙘𝙞ó𝙣 𝙥𝙖𝙧𝙖 𝙤𝙗𝙩𝙚𝙣𝙚𝙧 𝙢á𝙨 𝙙𝙚𝙩𝙖𝙡𝙡𝙚𝙨❤️🎄")

  async def is_new_user(self, user: User) -> bool:
    try:
      data = db[user.id]
      print(f"{user.username} is in the database:: {data}")
      if data['tipped']:
        return False
      else:
        return True
    except:
      return True

  async def tip_new_user(self, user: User, amount: int) -> None:
    if await self.is_new_user(user):
      #check if the bot has the amount
      bot_wallet = await self.highrise.get_wallet()
      bot_amount = bot_wallet.content[0].amount
      if bot_amount <= amount:
        print(f"Not enough funds")
        return

      #converts the amount to a string of bars and calculates the fee
      """Possible values are: "gold_bar_1",
      "gold_bar_5", "gold_bar_10", "gold_bar_50", 
      "gold_bar_100", "gold_bar_500", 
      "gold_bar_1k", "gold_bar_5000", "gold_bar_10k" """
      bars_dictionary = {
          10000: "gold_bar_10k",
          5000: "gold_bar_5000",
          1000: "gold_bar_1k",
          500: "gold_bar_500",
          100: "gold_bar_100",
          50: "gold_bar_50",
          10: "gold_bar_10",
          5: "gold_bar_5",
          1: "gold_bar_1"
      }
      fees_dictionary = {
          10000: 1000,
          5000: 500,
          1000: 100,
          500: 50,
          100: 10,
          50: 5,
          10: 1,
          5: 1,
          1: 1
      }
      #loop to check the highest bar that can be used and the amount of it needed
      tip = []
      total = 0
      for bar in bars_dictionary:
        if amount >= bar:
          bar_amount = amount // bar
          amount = amount % bar
          for i in range(bar_amount):
            tip.append(bars_dictionary[bar])
            total = bar + fees_dictionary[bar]
      if total > bot_amount:
        print(f"Not enough funds")
        return
      for bar in tip:
        await self.highrise.tip_user(user.id, bar)
        db[user.id] = {'tipped': True}
        print(f"tipping {user.username} {bar}")

    else:
      print(f"{user.username} has already been tipped")


  async def emote_loop(self):
    while True:
        await self.highrise.send_emote(
            random.choice([
              "idle-loop-sitfloor", "emote-tired", "emote-pose7", "emoji-thumbsup",
              "emoji-angry", "dance-macarena", "emote-hello", "dance-weird",
              "emote-superpose", "idle-lookup", "idle-hero", "emote-wings",
              "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes",
              "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull",
              "emote-think", "emote-hot", "dance-shoppingcart", "emote-greedy",
              "emote-frustrated", "emote-float", "emote-baseball", "emote-yes",
              "idle_singing", "idle-floorsleeping", "idle-loop-sitfloor",
              "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no",
              "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model",
              "emote-charging", "emote-snake", "dance-russian", "emote-sad",
              "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging",
              "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow",
              "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
              "idle-dance-tiktok4"
              "emote-maniac", "emote-energyball", "emote-frog", "emote-cute",
              "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8",
              "idle-dance-casual", "emote-pose1", "dance-sexy", "emote-pose3",
              "emote-pose5", "emote-cutey", "emote-Relaxing", "emote-model",
              "emote-fashionista", "emote-gravity", "emote-zombierun",
              "emoji-ceilebrate", "emoji-floss", "emote-Relaxing ", "emote-punkguitar",
              "dance-tiktok9", "dance-weird", "emote-punkguitar", "idle-uwu"
              "emote-swordfight", "emote-handstand", "emote-bow", "emote-cursty",
              "dance-breakdance", "emote-creepycute", "emote-headblowup", "idle-guitar",
                # ... (add your emote choices here)
            ]))
        await asyncio.sleep(4)

  async def rizz_loop(self):
    with open('no.json', 'r') as f:
      rizz = json.load(f)

    while True:
      data = random.choice(rizz)
      quote = data["quote"] + " " + data["emoji"]
      await self.highrise.chat(quote)
      await asyncio.sleep(40)
      
  async def note_loop(self):
    try:
        with open('data.json', 'r') as f:
            file_content = f.read()
            if not file_content.strip():
                print("Warning: 'note.json' is empty or contains only whitespace.")
                return

            notes = json.loads(file_content)

        while True:
            data = random.choice(notes)
            note_text = data["quote"] + " " + data["emoji"]
            await self.highrise.chat(note_text)
            await asyncio.sleep(10)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in 'note.json': {e}")
        # Handle the error as needed, e.g., by providing a default value or terminating the loop.