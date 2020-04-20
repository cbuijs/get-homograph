# get-homograph
Get all possible homograph punycoded domains of a particular domain

`cat domain.list | ./get-homograph.py`

Outputs two columns, the punycoded homograph and the original domain.

Test:
```
root@boohoo:/opt/get-homograph# echo "test.com" | ./get-homograph.py 
test.com	test.com
xn--tst-rdd.com	test.com
```

Based on Homoglyphs by Life4:
https://github.com/life4/homoglyphs

