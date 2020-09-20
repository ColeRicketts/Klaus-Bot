# Klaus
This is a discord bot designed in Python using the [discord.py] library.

The bot contains all basic moderation features, as well as a Wikipedia search function, auto moderator and soon to come voice channel music playback option.

# Commands
Below lists out the commands and their cogs, all starting with the '!' prefix.

### Moderation
Klaus supports a number of basic moderation commands, listed below:

* Kick - !kick <@member> <reason> - Kicks a member from the server, only able to be used with 'Kick_Members' permissions
* Ban - !ban <@member> <reason> - Ban a member from the server, only able to be used with 'Ban_Members' permissions
* Unban - !unban <@member> - Unbans a member from the banlist, only able to be used with 'Ban_Members' permissions
* Slowmode - !slowmode <amount> - Sets the channel into slowmode for the specified timings
* Clear - !clear <amount> - Clears a number of messages specified in the channel, as well as the clear command
* Warn - !warn <@member> - Adds a warning to a user, added to a database for cold storage
* Warnings - !warnings <@member> - Queries number warnings for a specified user
* Clearwarnings - !clearwarnings <@member> - Sets a specified user's warnings to 0
* Report - !report <@member> <reason> - Reports a user and flags them to the moderation team

### Voice
!!!Work In Progess!!!
Coming Soon, I will work to integrate voice functionality into the bot like playing music.

### Installation
Once the bot is done, I'll post an installation guide here!

   [discord.py]: <https://github.com/Rapptz/discord.py>