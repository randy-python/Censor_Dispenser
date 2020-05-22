email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["Helena", "she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#Answer for Question 2. This function will censor any word or phrase from a string taking into account capitalizations, puntuations and word length.
def word_censor(word, string):
    word_lst = []
    if word.isalpha():
        word_lst.append(word)
    else:
        word_lst += word.split()
    sliced_string = string
    count = 0
    for wrd in word_lst:
        count += 1
    number = -count
    censored_phrase = ""
    while number != 0:
        censored_phrase += " " + len(word_lst[number])*"X"
        number += 1
    censored_phrase = censored_phrase[1:len(censored_phrase)]
    for i in range(len(string)):
            if sliced_string[i:i+len(word)].lower() == word.lower():
                if i == 0 or sliced_string[i-1] == " " or sliced_string[i-1] == "\n":
                    if len(sliced_string[i:i+len(word)]) == (len(word)+1) or not sliced_string[i+len(word)].isalpha() or sliced_string[i+len(word)] == "s" and not sliced_string[i+len(word)+1].isalpha():
                        sliced_string = sliced_string[:i] + censored_phrase + sliced_string[i+len(censored_phrase):]
    return sliced_string

print(word_censor("learning algorithms", email_one))

#Answer for Question 3. This function runs a list of words or phrases through the word_censor function.
def word_lst_censor(word_lst, string):
    new_string = string
    for word in word_lst:
        if word.lower() in new_string.lower():
            new_string = word_censor(word, new_string)
    return new_string

#print(word_lst_censor(proprietary_terms, email_two))

#Answer for Question 4.  This function censors all words/phrases from the prop_words_lst argument as well as all words/phrases from the neg_words_lst argument after their second occurance.
def neg_prop_word_censor(neg_word_lst, prop_word_lst, string):
    string = word_lst_censor(prop_word_lst, string)
    first_bad_word = len(string)
    second_bad_word = len(string)
    third_bad_word = len(string)
    for i in range(len(string)):
        for word in neg_word_lst:
            index = string.lower().find(word.lower(), i, i+len(word))
            if index == -1:
                continue
            elif index < first_bad_word:
                first_bad_word = index
            elif index < second_bad_word:
                second_bad_word = index
            elif index < third_bad_word:
                third_bad_word = index
    return string[:third_bad_word] + word_lst_censor(neg_word_lst, string[third_bad_word:])

#print(neg_prop_word_censor(negative_words, proprietary_terms, email_three))

#Answer for Question 5:
def one_before_through_one_after(neg_words, prop_words, string):
    censored_words_lst = neg_words + prop_words
    new_string = string
    for word in censored_words_lst:
        start_index = 0
        end_index = len(word)
        if word.lower() in string.lower():
            for i in range(len(new_string)):
                count = 0
                if string[i:i+len(word)].lower() == word.lower():
                    if i == 0 or new_string[i-1] == " " or new_string[i-1] == "\n":
                        if len(string[i:i+len(word)]) == (len(word)) or not string[i+len(word)].isalpha():
                            start_index = i
                            end_index = i + len(word) - 1
                            if string[i+len(word)] == "'":
                                end_index = i + len(word) + 1
                else:
                    continue
                word_before_start = start_index
                word_before_end = start_index
                word_after_end = end_index
                word_after_start = end_index
                if start_index !=0:
                    a = 1
                    b = 1
                    while not new_string[start_index - a].isalpha():
                        a += 1
                        if new_string[start_index - a] != "X":
                            word_before_end = start_index - (a-1)
                            while new_string[word_before_end - b].isalpha():
                                b += 1
                            word_before_start = word_before_end - (b-1)
                if end_index + 1 != len(new_string) or end_index + 2 != len(new_string):
                    a = 1
                    b = 0
                    while not string[end_index + a].isalpha():
                        a += 1
                    word_after_start = end_index + a
                    while string[word_after_start + b].isalpha() or string[word_after_start + b] == "'":
                        b += 1
                    word_after_end = word_after_start + b
                    new_string = new_string[:word_before_start] + (word_before_end - word_before_start)*"X" + new_string[word_before_end:start_index] + ((end_index+1) - start_index)*"X" + new_string[(end_index+1):word_after_start] + (word_after_end - word_after_start)*"X" + new_string[word_after_end:]
    return new_string

#print(one_before_through_one_after(negative_words, proprietary_terms, email_four))


    
    



                
