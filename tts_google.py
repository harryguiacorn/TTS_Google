import gtts


def main(__importTextPath="", __exportAudioPath=""):
  print("here: ", __importTextPath)
  print("here: ", __exportAudioPath)
  with open(__importTextPath) as f:
    lines = f.read()
    # print(lines)

    # Create a gTTS object and set the language to English (en) and gender to female (f)
    # tts = gtts.gTTS(text=lines, lang='en', tld='co.uk', slow=False)

    # save the audio file
    # tts.save(__exportAudioPath)


if __name__ == "__main__":
  main()
