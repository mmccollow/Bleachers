import ply.lex as lex

tokens = (
	'SEPARATOR',
	'PLAYSEPARATOR',
	'ADVANCESEPARATOR',
	'OUT',
	'WILDPITCH',
	'ADVANCE',
	'UNEARNEDRUN',
	'PUTOUT',
	'BASEHIT',
	'WALK',
	'STRIKEOUT',
	'HITTYPE'
)

t_SEPARATOR = r'\/'
t_PLAYSEPARATOR = r'\;'
t_ADVANCESEPARATOR = r'\.'
t_OUT = r'^FC\d|\d+'
t_WILDPITCH = r'^WP'
t_ADVANCE = r'[123]-[23H]'
t_UNEARNEDRUN = r'\(NR\)'
t_PUTOUT = r'\(\d\)'
t_BASEHIT = r'^[SDT]+\d|HR'
t_WALK = r'^W'
t_STRIKEOUT = r'^K'
t_HITTYPE = r'[GDPLFR]+'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

# for testing
def tokenize():
	while True:
		tok = lexer.token()
		if not tok: break
		print tok
