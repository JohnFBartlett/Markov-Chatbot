from Network_Maker.Token import Token
import re


class FileParser:

    global tokens
    global debugMode

    def __init__(self, debug):
        self.tokens = dict()
        self.debugMode = debug

    def parse_plaintext(self, file):

        with open(file, 'r') as text:
            first = ''
            second = ''
            third = ''
            after =  ''
            i = 0
            for line in text:
                i += 1
                print('Line ' + str(i))
                for word in re.split(' |\n|\t|,', line):
                    if self.debugMode:
                        print('_________________________________')
                        print(word)
                    if not word:
                        continue
                    if '.' == word[-1]:
                        after = word[:-1]
                        self.lookBackAtIt(first, second, third, after)
                        first = second
                        second = third
                        third = after
                        after = '.'
                    else:
                        after = word
                    startOver = self.lookBackAtIt(first, second, third, after)
                    if startOver:
                        first = ''
                        second = ''
                        third = '.'
                        after = ''
                    else:
                        first = second
                        second = third
                        third = after
            after = ''
            self.lookBackAtIt(first, second, third, after)
        return self.tokens

    def lookBackAtIt(self, first, second, third, after):
        debug = self.debugMode
        # if all 3 variables are declared
        if debug:
            print("first: " + first + ", second: " + second + ", third: " + third + ", after: " + after)
        check = False
        if first:
            combined = first + ' ' + second + ' ' + third
            for t in self.tokens:
                if combined == t:
                    check = True
                    temp = self.tokens.get(t)
                    temp.update_next(after)
                    self.tokens[t] = temp
                    if debug:
                        print("Words following " + t + ": " + str(temp.get_next_list()))
                        # print("Printing dictionary so far")
                        # for item in self.tokens:
                        #     print(item)
            if not check:
                newToken = Token(combined, after)
                if debug:
                    print("====")
                    print("Storing combined: " + combined)
                self.tokens[combined] = newToken
                if debug:
                    print("Words following " + combined + ": " + str(newToken.get_next_list()))
                # print("Printing dictionary so far")
                # for item in self.tokens:
                #     print(item)

        # if at least 2 are declared
        if second:
            combined = second + ' ' + third
            for t in self.tokens:
                if combined == t:
                    check = True
                    temp = self.tokens.get(t)
                    temp.update_next(after)
                    self.tokens[t] = temp
                    if debug:
                        print("Words following " + t + ": " + str(temp.get_next_list()))
                    # print("Printing dictionary so far")
                    # for item in self.tokens:
                    #     print(item)
            if not check:
                newToken = Token(combined, after)
                if debug:
                    print("Storing combined: " + combined)
                self.tokens[combined] = newToken
                if debug:
                    print("Words following " + combined + ": " + str(newToken.get_next_list()))
            # print("Printing dictionary so far")
            # for item in self.tokens:
            #     print(item)

        # if at least 1 is declared
        if third:
            for t in self.tokens:
                if third == t:
                    check = True
                    temp = self.tokens.get(t)
                    temp.update_next(after)
                    self.tokens[t] = temp
                    if debug:
                        print("Words following " + t + ": " + str(temp.get_next_list()))
                    # print("Printing dictionary so far")
                    # for item in self.tokens:
                    #     print(item)
            if not check:
                newToken = Token(third, after)
                if debug:
                    print("Storing third: " + third)
                self.tokens[third] = newToken
                if debug:
                    print("Words following " + third + ": " + str(newToken.get_next_list()))
                # print("Printing dictionary so far")
                # for item in self.tokens:
                #     print(item)
        else:
            for t in self.tokens:
                # print('no variables stored, going through tokens... ' + t)
                if '' == t:
                    check = True
                    temp = self.tokens.get(t)
                    temp.update_next(after)
                    self.tokens[t] = temp
                    if debug:
                        print("Words following " + t + ": " + str(temp.get_next_list()))
                    # print("Printing dictionary so far")
                    # for item in self.tokens:
                    #     print(item)
            if not check:
                # print('no variables stored, nothing in tokens yet')
                newToken = Token('.', after)
                self.tokens['.'] = newToken
                if debug:
                    print("Words following " + '' + ": " + str(newToken.get_next_list()))
                # print("Printing dictionary so far")
                # for item in self.tokens:
                #     print(item)

        if '.' in after:
            # make function call itself with words shifted over and period by itself as after
            return True
        else:
            return False


