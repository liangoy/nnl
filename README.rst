** Eg


'''

    import nnl
    l=['hello \n hello','hi \n hi']
	
    '''
	encode
	'''
	
    text='\n'.join([nnl.encode(i)for i in l])
    
    with open('test.txt' ,'w') as f:
        f.write(text)
    
	'''
	decode
	'''
    with open('test.txt') as f:
        text_lines=f.read().splitlines()
    
    text_lines=[nnl.decode(i)for i in text_lines]
    
    print(text_lines==l)

'''

