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