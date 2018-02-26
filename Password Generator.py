import random
import string


def generate():
    result = [random.choice(string.digits) for i in range(0, 4, 1)]
    result += [random.choice(string.ascii_lowercase) for i in range(0, 6, 1)]
    result.append(random.choice(string.ascii_uppercase))
    result.append(random.choice(string.punctuation))
    random.shuffle(result)
    return ''.join(result)


print(generate())

