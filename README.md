# mgraphql
Python library link with graphql

------------------------------------------------

```from mgraphql import Mgraphql```

```query ="""
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""
```

``` variables = {

your variables

type Python Dictionary 

}
```

```
url = 'https://api.github.com/graphql'
```

# token default none
```
mgraph = Mgraphql(url,token)
```

```
query =mgraph.query(query)
```

```
mutation =mgraph.mutation(query,variables)
```

```
print(mutation)
#print(query)
```
