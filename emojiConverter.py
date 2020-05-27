def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😄", # Mac hot key:  control + command + blank
        ":(" : "😟"
    }
    output = ""
    for word in words:
        output +=emojis.get(word, word) + " "
    return output


mes = input(">")
print(emoji_converter(mes))