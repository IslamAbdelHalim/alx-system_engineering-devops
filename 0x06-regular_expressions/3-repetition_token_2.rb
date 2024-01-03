#!/usr/bin/env ruby

#Define the Pattern
redex = /hbtt*n/

#Take the input
input = ARGV[0]

#making the match
match = input.match(redex)

puts match
