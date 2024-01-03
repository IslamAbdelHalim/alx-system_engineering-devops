#!/usr/bin/env ruby

#Define the Pattern
redex = /hb{0,3}tn/

#Take the input
input = ARGV[0]

#making the match
match = input.match(redex)

puts match
