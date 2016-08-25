
#!/usr/bin/env python
import thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()) )

def main():
    try:
        thread.start_new_thread( print_time, ( "TH1", 2, ) )
        thread.start_new_thread( print_time, ( "TH2", 5, ) )
    except:
        print "FAIL to create thread"

    while 1:
        pass

    return 0

if __name__ == '__main__':
    main()
