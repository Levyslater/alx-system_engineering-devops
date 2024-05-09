#!/usr/bin/env ruby
#regex to match sender and recipient names and
#phone numbers
print ARGV[0].scan(/from:(\+?[a-zA-Z0-9]+)/).join(",") + ","
print ARGV[0].scan(/to:(\+?\d{11})/).join(",") + ','
print ARGV[0].scan(/flags:(-?\d{1}:-?\d{1}:-?\d{1}:-?\d{1}:-?\d{1})/).join
puts