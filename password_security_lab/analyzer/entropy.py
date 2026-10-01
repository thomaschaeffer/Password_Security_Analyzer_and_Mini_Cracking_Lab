import math

def estimate_entropy(password,alphabet_size):
    return len(password)*math.log2(alphabet_size)


if __name__ == "__main__":
    print(estimate_entropy("sdjfjsffqsdfsdg!!?sDJSJFGHOFS.5565lfdsf!5",42))