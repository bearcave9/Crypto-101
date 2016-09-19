#!/usr/bin/python
# -*- coding: utf-8 -*-
#----------------------------------
# Author- Prakhar Pratyush
# Learn Python The Hard Way
#
#----------------------------------

my_name = 'Prakhar Pratyush'
my_age = 21
my_height= 170 # cm
my_weight= 65 # kg
my_eyes= 'Brown'
my_teeth= 'white'
my_hair= 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(my_age, my_height,
	my_weight, my_age + my_height+ my_weight)

# %r -- print this no matter what

print round(1.7333) #Rounding a floating point number