import gobject
import time
source_id = gobject.timeout_add(intervalle , fonction , ...)
gobject.source_remove(source_id)
def process_a (): 
    print ( " [ process_a ] : " , time . time () , " \ n " ) 
    return True 
def process_b (): 
    print ( " [ process_b ] : " , time . time () , " \ n " ) 
    return True 
    
if __name__ == ’ __main__ ’: 
   try : 
    loop = gobject . MainLoop ()
    handle = gobject . timeout_add (500 , process_a ) # every 500 ms 
    handle2 = gobject . timeout_add (1000 , process_b ) # every 1000 ms 
    loop . run ()
   except KeyboardInterrupt : 
    print ( " Fin du programme \ n " )
    pass 

