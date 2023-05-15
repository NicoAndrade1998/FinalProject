''' Original file by Edgar Fong
    Modified by Nico Andrade 5-10-2023, 5-12-2023, 5-15-2023
    Modified by Saul Romero  
'''

# Traceback: 260 -> 81 -> 54 -> 20

from tkinter import *
from tkinter import messagebox
import re
from ply import yacc

inToken = ("empty", "empty")
Mytokens = [] 


def accept_token():
  global inToken
  global Mytokens
  print("     accept token from the list:" + inToken[1])
  #inToken = Mytokens.pop(0)


def math():
    print("\n----parent node math, finding children nodes:")
    global inToken
    if(inToken[0]=="Float_Literal"):
        print("child node (internal): float")
        print("   float has child node (token):"+inToken[1])
        accept_token()
    elif (inToken[0]=="Int_Literal"):
        print("child node (internal): int")
        print("   int has child node (token):"+inToken[1])
        accept_token()

        if(inToken[1]=="+"):
            print("child node (token):"+inToken[1])
            accept_token()

            print("child node (internal): math")
            math()
        else:
            print("error, you need + after the int in the math")

    else:
        print("error, math expects float or int")

def exp():
    print("\n----parent node exp, finding children nodes:")
    global inToken
    typeT,token=inToken
    if(typeT=="Identifier"):
        print("child node (internal): identifier")
        print("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect identifier as the first element of the expression!\n")
        return
    print("inToken[2] = " + inToken[1])
    if(inToken[1]=="Operator,="):
        print("child node (token):"+inToken[1])
        accept_token()
    else:
        print("expect = as the second element of the expression!")
        return

    print("Child node (internal): math")
    math()


def parser(Mytokens):
  global inToken
  inToken = Mytokens.pop(0)
  exp(Mytokens)
  if (inToken[1] == ";"):
    print("\nparse tree building success!")


def makeParseTree(Mytokens):
    global inToken
    inToken=Mytokens.pop(0)
    exp()
    if(inToken[1]==";"):
        print("\nparse tree building success!")
    return


def CutOneLineTokens(sample):
  newList = []
  str1 = ""
  inStringFlag = False

  for x in sample:
    #print(x)
    if x == '"':
      if inStringFlag == True:
        inStringFlag = False
      elif inStringFlag == False:
        inStringFlag = True

    if inStringFlag:
      str1 += x
      continue

    if x == "=" or x == "+" or x == ">" or x == "*" or x == "(" or x == ")" or x == ":" or x == ";":
      if str1 != "":
        newList.append(str1)
      newList.append(x)
      str1 = ""
      #print ("test")

    elif x.isspace() == False:
      str1 += x
      #print(str1)

    elif str1 != "":
      newList.append(str1)
      str1 = ""

  if str1 != "":
    newList.append(str1)
  print(newList)
  return newList


def Tokens(list):
  r = re.compile(r'^\d+$')  #checking if its an int
  out = False
  test = r.match(list)
  token = ""
  mytokens = []

  if test != None:  #checking for int
    token = "<Int_Literal," + str(list) + ">"
    tuples = "Int_Literal," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile("\d+\.\d+$")  #checking if its a float using regex
  test = r.match(list)

  if test != None and out == False:  #checking for float
    token = "<Float_Literal," + str(list) + ">"
    tuples = "Float_Literal," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'[=+>*]')
  test = r.match(list)

  if test != None and out == False:  #checking for operators
    token = "<Operator," + str(list) + ">"
    tuples = "Operator," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'".*"')
  test = r.match(list)

  if test != None and out == False:  #checking for string literals
    token = "<String_Literal," + str(list) + ">"
    tuples = "String_Literal," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'[():";]')
  test = r.match(list)

  if test != None and out == False:  #checking for separators
    token = "<Separator," + str(list) + ">"
    tuples = "Separator," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'^[a-zA-Z]+$')
  test = r.match(list)

  if test != None and out == False:  #checking for string literals and key words
    #sincekeywords and string literals match regex
    if list == "if" or list == "else" or list == "float" or list == "int":
      token = "<Keyword," + str(list) + ">"
      tuples = "Keyword," + str(list)
      mytokens.append(tuples)

    else:
      token = "<Identifier," + str(list) + ">"
      tuples = "Identifier," + str(list)
      mytokens.append(tuples)
    out = True

  if out == False:  #only thing left would be identifiers
    token = "<Identifier," + str(list) + ">"
    tuples = "Identifier," + str(list)
    mytokens.append(tuples)
  return token, mytokens


class LexerGUI:

  def __init__(self, root):
    self.master = root
    self.master.title("Lexer and Parser for TinyPie")
    self.count = 0
    #creating input label
    self.inlabel = Label(self.master, text="Source Code")
    self.inlabel.grid(row=0, column=0, sticky=W, padx=15, pady=(10, 0))
    #creating output label
    self.outlabel = Label(self.master, text="Tokens")
    self.outlabel.grid(row=0, column=1, sticky=W, padx=15, pady=(10, 0))
    #creating parser label
    self.parselabel = Label(self.master, text="Parse Tree")
    self.parselabel.grid(row=0, column=2, sticky=W, padx=15, pady=(10, 0))
    #creating input text box
    self.box1 = Text(self.master, width=30, height=10)
    self.box1.grid(row=1, column=0, sticky=W, padx=15)
    #creating output text box
    self.box2 = Text(self.master, width=30, height=10)
    self.box2.grid(row=1, column=1, sticky=W, padx=15)
    #creating parser text box
    self.box3 = Text(self.master, width=30, height=10)
    self.box3.grid(row=1, column=2, sticky=W, padx=15)
    #creating line proccess label
    self.prolabel = Label(self.master, text="Current Processing Line: ")
    self.prolabel.grid(row=2, column=0, sticky=W, padx=15)

    #creating line proccess value label
    self.provalabel = Label(self.master, text=self.count)
    self.provalabel.grid(row=2, column=0, sticky=E, padx=(0, 35))
    #creating next line button
    self.nextb = Button(self.master, text="Next Line", command=self.gonextline)
    self.nextb.grid(column=0, row=3, sticky=E, padx=(0, 35))
    #creating quit button
    self.quitb = Button(self.master, text="Quit", command=myTkRoot.quit)
    self.quitb.grid(column=1, row=3, sticky=E, padx=(0, 35))

  def gonextline(self):
    mytokens = []
    #getting user input from txt box
    text = self.box1.get("1.0", "end")
    #putting it into a list
    lines = text.split('\n')
    if lines[-1] == '':
      lines[-1] = '\n'  # removing last empty element if it exists
    # highlight previous line
    if self.count > 0:
      self.box1.tag_remove("highlight", f"{self.count}.0", f"{self.count}.end")
    #highlight current line
    self.box1.tag_add("highlight", f"{self.count+1}.0", f"{self.count+1}.end")
    self.box1.tag_config("highlight", background="yellow")

    #getting the first line and using HW3 Cut one line to separate it
    cutLines = CutOneLineTokens(lines[self.count])

    #calling Tokens and getting our input tokenized
    for x in cutLines:
      result = Tokens(x)
      mytokens.append(result[1])
      self.box2.insert(END, result[0] + "\n")

    new_list = list(tuple(item[0].split(',')) for item in mytokens)
    makeParseTree(new_list) #Changed from calling parser() to calling makeParseTree()
    self.count += 1
    self.provalabel.config(text=self.count)

    if self.count == len(lines):
      messagebox.showerror(
        "Error",
        "All values in input box have been processed and th next line is empty"
      )


if __name__ == '__main__':
  myTkRoot = Tk()
  my_gui = LexerGUI(myTkRoot)
  myTkRoot.geometry("830x250")
  myTkRoot.resizable(False, False)
  myTkRoot.mainloop()
