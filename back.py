import sys


x =0
S=set()



class Zip():
    def __init__(self):
        self.x=x
        self.s=S

    def loof(self):
        loof_nums = sys.stdin.readline()
        loof_num = int(loof_nums)

        
        while loof_num>=0 :
            insert = sys.stdin.readline()
            insert_def = insert.split()

            def_name = insert_def[0]
            if len(insert_def) >= 2:
                x=insert_def[1]
            if  def_name == "add" :
                self.add_x(x)
            elif def_name == "remove" :
                self.remove_x(x)
            elif def_name == "check" :
                self.check_x(x)
            elif def_name == "toggle" :
                self.toggle_x(x)
            elif def_name == "all" :
                self.all()
                print(self.s)
            elif def_name == "empty" :
                self.empty()
            loof_num = loof_num - 1

    def add_x(self, x):
        match = False
        for i in self.s:
            if i == int(x):
                match = True
            else :
                match = False

        if match == False:
            self.s.add(int(x))
        else: pass


    def remove_x(self, x):
        match = False
        for i in self.s:
            if i == int(x):
                match = True
                break
            else:
                match = False

        if match == True:
            self.s.remove(int(x))

    def check_x(self, x):
        match = False
        for i in self.s:
            if i == int(x):
                match = True
                break
            else:
                match = False

        if match ==True:
            print(1)
        else:
            print(0)


    def toggle_x(self, x):
        match = False
        for i in self.s:
            if i == int(x):
                match = True
                break
            else:
                match = False

        if match == True:
            self.s.remove(int(x))
        else:
            self.s.add(int(x))

    def all(self):
        self.s = set()
        for i in range(1,21):
            self.s.add(i)

    def empty(self):
        self.s=set()

zip = Zip()
zip.loof()











