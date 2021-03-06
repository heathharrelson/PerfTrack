
# PerfTrack Version 1.0     September 1, 2005
# See PTLICENSE for distribution information.

import sys
from PTds import PTdataStore


class PTdS_t6:

	def __init__(self, pf):
		self.pf = pf
	

	def test6(self, testStore):
	    """ Tests getChildResources, getAncestors, addAncestors, addDescendants
	        9-1-05 -- getChildResources deprecated 
	    """
	    #9-4-05 -- comment out getChildResources parts
	#Oracle Database data   
	#    good1 = 2  # Frost. has children. has anscestor. has too many descendants
	#    good2 = 12174 # a compiler resource. no children. no ancestor. no desc
	#    good3 =  13263 # a thread resource. has ancestors. no desc
	#    good4 = 13126 # an execution resource. has descendants in several levels
	#    good5 = 13262 # a process resource. has one level of desc
	#Postgres Database data
	#    good1 = 1163 -- MCR. has 3 children. has 1 ancestor. has 3459 descendants
	#    good2 = 4836 -- inputDeck resource. no children. no ancestor. no desc.
	#    good3 = A thread resource without descendants and with ancestors does not exist yet.
	#    good4 = 4624 -- an execution resource. has descendants in several levels
	#    good5 = 4790 -- a process resource. has one level of desc.
	    bad1 = None
	    bad2 = 0
	
	    #testConnection = testStore.connectToDB(testStore.NO_DEBUG, dbname, dbpwd, dbfullname) #old Oracle
	    #testConnection = testStore.connectToDB(testStore.NO_COMMIT, dbhost, dbname, dbuser, dbpwd) #old PG
	    testConnection = testStore.connectToDB(testStore.NO_COMMIT)
	    # for now, can't continue with testing if no DB connection
	    if testConnection == False:
	        self.pf.failed("test6: ancestors/descendants:  unable to connect.")
		self.pf.failed("Test 6.0 - Unable to connect.\n")
	        return False
	    else:
	        good1 = testStore.findResourceByShortNameAndType("grid|machine",\
       	            "Frost")
	        if good1 == None:
	            print "findResourceByShortNameAndType: No match found for Frost, grid/machine"
	        elif good1 == -1:
	            print "findResourceByShortNameAndType: Found more than 1 for Frost, grid/machine"
	        else:
	            print "findResourceByShortNameAndType: Found 1 match for Frost, grid/machine %s" % good1
	        
	        #This good2 is specific to data in oracle database
	        #good2 = int(testStore.findResourceByShortNameAndType("inputDeck", "iq.h-33"))
	        #This good2 exists in Postgresql database
	        good2 = testStore.findResourceByShortNameAndType("inputDeck", \
	                   "iq.h-22")
	        if good2 == None:
	            print "findResourceByShortNameAndType: No match found for iq.h-22, inputDeck"
	        elif good2 == -1:
	            print "findResourceByShortNameAndType: Found more than 1 for iq.h-22, inputDeck"
	        else:
	            print "findResourceByShortNameAndType: Found 1 match for iq.h-22, inputDeck"
	
	        #print "POSTGRESQL: N/A"
	        #This is the oracle data 
	        #good4 = int(testStore.findResourceByName("/irs-8-545"))
	        #This is for the postgresql db
	        good4 = int(testStore.findResourceByName("irs-2-503")) 
	        if good4:
	            print "findResourceByName: Found resource with name /irs-2-503"
	        else:
	            print "findResourceByName: Did not find resource with name /irs-2-503"
	
	        #This is for the Oracle db 
	        #good5 = int(testStore.findResourceByName("/irs-8-545/Process-38"))
	        #This is for the postgresql db
	        good5 = int(testStore.findResourceByName("irs-2-503|Process-3"))
	        if good5:
	            print "findResourceByName: Found resource with name /irs-2-503/Process-3"
	        else:
	            print "findResourceByName: Did not find resource with name /irs-2-503/Process-3"
	
	        #answer1 = testStore.getChildResources(good1)
	        #if answer1 == []:
	        #    self.pf.failed("getChildResources can't find children of %d" % good1)
	        #else:
	        #    self.pf.passed("ans/desc find a child " + str(answer1) + " for " +\)
	        #          str(good1)
	
	        #answer2 = testStore.getChildResources(good2)
	        #if answer2 != []:
	        #    self.pf.failed("getChildResources found children of %d" % good3)
	        #else:
	        #    self.pf.passed("ans/desc did not find a child "+str(answer2)+" for " +\)
	        #          str(good2)
	
	        #answer3 = testStore.getChildResources(bad1)
	        #if answer3 != []:
	        #    self.pf.failed("getChildResources found children of %d" % bad1)
	        #else:
	        #    self.pf.passed("ans/desc did not find a child "+str(answer3)+" for " +\)
	        #          str(bad1)
	
	        #answer4 = testStore.getChildResources(bad2)
	        #if answer4 != []:
	        #    self.pf.failed("getChildResources found children of %d" % bad2)
	        #else:
	        #    self.pf.passed("ans/desc did not find a child "+str(answer4)+" for " +\)
	        #          str(bad2)
	
	        answer5 = testStore.getAncestors(good1)
	        if answer5 == []:
	            self.pf.failed("getAncestors can't find ans of %s" % good1)
		    self.pf.failed("Test 6.1 getAncestors can not find any ans of " + str(good1) + '\n')
	        else:
	            self.pf.passed("ans/desc finds ancestors " + str(answer5) + " for " + str(good1))
		    self.pf.passed("Test 6.1 - ans/desc finds ancestors " + str(answer5) + " for " + str(good1) + '.\n')
		
	        answer6 = testStore.getAncestors(good2)
	        if answer6 != []:
	            self.pf.failed("getAncestors found ans of %d" % good2)
		    self.pf.failed("Test 6.3 - getAncestors found ans of " + good2 + '\n')
	        else:
	            self.pf.passed("ans/desc did not find ancestors " + str(answer6) + " for " + str(good2)) #the oracle test has this as bad1, which is wrong
		    self.pf.passed("Test 6.3 - ans/desc did not find ancestors " + str(answer6) + " for " + str(good2) + '\n')
	
	        answer7 = testStore.getAncestors(bad1)
	        if answer7 != []:
	            self.pf.failed("getAncestors found ans of %d" % bad1)
		    self.pf.failed("Test 6.4 - FAIL - getAncestors found ans of " + bad1 + '\n')
	        else:
	            self.pf.passed("ans/desc did not find ancestors " + str(answer7) + " for " + str(bad1))
		    self.pf.passed("Test 6.4 - PASS - ans/desec did not find ancestors " + str(answer7) + " for " + str(bad1) + '\n')
	
	        answer8 = testStore.getAncestors(bad2)
	        if answer8 != []:
	            self.pf.failed("getAncestors found ans of %d" % bad2)
		    self.pf.failed("Test 6.5 - FAIL - getAncestors found ans of " + bad2 + '\n')
	        else:
	            self.pf.passed("ans/desc did not find ancestors " + str(answer8) + " for " + str(bad2))
		    self.pf.passed("Test 6.5 - PASS - ans/desc did not find ancestors " + str(answer8) + " for " + str(bad2) + '.\n')
	
	        try:
	           testStore.addAncestors(good2) # no anc but shouldn't except   
	        except:
	            self.pf.failed("addAncestors failed for ans list of %s" % good2)
		    self.pf.failed("Test 6.7 - FAIL - addAncestors failed for ans list of " + 'good2' + '.\n')
	        else:
	            self.pf.passed("addAncestors passed for ans list of %s" % good2)
		    self.pf.passed("Test 6.7 - PASS - addAncestors passed for ans list of " + 'good2' + '.\n')
	
	        try:
	           testStore.addAncestors(bad1) # no anc but shouldn't except   
	        except:
	            self.pf.failed("addAncestors failed for ans list of %s" % bad1)
		    self.pf.failed("Test 6.8 - FAIL - addAncestors failed for ans list of " + 'bad1' + '.\n')
	        else:
	            self.pf.passed("addAncestors passed for ans list of %s" % bad1)
		    self.pf.passed("Test 6.8 - PASS - addAncestors passed for ans list of " + 'bad1' + '.\n')
	
	        try:
	           testStore.addAncestors(bad2) # no anc but shouldn't except   
	        except:
	            self.pf.failed("addAncestors failed for ans list of %s" % bad2)
		    self.pf.failed("Test 6.9 - FAIL - addAncestors failed for ans list of bad2.\n")
	            raise
	        else:
	            self.pf.passed("addAncestors passed for ans list of %s" % bad2)
		    self.pf.passed("Test 6.9 - PASS - addAncestors failed for ans list of bad2.\n")
	
	        try:
	           testStore.addDescendants(good4)
	        except:
	           self.pf.failed("addDescendants failed for des list of %s" % good4)
		   self.pf.failed("Test 6.10 - FAIL - addDescendants failed to add des for list of good 4.\n")
	        else:
	           self.pf.passed("addDescendants passed for des list of %s" % good4)
		   self.pf.passed("Test 6.10 - PASS addDescendants passed for des list of good4.\n")
	
	        try:
	           testStore.addDescendants(good5)
	        except:
	           self.pf.failed("addDescendants failed for des list of %s" % good5)
		   self.pf.failed("Test 6.11 - FAIL - addDescendants failed for lack of des list of good5.\n")
	        else:
	           self.pf.passed("addDescendants passed for des list of %s" % good5)
		   self.pf.passed("Test 6.11 - PASS - addDescendants passed for des list of good 5.\n")
	
	        try:
	           testStore.addDescendants(bad1)
	        except:
	           self.pf.failed("addDescendants failed for des list of %s" % bad1)
		   self.pf.failed("Test 6.12 - FAIL - addDescendants failed for des lis of bad1.\n")
	        else:
	           self.pf.passed("addDescendants passed for des list of %s" % bad1)
		   self.pf.passed("Test 6.12 - PASS - addDescendants passed for des list of bad1.\n")
	
	        try:
	           testStore.addDescendants(bad2)
	        except:
	           self.pf.failed("addDescendants failed for des list of %s" % bad2)
		   self.pf.failed("Test 6.13 - FAIL - addDescendants failed for des list of bad2.\n")
	        else:
	           self.pf.passed("addDescendants passed for des list of %s" % bad2)
		   self.pf.passed("Test 6.13 - PASS - addDescendants passed for des list of bad2.\n")
	
	        testStore.abortTransaction() 
	        testStore.closeDB()
