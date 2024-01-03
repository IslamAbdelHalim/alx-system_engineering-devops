#!/usr/bin/env ruby

#Define a patter that is must match a 10 digit phone number
regex = /^[0-9]{10}/

#Taking an input
input = ARGV[0]

#matching the input
match = input.scan(regex)

puts match.join
