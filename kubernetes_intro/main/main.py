from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    GREY_A,
    Rectangle,
    DoubleArrow,
    GrowFromCenter,
    Scene,
    SVGMobject,
    ImageMobject,
    Group,
    Text,
    TypeWithCursor,
)
from manim_slides.slide import Slide


class ThreeLayerAppScene(Slide):
    def construct(self):
        # Initial scene with 3-layer application explain
        three_layer_app_group = Group()
        angular_icon = SVGMobject(file_name="../assets/angular-logo.svg")
        angular_icon.add(
            Text(text="Angular Front-end").scale(0.5).next_to(angular_icon, DOWN)
        )
        self.play(GrowFromCenter(angular_icon))
        three_layer_app_group.add(angular_icon)
        self.next_slide()

        first_arrow = DoubleArrow(tip_length=0.2, buff=0)
        self.add(first_arrow)
        self.play(
            GrowFromCenter(first_arrow.center()),
            angular_icon.animate.next_to(first_arrow, LEFT),
        )
        three_layer_app_group.add(first_arrow)

        python_icon = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon.scale(0.5)
        python_icon.add(Text(text="REST API").scale(0.5).next_to(python_icon, DOWN))
        self.play(
            GrowFromCenter(python_icon),
            three_layer_app_group.animate.next_to(python_icon, LEFT),
        )
        three_layer_app_group.add(python_icon)
        self.next_slide()

        second_arrow = DoubleArrow(tip_length=0.2, buff=0)
        self.add(second_arrow)
        second_arrow.next_to(three_layer_app_group, RIGHT)
        self.play(
            GrowFromCenter(second_arrow),
        )
        three_layer_app_group.add(second_arrow)

        postgresql_icon = SVGMobject(file_name="../assets/postgresql-logo.svg")
        postgresql_icon.add(
            Text(text="SQL Database").scale(0.5).next_to(postgresql_icon, DOWN)
        )
        self.add(postgresql_icon)
        postgresql_icon.next_to(three_layer_app_group, RIGHT)
        self.play(GrowFromCenter(postgresql_icon))
        three_layer_app_group.add(postgresql_icon)
        self.next_slide()

        question_text = Text(text="How do we deploy this?")
        question_text.scale(0.8).next_to(three_layer_app_group, UP, buff=1)
        cursor = (
            Rectangle(
                color=GREY_A,
                fill_color=GREY_A,
                fill_opacity=1.0,
                height=1,
                width=0.2,
            )
            .scale(0.8)
            .move_to(question_text[0])
        )  # Position the cursor
        self.add(question_text)
        self.play(TypeWithCursor(text=question_text, cursor=cursor))
        self.next_slide()
        

class EvolutionOfDeploymentSlide(Slide):
    def construct(self):
        
