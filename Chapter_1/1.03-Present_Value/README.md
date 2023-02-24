The present value (PV) of some 
future value (FV) under continuous
compounding for times that are 
delta_t years apart with a required 
rate of return r is:
PV = FV * e^(-r*delta_t)

Try out the demo by calculating the 
present value of a million dollars 
in 30 years with a required rate of 
return of 10% by running the following code:
```
python demo.py --future_val=1000000 --rate=.1 --delta_t=30
```