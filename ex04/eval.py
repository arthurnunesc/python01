from typing import List

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: List[float or int], words: List[str]):
        if len(words) != len(coefs):
            print(-1)
            return 1
        sum = 0
        for word, coef in zip(words, coefs):
            sum += len(word) * coef
        print(sum)
        return sum

    @staticmethod
    def enumerate_evaluate(coefs: List[float or int], words: List[str]):
        if len(words) != len(coefs):
            print(-1)
            return 1
        sum = 0
        for index, word in enumerate(words):
            sum += len(word) * coefs[index]
        print(sum)
        return sum


def main():
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    Evaluator.zip_evaluate(coefs, words)
    Evaluator.enumerate_evaluate(coefs, words)
    
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    Evaluator.zip_evaluate(coefs, words)
    Evaluator.enumerate_evaluate(coefs, words)

if __name__ == "__main__":
    main()
