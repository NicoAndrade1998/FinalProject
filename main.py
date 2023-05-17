''' Original file by Edgar Fong
    Modified by Nico Andrade 5-10-2023, 5-12-2023, 5-15-2023
    Modified by Saul Romero 
    Tree class borrowed from  https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
'''

# Traceback: 260 -> 81 -> 54 -> 20

from tkinter import *
from tkinter import messagebox
import re
from ply import yacc

inToken = ("empty", "empty")
Mytokens = [] 

tokens = (
    'Int_literal', 'Float_literal', 'Operator', 'String_literal', 'Separator', 'Keyword', 'Identifier'
)


class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

def testTree ():
    myTree = Node(10)
    myTree.insert( 5)
    myTree.insert( 2)
    myTree.insert( 7)
    myTree.insert( 12)

    myTree.PrintTree()



def makeParseTree(MytokenList):
    global inToken
    inToken=MytokenList.pop(0)
    #exp()
    #print (inToken[0]) 
    #print (inToken[1])
    if(inToken[1]== ';'):
        print("\nparse tree building success!")
    return


#CutOneLineTokens splits input into separate tokens
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

#Tokens lexes tokens and determines what type they are
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
  #creates main GUI window
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

  #gonextline is called when the next line button is pressed. It will call the lexer and parser and display the corresponding results on screen  
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
    print (new_list)
    makeParseTree(new_list) #Changed from calling parser() to calling makeParseTree()
    self.count += 1
    self.provalabel.config(text=self.count)

    if self.count == len(lines):
      messagebox.showerror(
        "Error",
        "All values in input box have been processed and th next line is empty"
      )


if __name__ == '__main__':
  testTree()
  myTkRoot = Tk()
  my_gui = LexerGUI(myTkRoot)
  myTkRoot.geometry("830x250")
  myTkRoot.resizable(False, False)
  myTkRoot.mainloop()
