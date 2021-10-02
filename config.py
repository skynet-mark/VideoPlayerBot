"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "4476771"))
API_HASH = getenv("API_HASH", "f2498956859c009919a2e54204115e3b")
BOT_TOKEN = getenv("BOT_TOKEN", "2016907331:AAEtawJyxN8WlR3aK9P4wQjGn5zaMW9GiDs")
SESSION_STRING = getenv("SESSION_STRING", "BABJOHMEngVCcXjRh91PwTgxpQvjbxKi5ARJTmw3efIKSWzM7Xajsm9ZeTvxi4-eHltIx8sIU4gH9iVuaSiSzsqWC-pyHRf0KYp9GOGjUSXbWa_BNwohygDAWGg2XjsyOqywxXos_TNrQ2Qs2Vc9PN6losERL8tY_PrsuJdyPML1GCbJDIi_RNYh6IgQj1HGzW6uKavv2dmTnXw5102vxOsWTsAgfPuVbP6bL0dwUlG8rxqT_tRHPgkzKU0hfFKGDKtBtH2NMcwaH6SIeBhoKlv81_ghQOaIak4IGwyRBKwqCHDpTrLFZi-4-yq0AownZxZAtDXcfOyTQdCOI4m3VueAcJjnCAA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SafoTheBot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
