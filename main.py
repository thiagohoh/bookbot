from typing import Dict

def file_handler() -> str:
    with open('books/frank.txt') as f:
        file_content = f.read()
        return file_content


def word_count(text: str):
    print(f"Text has {len(text.split())} words")


def frequency(text: str) -> Dict[str, int]:
    f = {}
    for c in text.lower():
        if c in f:
            f[c] += 1
        else:
            f[c] = 1
    return f


def sort_on(dic: dict):
    return dic["num"]


def report(dic: dict):
    l = []
    for k, v in f.items():
        if k.isalpha():
            l.append({"name": k, "num": v})

    l.sort(reverse=True, key=sort_on)

    for j in l:
        k, v = j.items() # returns a Tuple
        print(f"The '{k[1]}' character was found {v[1]} times")


if __name__ == '__main__':
    t = file_handler()
    word_count(t)

    f = frequency(t)
    report(f)


