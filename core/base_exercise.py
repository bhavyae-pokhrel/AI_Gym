
#! abstract method that declared but not implemented in a parent class & It acts like a rule/contract that child classes must implement.

from abc import ABC, abstractmethod 
# landmarks = [{"id": 0, "name": "NOSE", "x": 0.50, "y": 0.10, "z": -0.10, "visibility": 0.99},....33 element]  
# # 0–10: Face, 11–16: Upper body, 17–22: Hands,23–28: Lower body (MOST IMPORTANT for squats), 29–32: Feet

#^ The dot product(2D) is: A⋅B = ∣A∣∣B∣cosθ=A⋅B = Ax.​Bx + Ay.By + Az.Bz the magnitude (length) is: ∣A∣=sqrt(Ax^2+Ay^2+Az^2)
# we have 3 points in 3D(hips,knee,ankle) as vector A,B,C u= A-B & v= C-B
#^ 0= cos-1(A.B/|A|*|B|)  if A.B/|A|*|B|=-1 -> degree = 180  && A.B/|A|*|B|=0 -> degree = 90 &&  A.B/|A|*|B|=1 -> degree = 0


import math 
from abc import ABC, abstractmethod


class BaseExercise(ABC):
    def __init__(self):
        self.reps = 0
        self.stage = None

    def calculate_angle(self, a, b, c):
        ax, ay = a[0] - b[0], a[1] - b[1]
        cx, cy = c[0] - b[0], c[1] - b[1]

        dot = ax * cx + ay * cy

        mag_a = math.sqrt(ax ** 2 + ay ** 2)
        mag_c = math.sqrt(cx ** 2 + cy ** 2)

        if mag_a * mag_c == 0:
            return 0.0

        cos_angle = max(-1.0, min(1.0, dot / (mag_a * mag_c)))

        return math.degrees(math.acos(cos_angle))

    def get_point(self, landmarks, idx):
        p = landmarks[idx]

        return (p.x, p.y)

    @abstractmethod
    def process(self, landmarks):
        pass

    @abstractmethod
    def reset(self):
        pass