# GFpy

> gfpy is similary of [gf](https://github.com/tomnomnom/gf), but is in python and it's possible to use gf-partners in another locals.

```
python3 gfpy.py -f parameters.txt -p xss.json | sort -u 

http://www.example.com/blog/?p=FUZZ
http://www.example.com.br/blog/?s=FUZZ
http://www.example.com.br/p/media?page=FUZZ

# OR

echo "example.com" | gau | python3 gfpy.py -p xss.json| sort -u

http://www.example.com/blog/?p=FUZZ
http://www.example.com.br/blog/?s=FUZZ
http://www.example.com.br/p/media?page=FUZZ 
```

### Recomendetion gf-patterns
[Gf-Patterns V 1.9](https://github.com/1ndianl33t/Gf-Patterns)
[top25-parameter](https://github.com/lutfumertceylan/top25-parameter)