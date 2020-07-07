#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+\d+|\W+\w+|\w+).*to:(\+\d+|\W+\w+|\w+).*flags:([\W+\d]{0,}\d)/).join(',')

