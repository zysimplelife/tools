from misc import has_same_load

print 'init giop protocol'

'''
http://community.microfocus.com/microfocus/corba/visibroker_-_world_class_middleware/w/knowledge_base/16544.how-to-read-giop-message-and-correlate-request-and-reply.aspx


'''
def match(pkt, load):
  if hasattr(pkt, 'load'):
    return pkt.load[16:] == load[16:]
  
def adjust(pkt, res):
  #print "adjust resp " + repr(res[0]) 
  res[0].load = res[0].load[0:12]+pkt.load[12:16]+res[0].load[16:]
  return res
