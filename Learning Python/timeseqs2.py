#File timeseqs.py
"Test the relative speed of iteration tool alternatives."
import sys, timer2 as timer # Import timer functions
reps = 10000
repslist = list(range(reps)) # Hoist out, list in both 2.X/3.X
def edi(x):
    return x + 10
def forLoop():
    res = []
    for x in repslist:
        res.append(edi(x))
    return res
def listComp():
    return [edi(x) for x in repslist]
def mapCall():
    return list(map(edi, repslist)) # Use list() here in 3.X only!
     # return map(abs, repslist)
def genExpr():
    return list(edi(x) for x in repslist) # list() required to force results
def genFunc():
    def gen():
        for x in repslist:
            yield edi(x)
    return list(gen()) # list() required to force results
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
