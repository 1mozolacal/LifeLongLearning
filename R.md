# R

### Binomial

```r
#size = n
#prob = p
# dbinom(x, size=n, prob=p)
dbinom(0, size=12, prob=0.2) + dbinom(1, size=12, prob=0.2) + dbinom(2, size=12, prob=0.2)
```

### Chi-squared Distribution

```r

# Find x of given percentile
# Function signature
# qchisq(p, df, ncp = 0, lower.tail = TRUE, log.p = FALSE)
qchisq( 0.95, df=7)#example 95 percentile and 7 degrees of freedom

# With x determind cumative probability. ie P(X<x)= ...
#signature
# pchisq(q, df, ncp = 0, lower.tail = TRUE, log.p = FALSE)

pchisq(14.06714, df=7, ncp = 0, lower.tail = TRUE, log.p = FALSE)
```

### Standard Distribution

```r
# Used to find the probability from negative infinity to xValue
# pnorm(xValue,mean= mu, df = sigma)

pnorm(0,mean=0,df = 1)#standard normal dis
# result -> 0.5
```
