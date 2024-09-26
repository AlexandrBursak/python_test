import re

# pattern = re.compile(
# 	"((year|month|day|hour|minute|weeks|yearday|weekday)[s]?=(\+|-)?"
# 	"([0-9]{1,4}|(MO|TU|WE|TH|FR|SA|SU)+\((\+|-)?[1-7]{1}\)))"
# )
# request = 'year=1991,months=+1'

# if re.match(pattern, request):
# 	print('valid')
# else:
# 	print('invalid');


pattern = re.compile("snowflake-oauth-5fcf7a254cfb3d550c0521e4-(.*)")

request = 'snowflake-oauth-5fcf7a254cfb3d550c0521e4-2020-12-10.07-40-31.pm'

if re.match(pattern, request):
	print('valid')
else:
	print('invalid');