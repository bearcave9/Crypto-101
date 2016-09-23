#!/usr/bin/python
# -*- coding: utf-8 -*-
#----------------------------------
# Author- Prakhar Pratyush
# Learn Python The Hard Way
#
#----------------------------------


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x  # %r is used for debugging to output raw data
# here a string with apostrophe

print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r" # incomplete 

print joke_evaluation % hilarious  # Now complete

w = "This is the left side of..."
e = "a string with a right side."

print w + e