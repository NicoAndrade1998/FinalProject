from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

Mytokens = []
inToken = ("empty", "empty")
'''
def accept_token(Mytokens):
  global inToken
  print("     accept token from the list:" + inToken[1])
  inToken = Mytokens.pop(0)


def math(Mytokens):
  print("\n----parent node math, finding children nodes:")
  global inToken 
  if (inToken[0] == "Int_Float"):
    print("child node (internal): float")
    print("    float has child node (token):" + inToken[1])
    accept_token(Mytokens)

    if (inToken[1] == "+"):
      print("child node (token):" + inToken[1])
      accept_token(Mytokens)

      print("child node (internal): math")
      math(Mytokens)

    elif (inToken[1] == "*"):
      print("child node (token):" + inToken[1])
      accept_token(Mytokens)

      print("child node (internal): math")
      math(Mytokens)

  elif (inToken[0] == "Int_Lit"):
    print("child node (internal): int")
    print("   int has child node (token):" + inToken[1])
    accept_token(Mytokens)

    if (inToken[1] == "+"):
      print("child node (token):" + inToken[1])
      accept_token(Mytokens)

      print("child node (internal): math")
      math(Mytokens)

    elif (inToken[1] == "*"):
      print("child node (token):" + inToken[1])
      accept_token(Mytokens)

      print("child node (internal): math")
      math(Mytokens)

    else:
      print("error, you need + after the int in the math")

  else:
    print("error, math expects float or int")


def exp(Mytokens):
  print("\n----parent node exp, finding children nodes:")
  global inToken
  typeT, token = inToken
  if (typeT == "Keyword"):
    print("child node (internal): keyword")
    print("   Keyword has child node (token):" + token)
    accept_token(Mytokens)
  else:
    print("expect Keyword as the first element of the expression!\n")
    return

  typeT, token = inToken
  print(inToken[0])
  if (typeT == "Identifier"):
    print("child node (token):" + token)
    accept_token(Mytokens)
  else:
    print("expect identifier as the second element of the expression!")
    return

  typeT, token = inToken
  if (token == "="):
    print("child node (token):" + token)
    accept_token(Mytokens)
  else:
    print("expect = as the third element of the expression!")
    return

  print("Child node (internal): math")
  math(Mytokens)


def parser(Mytokens):
  global inToken
  inToken = Mytokens.pop(0)
  exp(Mytokens)
  if (inToken[1] == ";"):
    print("\nparse tree building success!")
'''




def accept_token(Mytokens, box3, box4):
  global inToken
  #print("     accept token from the list:" + inToken[1])
  box3.insert(END, "     accept token from the list:" + inToken[1] + "\n")
  inToken = Mytokens.pop(0)

def print_exp(Mytokens, box3, box4):
  #print("\n----parent node if_exp, finding children nodes:")
  box3.insert(END,"\n----parent node if_exp, finding children nodes:\n")
  global inToken
  typeT, token = inToken

  if (token == "print"):
    #print("child node (token): print")
    box3.insert(END, "child node (token): print\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect print as the first element of the expression!\n")
    box3.insert(END, "expect print as the first element of the expression!\n")
    return

  if (inToken[1] == "("):
    #print("child node (token): (")
    box3.insert(END, "child node (token): (\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect ( as the second element of the expression!\n")
    box3.insert(END, "expect ( as the second element of the expression!\n\n")
    return

  if (inToken[0] == "string_literal"):
    #print("child node (internal): string_literal")
    box3.insert(END, "child node (internal): string_literal\n")
    #print("    string_literal has child node (token):" + inToken[1])
    box3.insert(END, "    string_literal has child node (token):" + inToken[1] + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect string_literal as the third element of the expression!\n")
    box3.insert(END, "expect string_literal as the third element of the expression!\n")
    return

  if (inToken[1] == ")"):
    #print("child node (token): )")
    box3.insert(END, "child node (token): )\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect ) as the fourth element of the expression!\n")
    box3.insert(END, "expect ) as the fourth element of the expression!\n\n")
    return


def comparison_exp(Mytokens, box3, box4):
  #print("\n----parent node comparison_exp, finding children nodes:")
  box3.insert(END, "\n----parent node comparison_exp, finding children nodes:\n")
  global inToken

  if (inToken[0] == "id"):
    #print("child node (internal): identifier")
    box3.insert(END, "child node (internal): identifier\n")
    #print("    identifier has child node (token):" + inToken[1])
    box3.insert(END, "    identifier has child node (token):" + inToken[1] + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect id as the first element of the comparison expression")
    box3.insert(END, "expect id as the first element of the comparison expression\n")
    return

  if (inToken[1] == ">"):
    #print("child node (token): " + inToken[1])
    box3.insert(END, "child node (token): " + inToken[1] + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    print("expect > as the second element of the comparison expression")
    box3.insert(END, "expect > as the second element of the comparison expression\n")
    return

  if (inToken[0] == "id"):
    #print("child node (internal): identifier")
    box3.insert(END, "child node (internal): identifier\n")
    #print("    identifier has child node (token):" + inToken[1])
    box3.insert(END, "    identifier has child node (token):" + inToken[1] + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect id as the third element of the comparison expression")
    box3.insert(END, "expect id as the third element of the comparison expression\n")
    return


def if_exp(Mytokens, box3, box4):
  #print("\n----parent node if_exp, finding children nodes:")
  box3.insert(END, "\n----parent node if_exp, finding children nodes:\n")
  global inToken
  typeT, token = inToken
  if (token == "if"):
    #print("child node (token): if")
    box3.insert(END, "child node (token): if\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect if as the first element of the expression!\n")
    box3.insert(END, "expect if as the first element of the expression!\n\n")
    return

  if (inToken[1] == "("):
    #print("child node (token): (")
    box3.insert(END, "child node (token): (\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expect ( as the second element of the expression!\n")
    box3.insert(END, "expect ( as the second element of the expression!\n\n")
    return

  if (Mytokens[0][1] == ">"):
    #print("child node (internal) comparison_exp")
    box3.insert(END, "child node (internal) comparison_exp\n")
    comparison_exp(Mytokens, box3, box4)
  else:
    #print("error, if_exp expects comparison_exp as the third element of the expression")
    box3.insert(END, "error, if_exp expects comparison_exp as the third element of the expression\n")
    return  # not sure if this is necessary

  if (inToken[1] == ")"):
    #print("child node (token): )")
    box3.insert(END, "child node (token): )\n")
    accept_token(Mytokens, box3, box4)
  else:
    #print("expected ) as the fourth element of the expression")
    box3.insert(END, "expected ) as the fourth element of the expression\n")

  print()


def multi(Mytokens, box3, box4):
  print("\n----parent node multi, finding children nodes:")
  box3.insert(END, "\n----parent node multi, finding children nodes:\n")
  box4.insert('math', 'end', 'multi', text= 'multi')
  global inToken
  if (inToken[0] == "float"):
    print("child node (internal): float")
    box3.insert(END, "child node (internal): float\n")
    print("   float has child node (token):" + inToken[1])
    box3.insert(END, "   float has child node (token):" + inToken[1] + "\n")
    box4.insert('multi', 'end', 'float', text= 'float: ' + inToken[1])
    accept_token(Mytokens, box3, box4)
  elif (inToken[0] == "int"):
    print("child node (internal): int")
    box3.insert(END, "child node (internal): int\n")
    print("   int has child node (token):" + inToken[1])
    box3.insert(END, "   int has child node (token):" + inToken[1] + "\n")
    box4.insert('math', 'end', 'int', text='int: ' + inToken[1])
    accept_token(Mytokens, box3, box4)

    if (inToken[1] == "*"):
      print("child node (token):" + inToken[1])
      box3.insert(END, "child node (token):" + inToken[1] + "\n")
      accept_token(Mytokens, box3, box4)

      print("child node (internal): multi")
      box3.insert(END, "child node (internal): multi\n")
      box4.insert('multi', 'end', '*', text= '*')
      multi(Mytokens, box3, box4)
    else:
      print("error, you need * after the int in the math")
      box3.insert(END, "error, you need * after the int in the math\n")


def math(Mytokens, box3, box4):
  print("\n----parent node math, finding children nodes:")
  box3.insert(END, "\n----parent node math, finding children nodes:\n")
  box4.insert('exp', 'end', 'math', text= 'math')
  global inToken

  # for a statement to be multi the first item has to be a float or the second has to be a *
  if inToken[0] == "float" or Mytokens[0][1] == "*":
    print("child node (internal): multi")
    box3.insert(END, "child node (internal): multi\n")
    multi(Mytokens, box3,box4)
  else:
    print("error, math expects multi as the first element of the expression")
    box3.insert(END, "error, math expects multi as the first element of the expression\n")

  if (inToken[1] == "+"):  # this will not detect if the value to the right is a multi
    print("child node (token):" + inToken[1])
    box3.insert(END, "child node (token):" + inToken[1] + "\n")
    box4.insert('', 'end', '+', text='+')
    box4.move('+', 'math', 'end')
    accept_token(Mytokens, box3, box4)

    print("child node (internal): multi")
    box3.insert(END, "child node (internal): multi\n")
    multi(Mytokens, box3, box4)


  else:
    print("error, math expects + as the second element of the expression")
    box3.insert(END, "error, math expects + as the second element of the expression\n")
    print("actual {}".format(inToken[1]))
    box3.insert(END, "actual {}\n".format(inToken[1]))


def exp(Mytokens, box3, box4):
  print("\n----parent node exp, finding children nodes:")
  box3.insert(END, "\n----parent node exp, finding children nodes:\n")
  box4.insert('', '0', 'exp', text= 'exp')
  global inToken
  typeT, token = inToken
  if (typeT == "key"):
    print("child node (internal): key")
    box3.insert(END, "child node (internal): key\n")
    box4.insert('exp', '1', 'key', text='keyword: ' + token)
    print("   key has child node (token):" + token)
    box3.insert(END, "   key has child node (token):" + token + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    print("expect key as the first element of the expression!\n")
    box3.insert(END, "expect key as the first element of the expression!\n\n")
    return

  if (inToken[0] == "id"):
    print("child node (internal): identifier")
    box3.insert(END, "child node (internal): identifier\n")
    box4.insert('exp', '2', 'id', text='id: ' + inToken[1])
    print("   identifier has child node (token):" + inToken[1])
    box3.insert(END, "   identifier has child node (token):" + inToken[1] + "\n")
    accept_token(Mytokens, box3, box4)
  else:
    print("expect id as the second element of the expression!")
    box3.insert(END, "expect id as the second element of the expression!\n")
    print("Actual {}".format(inToken[1]))
    box3.insert(END, "Actual {}\n".format(inToken[1]))
    return
  if (inToken[1] == "="):
    print("child node (token):" + inToken[1])
    box3.insert(END, "child node (token):" + inToken[1] + "\n")
    box4.insert('exp', '3', '=', text='=')
    accept_token(Mytokens, box3, box4)
  else:
    print("expect = as the third element of the expression!")
    box3.insert(END, "expect = as the third element of the expression!\n")
    return
  print("child node (internal): math")
  box3.insert(END, "child node (internal): math\n")
  math(Mytokens, box3, box4)


def parser(Mytokens, box3, box4):
  global inToken
  inToken = Mytokens.pop(0)
  #exp(Mytokens, box3, box4)
  #if_exp(Mytokens, box3, box4)
  '''
  if (inToken[1] == ";"):
    #print("\nparse tree building success!")
    box3.insert(END, "\nparse tree building success!\n")
  return
  '''
  if (inToken[1] == "if"):
    if_exp(Mytokens, box3, box4)
    if (inToken[1] == ":"):
      # print("\nparse tree building success!")
      box3.insert(END, "\nparse tree building success!\n")
    return
  elif(inToken[1] == "int" or inToken[1] == "float"):
    exp(Mytokens, box3, box4)
    if (inToken[1] == ";"):
      # print("\nparse tree building success!")
      box3.insert(END, "\nparse tree building success!\n")
    return
  elif (inToken[1] == "print"):
    print_exp(Mytokens, box3, box4)
    if (inToken[1] == ";"):
      # print("\nparse tree building success!")
      box3.insert(END, "\nparse tree building success!\n")
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
    token = "<int," + str(list) + ">"
    tuples = "int," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile("\d+\.\d+$")  #checking if its a float using regex
  test = r.match(list)

  if test != None and out == False:  #checking for float
    token = "<float," + str(list) + ">"
    tuples = "float," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'[=+>*]')
  test = r.match(list)

  if test != None and out == False:  #checking for operators
    token = "<op," + str(list) + ">"
    tuples = "op," + str(list)
    mytokens.append(tuples)
    out = True

  r = re.compile(r'".*"')
  test = r.match(list)

  if test != None and out == False:  #checking for string literals
    token = "<string_literal," + str(list) + ">"
    tuples = "string_literal," + str(list)
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
      token = "<key," + str(list) + ">"
      tuples = "key," + str(list)
      mytokens.append(tuples)

    else:
      token = "<id," + str(list) + ">"
      tuples = "id," + str(list)
      mytokens.append(tuples)
    out = True

  if out == False:  #only thing left would be identifiers
    token = "<id," + str(list) + ">"
    tuples = "id," + str(list)
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
    self.parselabel = Label(self.master, text="Parse Tree (Text)")
    self.parselabel.grid(row=0, column=2, sticky=W, padx=15, pady=(10, 0))

    #creting parse tree label
    self.treelabel = Label (self.master, text="Parse Tree (Visual)")
    self.treelabel.grid(row=0, column=3, sticky=W, padx=15, pady=(10,0))

    #creating input text box
    self.box1 = Text(self.master, width=30, height=10)
    self.box1.grid(row=1, column=0, sticky=W, padx=15)
    #creating output text box
    self.box2 = Text(self.master, width=30, height=10)
    self.box2.grid(row=1, column=1, sticky=W, padx=15)
    #creating parser text box
    self.box3 = Text(self.master, width=30, height=10)
    self.box3.grid(row=1, column=2, sticky=W, padx=15)
    
    #creating tree visual box
    self.box4 = ttk.Treeview()
    self.box4.grid(row=1, column=4, sticky=W, padx=15)
    
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

  def populateTree(self):   #used for testing and reference purposes. -Nico
    #Inserting parent
    self.box4.insert('', '0', 'item1', text ='Exp')
    
    # Inserting child
    self.box4.insert('', '1', 'item2', text ='key')
    self.box4.insert('', '2', 'item3', text ='identifier')
    self.box4.insert('', '3', 'item4', text ='=') 
    self.box4.insert('', 'end', 'item5', text ='math') 
    
    #Moving children under parent.
    self.box4.move('item2', 'item1', 'end')
    self.box4.move('item3', 'item1', 'end')
    self.box4.move('item4', 'item1', 'end')
    self.box4.move('item5', 'item1', 'end')

  def gonextline(self):
    #self.populateTree()
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
    parser(new_list, self.box3, self.box4)
    self.count += 1
    self.provalabel.config(text=self.count)

    if self.count == len(lines):
      messagebox.showerror(
        "Error",
        "All values in input box have been processed and the next line is empty"
      )


if __name__ == '__main__':
  myTkRoot = Tk()
  my_gui = LexerGUI(myTkRoot)
  myTkRoot.geometry("2000x1000")
  myTkRoot.resizable(False, False)
  myTkRoot.mainloop()
