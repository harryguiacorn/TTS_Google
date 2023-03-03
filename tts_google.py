import gtts
# from playsound import playsound

with open('Chapter 1 - LIVERMORE SPEAKS.txt') as f:
  lines = f.read()
  # print(lines)

  # Create a gTTS object and set the language to English (en) and gender to female (f)
  tts = gtts.gTTS(text=lines, lang='en', tld='co.uk', slow=False)

  # save the audio file
  tts.save("Chapter 1 - LIVERMORE SPEAKS.mp3")
  # play the audio file
  # playsound("hello.mp3")

  # all available languages along with their IETF tag
  # print(gtts.lang.tts_langs())
