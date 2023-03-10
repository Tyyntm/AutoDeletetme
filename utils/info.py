#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os
from vars import api_id, api_hash, bot_token, session, time, chats, white_list, black_list, database_uri



API_ID       = int(os.environ.get("API_ID", api_id))
API_HASH     = os.environ.get("API_HASH", api_hash)
BOT_TOKEN    = os.environ.get("BOT_TOKEN", bot_token)
SESSION      = os.environ.get("SESSION", session)
TIME         = int(os.environ.get("TIME", time))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", chats).split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", white_list).split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", black_list).split()]
DATABASE_URI = os.environ.get("DATABASE_URI", database_uri)
PORT         = os.environ.get("PORT", "8080")
