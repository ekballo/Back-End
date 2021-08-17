import random, string

tamnho = 16

chars = string.ascii_letters + string.digits + '2@fe47jr24'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range (tamnho)))