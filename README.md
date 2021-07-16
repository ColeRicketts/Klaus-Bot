# Klaus - Multipurpose Bot
This is a Discord bot designed in Python using the [discord.py] library. It is intended for use in smaller servers and to be selfhosted by the owners/admins, if you are looking for alternatives to lots of the features locked behind 'Premium' on other bots.

The bot contains all basic moderation features, announcements, automoderator, levelling, polling, automessages and a music feature (WIP)

# Commands
Below lists out the commands and their cogs, all starting with the '!' prefix. All of these can be found with the '!help' command

### Moderation
The bot supports a number of basic moderation commands, listed below:

* Kick - !kick <@member> <reason> - Kicks a member from the server, only able to be used with 'Kick_Members' permissions
* Ban - !ban <@member> <reason> - Ban a member from the server, only able to be used with 'Ban_Members' permissions
* Unban - !unban <@member> - Unbans a member from the banlist, only able to be used with 'Ban_Members' permissions
* Slowmode - !slowmode <amount> - Sets the channel into slowmode for the specified timings
* Clear - !clear <amount> - Clears a number of messages specified in the channel, as well as the clear command
* Warn - !warn <@member> - Adds a warning to a user, added to a database for cold storage
* Warnings - !warnings <@member> - Queries number warnings for a specified user
* Clearwarnings - !clearwarnings <@member> - Sets a specified user's warnings to 0
* Report - !report <@member> <reason> - Reports a user and flags them to the moderation team

### Announcements
The bot has the ability to create server announcements, using these commands:

* Announcetitle - !announcetitle <title> - Sets the title of the announcement to be broadcasted
* Announcemessage - !announcemessage <message> - Sets the message of the announcement to be broadcasted
* Previewannounce - !previewannounce - Sends the announcement in the channel you are in, to check it is formatted properly
* Announce - !announce - Announces the message as an embed in the announcements channel of the server
* Serverannounce - !serverannounce - Announces the message in every channel across the server as an embed

### Automod
The bot can filter words sent in the chat as specified by the moderators:

* Banword - !banword <word> - Adds a word to the banlist which filters it in the chat
* Unbanword - !unbanword <word> - Removes a word from the banlist which unfilters it in chat
* Bannedwords - !bannedwords - Outputs a list of all banned words on the server

### Levelling
For every message sent, a random quantity of XP is assigned to create a level based system:

* Leaderboard - !leaderboard - Displays the top 3 people in the server based on most message experience
* Level - !level - Displays stats about your level, including experience and number of messages

### Poll
The bot can generate reaction based polls in the server with these commands:

* Rating - !rating <topic> - Creates a rating poll for users to answer on a scale of 1-10
* True or False - !truefalse <topic> - Creates a true or false poll which users answer either way
* Poll - !poll <title;option1;option2 etc> - Creates a poll with a max of 25 possible answers as specified
* Endpoll - !endpoll <identifier> - Ends the poll with the ID and outputs the most picked answers

### Music
WORK IN PROGRESS:

* Join - !join - Bot joins the voice channel as long as a user is connected there
* Leave - !leave - Bot leaves a voice channel
* Play - !play <search_terms> - Bot searches YouTube and plays a song

# Installation
### Prerequisites
1) Look in **requirements.txt** for the required packages and links to them on GitHub. Install these via command line.
2) Have a bot made in the Discord developer portal, with an OAUTH link to your server with admin permissions. Guides for this can be found online.
3) Developer mode enabled on Discord to gather ID's of channels

### Using the bot
1) Next, download the latest release source code and edit the values in **config.json** for your particular guild.
2) Run **discordbot.py** to start the bot and it should connect to the server, no other Python config needed.
3) Enjoy the use of the bot and feel free to raise any issues in GitHub.

# Credits

Special thanks to Aethese, Spaxly, Wurgo and Neil Shah for their contributions!
