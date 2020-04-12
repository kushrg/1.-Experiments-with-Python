def combine_words (word,**kwargs): 
	#print(kwargs)
    if 'prefix' in kwargs:
    	return kwargs['prefix']+word
    if 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


print(combine_words("kushal", prefix="Mr"))
print(combine_words("kushal", suffix="ganatra"))