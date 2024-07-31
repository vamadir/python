PNL calculating (task in attach).
In addition to the task: I would like to draw attention to the fact that this is just a small excerpt of data, the source of which is unknown, and it requires preliminary verification.


Using “test_logs.csv” file:  
1. Calculate total gross PnL;  
2. Calculate total gross PnL over each security ID;  
3. Draw cumulative gross PnL.  
File structure:  
● currentTime – order time;  
● action – order status:  
o sent – the order is sent to the exchange;  
o placed – the exchange has accepted the order;  
o filled – the trade happened;  
o cancelling – the order is in the process of cancellation;  
o cancelled – the exchange has confirmed the order cancellation.  
● orderId – ID of a particular order;  
● orderProduct – security ID, that we want to trade;  
● orderSide – the side of our order (buy / sell);  
● tradePx – trade price;  
● tradeAmt – number of securities bought / sold.  