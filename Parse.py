import nltk
v = """
angus => a
bertie => b
brutus => r
olive => o
cyril => c
man => {a}
boy => {b}
girl => {o}
dog => {c}
cat => {r}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
hear => {(a, r)}
"""
val = nltk.Valuation.fromstring(v)
g = nltk.Assignment(val.domain)
m = nltk.Model(val.domain, val)
sent = 'Angus hears a cat'
grammar_file = 'simple-sem.fcfg'
results = nltk.evaluate_sents([sent], grammar_file, m, g)[0]
for (syntree, semrep, value) in results:
    print(semrep)
    print(value)
