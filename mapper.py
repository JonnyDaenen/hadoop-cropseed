#!/usr/bin/env python

# Mapper
# Author: Jonny Daenen
# Date created: 2014-11-13
#
# Given a file with a min and max in it,
# this mapper generates max - min tuples
# using a given function that returns strings.
# When the function returns None, the mappers stops,
# when it returns an empty string, it skips this output.
# When the function returns a list of strings,
# each of them is output on a separate line.
#
#

import sys
import imp

# determine module filename
funcfile = "functions.py"
function = "generate_keyvalue"
if len(sys.argv) > 2:
    funcfile = sys.argv[1];
    function = sys.argv[2];

# extra argument: total number of rows
# to pass to the function
totalRows = None
if len(sys.argv) > 3:
    totalRows = sys.argv[3]



# remove extension
module_name = funcfile.split(".")
module_name.pop()
module_name = reduce(lambda x,y: x + "." + y ,module_name)

# load module and function
module = imp.load_source(module_name,funcfile)
generate_keyvalue = getattr(module,function)

# set global value for n in the module
module.n = int(totalRows)


# apply function to the given range of values
for line in sys.stdin:
    
    # determine range
    line = line.strip()
    keys = line.split()
    
    min = int(keys[0])
    max = int(keys[1])
    
    # check if there is an extra field
    module.m = 0
    if len(keys) >= 3:
        module.m = int(keys[2])
        
    
    # for all the indexes we need to consider
    for i in range(min,max+1):
        
        # generate the i-th tuple
        s = generate_keyvalue(i)
        
        # None stops output 
        if s == None:
            sys.exit(0)
            
        # convert to tuple/list if necessary
        vals = s
        if (not isinstance(s, (list,tuple))):
            vals = [s]
            
        for s in vals:
            #output row only if non-empty
            if s != "":
                print s