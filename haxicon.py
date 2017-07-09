# Tested on Kali Debian Linux.
import sys

# First of all, this is for fun and profit.
# Second of all, I am VERY surprised python doesn't have a switch/case statement,
# I saw dictionary/structures examples, but I'm going for occam's razor.
# This script is meant to translate everything you type into h@ck3rc0d3
# without the delays of typing "h@ck3rc0d3" manually.

# I'm just doing vowels for now.
# I can add a "random char" function but I don't know about the readability
# Add API functions so that it can communicate with a forum.

print "Type some shit\n=============="

charray = ['\x40', '\x33', '\x21', '\x30', '\x23'] # <- Change these
string = raw_input("> ")

def replacer(string):
    replace = string.replace("a", charray[0])\
                    .replace("A", charray[0])\
                    .replace("e", charray[1])\
                    .replace("E", charray[1])\
                    .replace("i", charray[2])\
                    .replace("I", charray[2])\
                    .replace("o", charray[3])\
                    .replace("O", charray[3])\
                    .replace("u", charray[4])\
                    .replace("U", charray[4])
    print replace

replacer(string)
