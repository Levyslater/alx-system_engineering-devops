#!/usr/bin/env ruby
#Regex Expression to match the string hbtn
#with 2 to 5 t characters
puts ARGV[0].scan(/hbt{2,5}n/).join
