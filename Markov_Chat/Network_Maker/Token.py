import random


class Token:
    global word
    global nextList

    def __init__(self, word, nextWord):
        self.word = word
        self.nextList = dict()
        self.update_next(nextWord)

    def update_next(self, nextWord):
        if nextWord in self.nextList:
            self.nextList[nextWord] += 1
            # print('Updated ' + nextWord + ', now has ' + str(self.nextList[nextWord]))
        else:
            self.nextList[nextWord] = 1

    def get_next_list(self):
        return self.nextList

    def pick_word(self):
        total = self.get_total_following()
        rand = random.randint(0,total)
        counter = 0
        for item in self.nextList:
            counter += self.nextList.get(item)
            # print("trying...")
            if counter >= rand:
                # print("Found. Counter " + str(counter) + " is >= " + str(rand))
                return item

    # NOTE: This replaces the counts in nextList with probabilities, doesn't make a copy
    # NOT USED RIGHT NOW
    def return_probability_dict(self):
        total = 0
        for key in self.nextList:
            num = self.nextList.get(key)
            total += num
        for key in self.nextList:
            top = float(self.nextList.get(key))
            self.nextList[key] = top / float(total)

        return nextList

    def get_total_following(self):
        total = 0
        for key in self.nextList:
            num = self.nextList.get(key)
            total += num
        return total
