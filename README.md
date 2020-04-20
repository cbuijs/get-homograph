# get-homograph
Get all possible homograph punycoded domains of a particular domain

`cat domain.list | ./get-homograph.py`

Test:
```
echo "test.com" | ./get-homograph.py 
test.com	test.com
xn--tst-rdd.com	test.com
```

Based on Homoglyphs by Life4:
https://github.com/life4/homoglyphs

