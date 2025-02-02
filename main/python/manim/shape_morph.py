from manim import *

class ShapeMorph(Scene):
    def construct(self):
        # Create the initial square
        square = Square(side_length=2, color=BLUE)

        # Create the rectangle
        rectangle = Rectangle(width=4, height=1.5, color=GREEN)
        # Position the rectangle where the square was.
        rectangle.move_to(square.get_center())

        # Create the circle
        circle = Circle(radius=1.5, color=RED)
        # Position the circle where the square was.
        circle.move_to(square.get_center())
        
        # Show the initial square
        self.play(Create(square))
        self.wait(0.5)

        # Morph the square into the rectangle
        self.play(Transform(square, rectangle), run_time=2)
        self.wait(0.5)
        
        # Morph the rectangle into the circle
        self.play(Transform(square, circle), run_time=2)
        self.wait(0.5)

        # Display the final circle
        self.play(FadeIn(circle))
        self.wait(1)