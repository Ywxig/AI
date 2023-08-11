# The education directory
This directory is needed to store text data as a generation resource. Changing the contents of the directory will change the final result of the generation.

If you need to change the characteristics of the response, then you can change the contents of the files

You can enter a variety of text in the files, here is an example from the site https://metanit.com/cpp/tutorial/1.1.php for an example of the file structure

* ___text.txt___ - File with basic text resources. This is the text from which the response to the message will be obtained.
  >You can enter any text. But if you told the algorithm to collect only sentences with keywords, then use the
  >
  >`#KEYWORDS setting <Words are merged separated by commas>`
  ```
  #KEYWORDS Язык,программирования
  Язык программирования С++ представляет высокоуровневый компилируемый язык программирования
  общего назначения со статическойтипизацией, который подходит для создания самых различных
  приложений. На сегодняшний день С++ является одним из самых популярных и распространенных языков.
  Своими корнями он уходит в язык Си, который был разработан в 1969—1973 годах в компании Bell Labs
  программистом Деннисом Ритчи (Dennis Ritchie). В начале 1980-х годов датский программист Бьерн
  Страуструп (Bjarne Stroustrup), который в то время работал в компании Bell Labs, разработал С++ как расширение к
  языку Си. Фактически вначале C++ просто дополнял язык Си некоторыми возможностями
  объектно-ориентированного программирования. И поэтому сам Страуструп вначале называл
  его как "C with classes" ("Си с классами").
  ```
  
* ___hyibrid.txt___ - a file with prepared responses to user messages. Needed to speed up the generation
  ```
  привет:Hello worlp,||Привет||здарасте
  пока:пока,
  досвидание:досвидание,
  спасибо:пожалуйста,
  ```

* ___parameters.sws___ - file with generator parameters. Changing them will lead to a change in the behavior of the bot
  ```
  bool::show_dict_PARAMETERS::False
  //
  //
  float::chance_choosing_full_pair::0.59
  float::chance_choosing_main_word::0.4
  float::chance_teleport::0.1
  float::chance_use_message::0.45

  float::chance_use_next_word::0.42
  float::match_percentage::0.78
  float::chance_add_to_banlist::0.7
  float::Probability_descent_for_use_message::0.06
  int::max_size_respons::5
  int::allowed_array_length::6
  int::min_word_in_pair::2
  int::max_word_in_pair::5
  //
  print::End of PARAMETERS.SWS
  ```
