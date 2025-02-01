from cloup import file_path
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    GREY_A,
    WHITE,
    FadeIn,
    Rectangle,
    DoubleArrow,
    GrowFromCenter,
    RoundedRectangle,
    SVGMobject,
    ImageMobject,
    Group,
    Text,
    TypeWithCursor,
    Create,
    Scene,
)
from manim_slides.slide import Slide

CURSOR = Rectangle(
    color=GREY_A,
    fill_color=GREY_A,
    fill_opacity=1.0,
    height=1,
    width=0.2,
)


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
            CURSOR.copy().scale(0.8).move_to(question_text[0])
        )  # Position the cursor
        self.add(question_text)
        self.play(TypeWithCursor(text=question_text, cursor=cursor, time_per_char=0.05))
        self.next_slide()


class EvolutionOfDeploymentSlide(Slide):
    def construct(self):
        header_text = Text(text="The Evolution Of Software Deployment")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        icons_group = Group()

        server_icon = SVGMobject(file_name="../assets/server-icon.svg")
        server_text = Text(text="Bare-Metal").scale(0.5)
        server_icon.add(server_text.next_to(server_icon, DOWN, buff=0.5))

        vm_icon = SVGMobject(
            file_name="../assets/virtual-machine-icon.svg",
        )
        vm_text = Text(text="Virtual Machines").scale(0.5)
        vm_icon.add(vm_text.next_to(vm_icon, DOWN, buff=0.5))
        vm_icon.scale_to_fit_height(server_icon.height)
        vm_icon.next_to(server_icon, RIGHT, buff=2)

        docker_icon = SVGMobject(
            file_name="../assets/container-icon.svg",
        )
        docker_text = Text(text="Containers").scale(0.5)
        docker_icon.add(docker_text.next_to(docker_icon, DOWN, buff=0.5))
        docker_icon.scale_to_fit_height(server_icon.height)
        docker_icon.next_to(vm_icon, RIGHT, buff=2)

        icons_group.add(server_icon, vm_icon, docker_icon)
        icons_group.center()

        self.play(FadeIn(server_icon))

        self.next_slide()
        self.play(FadeIn(vm_icon))

        self.next_slide()
        self.play(FadeIn(docker_icon))


class BareMetalDeployment(Slide):
    def construct(self):
        header_text = Text(text="Bare-Metal Deployment")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        server_border = RoundedRectangle(
            width=13, height=6, stroke_width=1, corner_radius=0.1
        )
        server_border.next_to(header_text, DOWN, buff=0.5)

        server_icon = SVGMobject(file_name="../assets/server-icon.svg").scale(0.7)
        server_icon.move_to(server_border.get_corner(UP + RIGHT))

        dependencies_header = Text(text="Dependencies").scale(0.5)
        dependencies_border = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        dependencies_border.align_to(server_border, direction=UP + LEFT)
        dependencies_border.shift(LEFT * -0.5, UP * -0.5)
        dependencies_header.next_to(dependencies_border.get_top(), DOWN, buff=0.2)

        application_header = Text(text="Application").scale(0.5)
        application_border = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        application_border.align_to(server_border, direction=UP + RIGHT)
        application_border.shift(RIGHT * -0.7, UP * -0.5)
        application_header.next_to(application_border.get_top(), DOWN, buff=0.2)

        python_icon = ImageMobject(filename_or_array="../assets/python-logo.png")
        nginx_icon = SVGMobject(file_name="../assets/nginx-logo.svg")
        iis_icon = SVGMobject(file_name="../assets/iis-logo.svg")

        python_icon.scale(0.4).align_to(dependencies_border, direction=UP + LEFT)
        python_icon.shift(DOWN * 1).shift(RIGHT * 0.5)

        nginx_icon.scale(0.7).align_to(dependencies_border, direction=UP + RIGHT)
        nginx_icon.shift(DOWN * 1.5).shift(LEFT * 0.5)

        iis_icon.add_background_rectangle(color=WHITE, opacity=1, buff=0.5)
        iis_icon.scale(0.5).align_to(dependencies_border, direction=DOWN + LEFT)
        iis_icon.shift(UP * 0.2).shift(RIGHT * 0.5)

        application_code = SVGMobject(file_name="../assets/code-icon.svg")
        application_code.move_to(application_border.get_center())

        self.play(Create(server_border), GrowFromCenter(server_icon))

        self.next_slide()
        self.play(Create(dependencies_border), FadeIn(dependencies_header))

        self.next_slide()
        self.play(
            GrowFromCenter(python_icon),
            GrowFromCenter(nginx_icon),
            GrowFromCenter(iis_icon),
        )

        self.next_slide()
        self.play(Create(application_border), FadeIn(application_header))

        self.next_slide()
        self.play(GrowFromCenter(application_code))
