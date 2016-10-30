import random

def get_t():
	if random.random() < 0.99:
		return True
	return False

def get_c(t):
	if t and random.random() < 0.95:
		return True
	return False

def get_sample():
	t = get_t()
	c = get_c(t)
	return [t, c]