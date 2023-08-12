# AI chatbot for Discord
AI is a chat bot that was created to communicate with users using a text generation algorithm based on Markov chips, random numbers, probabilities, text branching. Thanks to logical operations, the bot can generate text close to real text. The bot can act as a guide or just an interlocutor to maintain interest on the server. The bot has many settings, thanks to which you can get different characters, or behavior patterns.

# Bot interaction
Perhaps the action with the bot occurs by sending a message to the Discord server. The response to the user's messages will return the same channel where the user's message was sent.

## Technology stack
* CuteON - Serializer to save reading data
* Python - Programming language for programming logic
* Discord.py - library for interacting with discord
* pymorphy2 - To get keywords from text
* pyowm - Module for getting the weather in the specified region

> ___Recommendation:___ _make sure you install all modules from the list!_

# Setting up your own bot
To configure the bot, go to the config.sws file and change the Token parameter to your token from the Discord developer portal. After that you can change other parameters

### __Config.sws parameter list__

* __chance_choosing_full_pair__ - the chance of choosing the whole pair and not just one word from the text
* __chance_choosing_main_word__ - chance of choosing the first word from the text
* __chance_teleport__ - chance of jumping the message distance delta plus word index from the iteration
* __chance_use_message__ - chance of using a random word from the user's message
* __chance_use_next_word__ - chance of using the next word after the word chosen from the message if this word is in the text
* __match_percentage__ - the percentage of the match of the word, if the word is less than this coefficient, then the word is not considered necessary
* __chance_add_to_banlist__ - With what chance the word from the answer will be included in the list of not used words
* __Probability_descent_for_use_message__ - step, adding which will decrease the probability of using the message
* __max_size_respons__ - the maximum size of the bot's response to user messages
* __allowed_array_length__ - If the value of the unused array is greater than it will be reset to the standard value of the array

To customize the algorithm, you can change the parameters in the education/parameters.sws file, where you can specify your bot settings

# Admin panel
It's not a big Flask application for configuring bot parameters. Since constantly making changes to files is long and not convenient, but thanks to this simple panel, I can change the generation parameters and bot settings through the local network where the host (or server) and the client device are located

> _Important: both devices must be on the local network, otherwise you will not be able to connect to the host and change the state of the files_

# Interface

When entering the panel, there will be two small islands for setting up the bot. They can be swapped through the configuration file, as well as changing their CSS styles, though only through files.

## Change data

For changing data in files with the extension . sws responds to the first island, you can choose the type of data you want to enter, then fill in the address to the file, the line name, and the data itself that needs to be changed

## Changing text data
To quickly change text data, use the second island to change text files or to create others. In the upper field, enter the name or address before the file, then you can enter the entire contents of the file in the text field
