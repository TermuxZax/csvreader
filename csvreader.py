import sys

__banner__ = 'Csv Reader python v2.0 Created by @ciku370'
__author__ = '@ciku370'

class csv:
    def get_content(self):
        """take the title and fill from the file"""
        try:
            for i in open(self.FILE,'r').readlines():
                # take the title
                if self.S_ == 0:
                    self.TITLE = i.strip().split(',')
                    self.S_ += 1
                # take the contents
                else:
                    x = i.strip().split(',')
                    ai = {}
                    for i_ in range(0,len(self.TITLE)):
                        try:
                            ai.update({self.TITLE[i_]:x[i_]})
                        except IndexError: # If there is an empty column
                            ai.update({self.TITLE[i_]:''})
                    self.RESULTS.append(ai)
        except Exception as e: # If the file is not loaded
            print('\n%s\nError:%s\n'%(__banner__,str(e)))
            exit()
    def get_long_word(self):
        """looking for the longest word"""
        self.max_all = {i:len(i) for i in self.TITLE}
        for i in range(0,len(self.RESULTS)):
            for _ in self.RESULTS[i]:
                if len(self.RESULTS[i][_]) >= self.max_all[_]:
                    self.max_all[_] = len(self.RESULTS[i][_])
    def _table_(self):
        """create header and footer"""
        for i in self.max_all:
            sys.stdout.write((self.max_all[i]+2)*'-'+'+')
    def create_table(self):
        """Create and display table in the terminal"""
        # print title
        sys.stdout.write('\nread the CSV file from: %s\n\n   +-----+' % self.FILE)
        self._table_()
        sys.stdout.write('\n   | ID  |')
        for i in self.max_all:
            sys.stdout.write(i.center(self.max_all[i]+2)+'|')
        sys.stdout.write('\n   +-----+')
        self._table_()
        # print data
        print '' # new line
        for x in range(0,len(self.RESULTS)):
            sys.stdout.write('   | '+(str(x+1)+(int(int(4)-int(len(str(x+1))))*' ')+'|'))
            for i in self.max_all:
                sys.stdout.write(' '+self.RESULTS[x][i]+((self.max_all[i]-len(self.RESULTS[x][i])+1)*' ')+'|')
            print '' # new line
        sys.stdout.write('   +-----+')
        for i in self.max_all:
            sys.stdout.write((self.max_all[i]+2)*'-'+'+')
        print '\n\n%s\n' % __banner__
    def __init__(self,file):
        self.FILE = file
        self.S_ = 0
        self.RESULTS = []
        self.get_content()
        self.get_long_word()
        self.create_table()
if __name__ == '__main__':
    try:
        csv(sys.argv[1])
    except IndexError:
       print '\n%s\nUsage: python2 %s data.csv\n' % (__banner__,sys.argv[0])
