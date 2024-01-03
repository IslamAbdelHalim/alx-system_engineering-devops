#!/usr/bin/env ruby

#Define The regex to match
reg = /School/

input = ARGV[0]

match = input.scan(reg)

puts match.join
