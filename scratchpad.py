from ply import yacc

# Define the grammar rules
grammar = '''
expression : expression '+' expression
           | expression '*' expression
           | NUMBER
'''

# Define parsing functions
def p_expression_plus(p):
    'expression : expression "+" expression'
    p[0] = ("+", p[1], p[3])

def p_expression_times(p):
    'expression : expression "*" expression'
    p[0] = ("*", p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Define token names
tokens = (
    'NUMBER',
)




# Build the parser
parser = yacc.yacc()

# Define token patterns using regular expressions
t_NUMBER = r'\d+'

# Parse an input expression
input_expr = "2 + 3 * 4"
parse_tree = parser.parse(input_expr)
print(parse_tree)










#float mathresult1 = 5*4.3 + 2.1;
#assignexp :- keyword(int|float) variable mathexp separator(;)
#mathexp :- num_literal +|* num_literal|mathexp


#if (mathresult1 > mathresult2):
#conditional :- keyword(if) separator(() variable operator(<|>) variable separator()) separator(:)

#print("I just built some parse trees");
#funcall :- variable separator(() variable|literal separator()) separator(;)