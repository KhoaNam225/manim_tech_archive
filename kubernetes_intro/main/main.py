from manim import (
    GrowFromCenter,
    Scene,
    Circle,
    Square,
    Create,
    Transform,
    FadeOut,
    SVGMobject,
)
from manim import PINK, RIGHT, TAU


class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount
        square.scale(0.5)

        docker_logo = SVGMobject(file_name="../assets/docker-logo.svg")
        server_icon = SVGMobject(file_name="../assets/server-icon.svg")

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
        self.play(GrowFromCenter(docker_logo))
        self.play(FadeOut(docker_logo))
        self.play(GrowFromCenter(server_icon))
