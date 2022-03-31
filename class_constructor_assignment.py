
class traffic:
    attr1  ="Stop!"
    attr2 = "Ready to go"
    attr3 = "Go"
    def slow_down(self):
      return self.attr1
    def hold_on(self):
        return self.attr2
    def move_on(self):
        return self.attr3
test = traffic()

# print(test.attr3)
# print(test.slow())
# print(test.colour_3)

col = input("enter colour:")
 
if col == "red":
    a = test.slow_down()
    print(a)
elif col == "yellow":
    b = test.hold_on()
    print(b)
elif col == "green":
    c = test.move_on()
    print(c)