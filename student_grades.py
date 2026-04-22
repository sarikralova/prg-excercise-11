class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.get_by_index(index)

        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        vysledek = []
        for i in range(len(self.scores)):
            if self.scores[i] == value:
                vysledek.append(i)
        return vysledek

    def get_sorted(self):
        scores = self.scores.copy()

        for j in range(len(scores)):
            for i in range(0, len(scores) - j - 1):
                if scores[i] > scores[i +1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
        return scores


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.get_sorted())
    print(results.scores)