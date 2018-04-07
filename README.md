# Bowling Kata  
  
Python-coded solution for [Bowling Kata](http://codingdojo.org/kata/Bowling/).
  
The idea behind this solution is to loop over the sequence of tries in a complete bowling game while computing the overall score achieved so far each try. After having processed the last try in the sequence, we'll end up with the total score for the whole game. The method this solution uses is to keep in a table the amount of bonus points which have to be computed at each try. Bonus points are allocated when a "strike" or a "spare" occur. According to bowling rules, a "strike" gets bonus points for the next two throws, while a "spare" gets bonus points for the next throw.
  
## Usage  
  
### Commands:  
  
```  
$ python test_bowling.py  
```
