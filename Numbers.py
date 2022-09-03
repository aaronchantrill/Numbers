#!/usr/bin/env python
import random
from pprint import pprint

ones = [
	'ONE',
	'TWO',
	'THREE',
	'FOUR',
	'FIVE',
	'SIX',
	'SEVEN',
	'EIGHT',
	'NINE',
	'TEN'
]
oneteens = ones.copy()
oneteens.extend([
	'ELEVEN',
	'TWELVE',
	'THIRTEEN',
	'FOURTEEN',
	'FIFTEEN',
	'SIXTEEN',
	'SEVENTEEN',
	'EIGHTEEN',
	'NINETEEN'
])
tens = [
	'TWENTY',
	'THIRTY',
	'FORTY',
	'FIFTY',
	'SIXTY',
	'SEVENTY',
	'EIGHTY',
	'NINETY'
]
hundred = [
	'HUNDRED'
]
magnitude = [
	'THOUSAND',
	'MILLION',
	'BILLION',
	'QUADRILLION'
]
# It's not normal to say "TEN HUNDRED" since that would be "ONE THOUSAND", but "NINE HUNDRED" or "ELEVEN HUNDRED" are both acceptable
leadinghundred = ['A']
leadinghundred.extend(ones[:9])
print(leadinghundred)
leadinglasthundred=leadinghundred.copy()
leadinglasthundred.extend(oneteens)
leadinglasthundred.extend([" ".join([ten,one]) for ten in tens for one in ones[:9]])
leadingmagnitude = leadinglasthundred.copy()
leadingmagnitude.extend(['TEN'])
trailing = oneteens.copy()
trailing.extend(tens)

trailing.extend([" ".join([ten,one]) for ten in tens for one in ones[:9]])
# Most people don't say "ZERO HUNDRED AND THREE". One notable exception is military time where it is common to say
# "OH EIGHT HUNDRED HOURS". People also usually don't say "one thousand, zero hundred and twenty three" unless they
# have been listing off numbers which do include a hundreds place and want to clarify.
trailing.extend(['ZERO', 'OH'])
temp = ["AND {}".format(number) for number in trailing]
trailing.extend(temp)

# [leadingmagnitudehundred hundred]? [[AND]? oneteens]
# [leadingmagnitudehundred hundred] [[AND]? oneteens]?
print(" ".join([random.choice(oneteens)]))
print(" ".join([random.choice(tens)]))
print(" ".join([random.choice(tens),random.choice(ones[:9])]))
print(" ".join([random.choice(leadinglasthundred),hundred[0]]))
print(" ".join([random.choice(leadinglasthundred),hundred[0],random.choice(trailing)]))
# with the magnitudes, you can have any number of repeating "LEADINGMAGNITUDE MAGNITUDE LEADINGHUNDRED HUNDRED TRAILING..."
# but the magnitudes have to stay in order. In other words, you can have "ONE BILLION ONE HUNDRED MILLION" but people only say
# "A MILLION BILLION" when they mean an uncountable number (even though a million billion would only be a quadrillion, which is not only
# countable, but pertinant in terms of national debt).
print(" ".join([random.choice(leadingmagnitude),random.choice(magnitude)]))
print(" ".join([random.choice(leadinghundred),hundred[0],random.choice(trailing),random.choice(magnitude)]))
# NINE HUNDRED NINETY NINE MAGNITUDE
magnitudes = random.sample(range(4),random.randint(1,4))
magnitudes.sort(reverse=True)
text = []
for m in magnitudes:
	text.extend([random.choice(leadinghundred),hundred[0],random.choice(trailing),magnitude[m]])
text.extend([random.choice(leadinghundred),hundred[0],random.choice(trailing)])
print(" ".join(text))

begin = {}
for number in leadingmagnitude:
	number = number.split()[0]
	begin[number]=1
for number in leadinghundred:
	number = number.split()[0]
	begin[number]=1
for number in leadinglasthundred:
	number = number.split()[0]
	begin[number]=1

print("Begin keys")
print(begin.keys())
print(len(begin.keys()))

end = {}
for number in trailing:
	number = number.split()[-1]
	end[number] = 1

print("End keys")
print(end.keys())
print(len(end.keys()))

begin_or_end = begin.copy()
for number in end.keys():
	begin_or_end[number] = 1

print("Begin or end keys")
print(begin_or_end.keys())
print(len(begin_or_end.keys()))
