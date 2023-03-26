import pandas

df = pandas.read_csv("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day26_NATO-alphabet-start/nato_phonetic_alphabet.csv")

word_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(type(word_dict))
print(word_dict)

def a():
    try:
        word = input("Enter a word: ").upper()
        alphabet_list = [word_dict[w] for w in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        a()
    else:
        print(alphabet_list)
a()
# for w in word:
    # alphabet_list.append(word_dict[w])

