# un estudio de TAD's implementando los TAD

## Pila

Usamos como tipo base el tipo -class- list de python
Aporta mucho trabajo hecho. (esto será un wrapper y poco mas)

## diseño

    datos: la pila es generica. (apila cualquier dato,, tipo: object)
    operaciones:

- [x] push()
- [x] pop()
- [x] h()    // altura
- [x] drop() // descarte
- [x] esVacia()
- [x] esLlena()

## Cola

Nos inspiramos en [este material](https://www.geeksforgeeks.org/queue-in-python/)

>List is a Python’s built-in data structure that can be used as a queue. Instead of `enqueue()` and `dequeue()`, `append()` and `pop()` function is used. However, lists are **quite slow** for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one: a task in O(n) time.

v0: sin usar `collections.deque`

- [x] enqueue() // append
- [x] dequeue() //
- [] l()    // length
- [] drop() // descarte
- [] esVacia()
- [] esLlena()
