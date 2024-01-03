#!/usr/bin/env ruby

#define the pattern
redex = /[A-Z]+/

#Takin an input
input = ARGV[0]

match = input.scan(redex)

puts match.join
