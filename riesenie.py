# 7. zadanie: repository
# autor: Adam Lopaška
# datum: 4.5.2022

class Repository:
    class Node:
        def __init__(self, value=None):    # vrchol prefixového stromu
            self.value = value
            self.child = None    # spájaný zoznam typu Child - spájaný zoznam podstromov

    class Child:
        def __init__(self, char, node=None, next=None):
            self.char = char
            self.node = node     # podstrom typu Node
            self.next = next     # nasledovný prvok spájaného zoznamu

    def __init__(self):
        self.root = None         # prázdny strom
        self.len = 0
        self.len2 = 0
    def __setitem__(self, key, value):
        if self.root is None:
            self.root = self.Node()
            self.len = 1
        
        self.search(self.root,key,value)

    class myNone:
        def __init__(self):
            self.val = None

    def search(self,root,key,value):
        if len(key) == 0:
            if value is None:
                value = self.myNone()
            if root.value is None or isinstance(root.value, self.myNone):
                self.len2 += 1
            root.value = value
            return
        letter = key[0]

        if root.child is None:
            root.child = self.Child(letter,self.Node())
            self.len+=1
            self.search(root.child.node,key[1:],value)
            return

        tempChild = root.child
        while tempChild is not None:
            if tempChild.char == letter:
                self.search(tempChild.node,key[1:],value)
                return
            if tempChild.next is None:
                tempChild.next = self.Child(letter,self.Node())
                self.len+=1
                self.search(tempChild.next.node,key[1:],value)
                return 
            tempChild = tempChild.next

        

    def __getitem__(self, key):
        def search(root,key):
            if len(key) == 0:
                if root.value is None:
                    raise KeyError
                if isinstance(root.value,self.myNone):
                    return None 
                return root.value
            if root.child is None:
                raise KeyError
            letter = key[0]
            tempChild = root.child
            while tempChild is not None:
                if tempChild.char == letter:
                    return search(tempChild.node,key[1:])
                tempChild = tempChild.next
            raise KeyError
        if self.root is None:
            raise KeyError   
        return search(self.root,key)

    def __delitem__(self, key):
        def search(root,key):
            if len(key) == 0:
                if root.value is None or isinstance(root.value, self.myNone):
                    raise KeyError
                self.len2 -= 1
                root.value = None
                return
            if root.child is None:
                raise KeyError
            letter = key[0]
            tempChild = root.child
            while tempChild is not None:
                if tempChild.char == letter:
                    search(tempChild.node,key[1:])
                    return
                tempChild = tempChild.next
            raise KeyError
        if self.root is None:
            raise KeyError   
        return search(self.root,key)

    def node_count(self):
        return self.len

    def __len__(self):
        return self.len2 #len(list(self.__iter__()))

    def __iter__(self):
        stack = [(self.root,"")]
        while stack != []:
            node,word = stack.pop()
            if node.value is not None and not isinstance(node.value, self.myNone):
                yield word
            if node.child is None:
                continue
            tempChild = node.child
            while tempChild is not None:
                stack.append((tempChild.node,word+tempChild.char))
                tempChild = tempChild.next
            
if __name__ == '__main__':
    '''d = Repository()
    d['hjdgbfde'] = None
    d['cgdfbbaihd'] = None
    d['hg'] = None
    d['dadjc'] = None
    d['dh'] = None
    d['ficbjhc'] = None
    d['ggihfhhdij'] = None
    d['afff'] = None
    d['i'] = None
    d['ejc'] = None
    d['jehbbia'] = None
    d['dc'] = None
    d['e'] = None
    d['h'] = None
    d['cchfig'] = None
    d['iajbijbgd'] = None
    d['ijghg'] = None
    d['jdaaceijef'] = None
    d['he'] = None
    d['gggac'] = None
    d['def'] = None
    d['a'] = None
    d['gchjbcfg'] = None
    d['j'] = None
    d['ghabhcaa'] = None
    d['jcfbifdghb'] = None
    d['j'] = None '''
    d = Repository()
    d[""] = None
    print(len(d)) 
    #print(len(d),d.node_count())
    '''for w in 'mama ma emu a ema ma mamu'.split():
        try:
            m[w] = m[w] + 1
        except KeyError:
            m[w] = 1

    print(list(m), m.node_count(), len(m))
    ww = list(m)
    for w in ww:
        del m[w]
        print(w, m.node_count(), len(m))'''