class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
#        super(Child, self).altered()
#        print "CHILD, AFTER PARENT altered()"

class GrandChild(Child):

    def altered(self):
        print "GRANDCHILD, BEFORE Child altered()"
        super(Child, self).altered()
        print "GRANDCHILD, AFTER CHILD altered()"

#ad = Parent()
son = Child()
grandson = GrandChild()

#dad.altered()
#son.altered()
grandson.altered()

