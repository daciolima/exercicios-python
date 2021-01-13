def phoneword(phonenumber):
    """
    Retorna todas as possibilidades de phonewords dos seus respectivos phonenunbers

    :param phonenumber: str
    :return: Lista de strings com todos os phonewords

    0(3**n) <= ? <=0(4**n) => 0(a**n)  # Complexidade do algorítmo é exponencial

    """
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    n = len(phonenumber)

    def phoneword_rec(previews_results, cursor):
        if cursor == n:
            return previews_results
        digit = phonenumber[cursor]
        results = []

        for char in digit_to_chars[digit]:
            results.extend(
                prev_result + char for prev_result in previews_results)
        return phoneword_rec(results, cursor + 1)
    return phoneword_rec([''], 0)


print(phoneword(''))  # ['']
print(phoneword('7'))
print(phoneword('73'))
print(phoneword('736'))  # ['REN', 'SEN']



