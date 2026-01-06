"""Assignment
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from each message at that particular index."""

def filter_messages(messages):
    filtered_message = []
    count = []
    for message in messages:
        words = message.split()
        dangs = []
        good_words = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
                
        sentence = " ".join(good_words)
        filtered_message.append(sentence)
        
        count_dang = len(dangs)
        count.append(count_dang)
        
    return filtered_message, count