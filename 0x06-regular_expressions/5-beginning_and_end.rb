#!/usr/bin/env ruby

#Define the Pattern
redex = /^h[^t]n/

#Take the input
input = ARGV[0]

#making the match
match = input.match(redex)

puts match
