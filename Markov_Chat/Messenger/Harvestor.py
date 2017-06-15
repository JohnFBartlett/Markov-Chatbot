import re

class People_Harvestor:
    @staticmethod
    def harvest_from_sender(sender, file):
        with open(file, 'r') as f:
            copying = False
            out = open(sender + '.txt', 'w')
            for line in f:
                if copying:
                    out.write(line)
                    print(line)
                    copying = False
                elif sender in line:
                    print('---')
                    print(line)
                    copying = True

if __name__ == '__main__':
    # from Messenger import harvest_from_sender
    People_Harvestor.harvest_from_sender('Caroline Strauss', 'Facebook-messages.txt')