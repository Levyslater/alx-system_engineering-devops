#!/usr/bin/env ruby
#Regex expression matchs a string that starts with h and ends with n 
#and can have any single character in between
puts ARGV[0].scan(/^h.{1}n$/).join
