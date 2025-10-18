class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Foot:
    def __init__(self):
        pass

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self):
        self.head = Head()
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)
        self.right_foot = Foot()
        self.left_foot = Foot()
        self.right_leg = Leg(self.right_foot)
        self.left_leg = Leg(self.left_foot)
        self.torso = Torso(
            self.head,
            self.right_arm,
            self.left_arm,
            self.right_leg,
            self.left_leg
        )

if __name__ == "__main__":
    juan = Human()
    print(juan.torso.head)
    print(juan.torso.right_arm.hand)
    print(juan.torso.left_leg.foot)

