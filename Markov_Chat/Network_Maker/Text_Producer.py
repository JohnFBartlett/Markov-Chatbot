

class Text_Producer:

    # For single word token prediction
    @staticmethod
    def single_word_prediction(data, outName):
        currToken = data.get('.')

        out = open(outName, 'w')
        for i in range(0, 10):
            print("\nStatement " + str(i))
            out.write("\nStatement " + str(i))
            for i in range(0,30):
                word = ''
                try:
                    word = currToken.pick_word()
                except(AttributeError):
                    print('.pick_word() resulted in NoneType')
                    break
                if word:
                    print(word, end=' ')
                    out.write(word + ' ')
                else:
                    print('Nothing left')
                    out.write('Nothing left')
                    break
                currToken = stuff.get(word)
                if not currToken:
                    print('Token for ' + word + ' not found')
                    out.write('Token for ' + word + ' not found')
            out.write('\n')
        out.close()

    # For double word token prediction
    @staticmethod
    def double_word_prediction(data, outName):
        # Start out getting a second word

        out = open(outName, 'w')
        for i in range(0, 10):
            print("\nStatement " + str(i))
            out.write("\nStatement " + str(i))
            word1 = '.'
            part1 = data.get(word1)
            try:
                word2 = part1.pick_word()
            except(AttributeError):
                # print('.pick_word() resulted in NoneType')
                out.write('.pick_word() resulted in NoneType')
            if word2:
                print(word2, end=' ')
                out.write(word2 + ' ')
            else:
                # print('Nothing left')
                out.write('Nothing left')

            if '.' == word2:
                print('PERIOD')
                currToken = stuff.get(word1 + '.')
            else:
                currToken = stuff.get(word1 + ' ' + word2)
            if not currToken:
                # print('Token for ' + word1 + ' ' + word2 + ' not found')
                out.write('Token for ' + word1 + ' ' + word2 + ' not found')

            for i in range(0, 30):
                # Get previous two words if possible
                word1 = word2
                try:
                    word2 = currToken.pick_word()
                except(AttributeError):
                    # print('.pick_word() resulted in NoneType')
                    out.write('.pick_word() resulted in NoneType')
                    break
                if word2:
                    print(word2, end=' ')
                    out.write(word2 + ' ')
                else:
                    # print('Nothing left')
                    out.write('Nothing left')
                    break
                if '.' == word2:
                    word1 = '.'
                    part1 = data.get(word1)
                    word2 = part1.pick_word()
                    print(word2, end=' ')
                    out.write(word2 + ' ')
                currToken = stuff.get(word1 + ' ' + word2)
                if not currToken:
                    # print('\nToken for ' + word1 + ' ' + word2 + ' not found')
                    out.write('Token for ' + word1 + ' ' + word2 + ' not found')
        out.close()

    # For triple word token prediction
    # TODO: This ^

if __name__ == '__main__':
    from Network_Maker.File_Parser import FileParser
    from Network_Maker.File_Parser import Token
    parserTokens = FileParser(False)
    person = 'Caroline Strauss'
    stuff = parserTokens.parse_plaintext(person + '.txt')

    curr = stuff.get('.')
    blah = curr.get_next_list()
    print("Possible Starting tokens: " + str(blah))

    print('++++++++++++++++++++++++++++++++++++++++++')
    print('Making single token prediction sentences')
    one_out = person + 'one_w_speech.txt'
    Text_Producer.single_word_prediction(stuff, one_out)

    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++')
    print('Making double token prediction sentences')
    two_out = person + 'two_w_speech.txt'
    Text_Producer.double_word_prediction(stuff, two_out)

