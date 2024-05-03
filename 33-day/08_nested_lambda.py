# 08_nested_lambda.py
# Nested lambda functions

mul = lambda x: lambda y: x * y

double = mul(2)
triple = mul(3)

print("Double 10:", double(10))
print("Triple 10:", triple(10))
