from collections import defaultdict


def main():
    print("Let's generate letter frequency chart from a sentence:\n")

    sentence = input("Input your sentence: ")
    separator = " "

    print("\nChart:")

    char_freqs = count_char_freqs(sentence)

    chart = build_chart(char_freqs, separator)

    print(chart)


def count_char_freqs(sentence: str) -> dict[str, list[str]]:
    char_freq: dict[str, list[str]] = defaultdict(list[str])

    for char in sentence:
        if not is_letter(char):
            continue

        lower_case_char = char.lower()

        char_freq[lower_case_char].append(lower_case_char)

    return char_freq


def is_letter(letter: str):
    is_upper_case = 65 <= ord(letter) and ord(letter) <= 90
    is_lower_case = 97 <= ord(letter) and ord(letter) <= 122

    return is_upper_case or is_lower_case


def build_chart(char_freqs: dict[str, list[str]], separator: str) -> str:
    keys = char_freqs.keys()
    vals = char_freqs.values()

    highest_freq = max([len(val) for val in vals])

    spaces = [" " for _ in range(len(str(highest_freq) + " "))]
    chart = f"{''.join(spaces) + ' '}🭯"

    for i in range(highest_freq - 1, -1, -1):
        chart += "\n"
        number_length = len(str(i + 1))
        adjusted_spaces = spaces[:]
        for _ in range(number_length):
            adjusted_spaces.pop()

        chart += f" {i + 1}{''.join(adjusted_spaces)}│"

        for key in keys:
            char_freq = char_freqs.get(key)

            if not char_freq:
                continue

            char = " "

            if len(char_freq) - 1 >= i:
                char = char_freq[i]

            chart += f"{separator} {char} {separator}"

    chart += "\n"
    for i in range(len(spaces) + 1):
        chart += "─"
    chart += "┼"

    for key in keys:
        chart += "─────"
    chart += "🭬"

    chart += "\n"
    for i in range(len(spaces) + 1):
        chart += " "
    chart += "│"

    for key in keys:
        chart += f"{separator}[{key}]{separator}"

    return chart


if __name__ == "__main__":
    main()
