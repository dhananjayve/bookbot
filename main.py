# print("hello world")
def get_word_count(content):
    s = content.split(" ")
    print(f"word count is {len(s)}")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

with open("books/frankenstein.txt", 'r') as f:
    file_contents = f.read()
    #print(file_contents)
    get_word_count(file_contents)
    dictdata =  get_chars_dict(file_contents)
    print(dictdata)
    listdata = list(dictdata.keys())
    print('list data')
    print(listdata)
    print('sorted list')
    listdata.sort(reverse=False)
    print(listdata)
    for item in listdata:
        if not item.isalpha():
            continue
        print(f"The '{item}' character was found {dictdata[item]} times")

