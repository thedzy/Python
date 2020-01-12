#!/usr/bin/env python3

print('\nVariables in scope:')
for scoped_varaible in dir():
	print('\t{0}'.format(scoped_varaible))

print('\nLocal variables')
local_variables = locals().copy()
for local_variable_name in local_variables.keys():
	print('\t{0}'.format(local_variable_name))

print('\nGlobal variables')
global_varaibles = globals().copy()
for global_varaible_name in global_varaibles.keys():
	print('\t{0}'.format(global_varaible_name))
