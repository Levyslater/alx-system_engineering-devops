#!/usr/bin/env ruby
#Regex expression that must match a 10 digit phone number
puts ARGV[0].scan(/(?<!\s)[0-9]{10}/).join
