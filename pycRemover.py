import os
import sys

def Usage():
    print "pycRemover.py <Folder> \nExample: pycRemover.py 'C:\Program Files (x86)\FolderThatHasPYCfiles'"


if __name__ == "__main__":
    
    try:
        path = sys.argv[1] 
        raw_input("PYC files will be deleted from %s \nPress ENTER key to continue ..." %(path))    
        for root,dir,files in os.walk(path):
            for f in files:
                if f.endswith("pyc"):
                    fn = os.path.join(root,f)
                    os.remove(fn)
                    print "Removed {}".format(fn)
    except IndexError, ie:
        print "Please use the script as below"
        Usage()
    except Exception,e:
        print "Exception:\n"
        print "%s" %str(e)
        raw_input("Exception")
            
raw_input("Done")
raw_input()