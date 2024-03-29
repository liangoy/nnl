import re

'''
string
'''

c1=re.compile('(\n+)')
c2=re.compile('(?:"")|(?:"\t+")')

def _encode(t):
    t=t.replace('"','""')
    t=c1.sub('"\\1"',t).replace('\n','\t')
    return t

def fn(matched):
    x=matched.group(0)
    return '"' if x=='""' else '\n'*(len(x)-2)

def _decode(t):
    t=c2.sub(fn,t)
    return t

'''
bytes
'''

bc1=re.compile(b'(\n+)')
bc2=re.compile(b'(?:"")|(?:"\t+")')

def _bencode(t):
    t=t.replace(b'"',b'""')
    t=bc1.sub(b'"\\1"',t).replace(b'\n',b'\t')
    return t

def bfn(matched):
    x=matched.group(0)
    return b'"' if x==b'""' else b'\n'*(len(x)-2)

def _bdecode(t):
    t=bc2.sub(bfn,t)
    return t

'''
merge
'''
def decode(t):
    '''

    :param t: str or bytes
    :return: str or bytes
    '''
    return _decode(t) if type(t)==str else _bdecode(t)

def encode(t):
    '''

    :param t: str or bytes
    :return: str or bytes
    '''
    return _encode(t) if type(t)==str else _bencode(t)

