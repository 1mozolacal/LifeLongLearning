# Stats

## Moment Generating Fucntions

<img src="https://miro.medium.com/max/700/1*gu6VljOvoa0Zc45h1aIgiQ.png" title="status" />
<img src="https://miro.medium.com/max/700/1*E_1m2aXh-4_mNxc-mUGyMA.png" title="status" />
This can be proven with taylor series
<img src="https://miro.medium.com/max/700/1*Q8nidMGltk6KdtWnsjJ-uw.png" title="status" />
<img src="https://miro.medium.com/max/700/1*lf5tHBdXNGlUL9ULbWl-_Q.png" title="status" />
<img src="https://miro.medium.com/max/700/1*B3mmdnwXKz20ipXQyUisHw.png" title="status" />

---

## Geometric distribution

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = q^{x-1}p" title="product rule" />
<br><img src="https://latex.codecogs.com/svg.latex?\Large&space;M_x(t) = \frac{pe^t}{1 - qe^t}" title="product rule" />

---

## Binomial Distribution

n number of trials that is either success or failure. Denoted by b(n,p) or B(n,p)

> Mean and Var <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu = np" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2 = np(1 - p)" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = { n \choose x} p^x (1 - p)^{n-x}" title="product rule" />

---

## Hypergeometric distribution

---

## Possion Distribution

---

## Percentile

Where P is the percentile. Example 0.25 would be the first quartile.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;P = \int_{-\infty}^{\pi_p} f(x) dx" title="product rule" />

---

## Exponential Distribution

> Mean and Var<br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu =  \theta" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2 =  \theta^2" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = \frac{1}{\theta}e^{-x/\theta}" title="product rule" /> where <img src="https://latex.codecogs.com/svg.latex?\theta = \frac{1}{\lambda}" title="product rule" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;M_x(t) = \frac{1}{1-\theta t" title="product rule" /> such that t < 1/theta

---

## Gamma Distribution

> gamma function<br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space; \Gamma (t) = \int_0^{\infty} y^{t-1} e^{-y} dy" title="product rule" /> <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Gamma(t) = (t-1)!" title="product rule" /> For positive t.

> Mean and Var <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu = \alpha \theta" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2 = \alpha \theta^2" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = \frac{1}{\gamma (\alpha ) \theta ^\alpha} x^{\alpha-1} e^{-x/\theta}" title="product rule" /><br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;M_x(x) = \frac{1}{ ( 1 - \theta t)^\alpha} " title="product rule" /> where t < 1/theta

---

## Chi-square

> Mean and Var <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu = r" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2 = 2r" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = \frac{1}{\gamma ( \frac{r}{2} ) 2 ^ \frac{r}{2}} x^{\frac{r}{2} -1} e^{-x/2}" title="product rule" /><br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;M_x(x) = \frac{1}{ ( 1 - 2 t)^\frac{r}{2}} " title="product rule" /> where t < 1/2

---

## Standard Distribution

> Mean and Var <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu = \mu" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2 = \sigma^2" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = \frac{1}{\sigma \sqrt{2\pi}} exp[ -1/2] " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;M_x(x) = e^{\mu t + \frac{\sigma^2 t^2}{2}} " title="product rule" />

---

## Lognormal Distribution

> Mean and Var <br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_x = e^{\mu + \frac{ \sigma^2}{2}}" title="product rule" /><br> > <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma^2_x = (e^{\sigma^2}-1)e^{2\mu+\sigma^2}" title="product rule" /><br>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x) = \frac{1}{\sigma x \sqrt{2\pi}} exp[ \frac{-1}{2} (\frac{\ln{x}- \mu}{\sigma})^2] " title="product rule" /> <br>

---

## Joint Probability

---

<img src="https://latex.codecogs.com/svg.latex?\Large&space; f(x,y) = P(X=x,Y=y) " title="product rule" /> <br>

## Marginal Functions (JP)

<img src="https://latex.codecogs.com/svg.latex?\Large&space; f(x)_{x} = P(X=x) = \sum_{y} P(X=x,Y=y) " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; f(x,y) = f(x)_{x} f(y)_{y} " title="product rule" />

> If independant<br>

## Covariance (JP)

<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = \sigma_{xy} = E[ (X-\mu_x) (Y-\mu_y)] " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = \sum_{x} \sum_{y} (x-\mu_x) (y-\mu_y) f(x,y)" title="product rule" />

> For discret

<br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = \int_{x} \int_{y} (x-\mu_x) (y-\mu_y) f(x,y)" title="product rule" />

> For continuous

<br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = E[XY] - \mu_x \mu_y " title="product rule" /> <br>

## Correlation

<img src="https://latex.codecogs.com/svg.latex?\Large&space; Corr(x,y) = P_{xy} = \frac{\sigma_{xy}}{\sigma_x\sigma_y} " title="product rule" /> <br>

### If independant (JP)

<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = Corr(x,y) = 0 " title="product rule" /> <br>

proof

<img src="https://latex.codecogs.com/svg.latex?\Large&space; E[XY] = \sum_x \sum_y xy f(x,y)" title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; E[XY] = \sum_x \sum_y xy f(x)_x f(y)_y" title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; E[XY] = \sum_x x f(x)_x \sum_y y f(y)_y" title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; E[XY] = \mu_y \mu_y " title="product rule" /> <br>
<br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = E[XY] - \mu_x \mu_y " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Cov(x,y) = \mu_x \mu_y - \mu_x \mu_y = 0" title="product rule" /> <br>
<br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Corr(x,y) = P_{xy} = \frac{\sigma_{xy}}{\sigma_x\sigma_y} " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; Corr(x,y) = P_{xy} = \frac{0}{\sigma_x\sigma_y}  = 0" title="product rule" /> <br>

## Conditional Probability (JP)

<img src="https://latex.codecogs.com/svg.latex?\Large&space; g(x|y) = \frac{f(x,y)}{f(y)_y} " title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; P(a<Y<b|x) = \sum_{a<y<b} g(y|x)" title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; E[u(Y)|X=x] = \sum_{y}u(y)  g(y|x)" title="product rule" /> <br>
<img src="https://latex.codecogs.com/svg.latex?\Large&space; \mu_{y|x} = E[Y|X=x] = \sum_{y} y  g(y|x)" title="product rule" /> <br>
