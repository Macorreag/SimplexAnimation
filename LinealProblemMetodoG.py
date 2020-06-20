#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

##Todos los elementos del video salen en orden cronológico
class Title (Scene):
	CONFIG ={
	"camera_config" : {"background_color":"#070707"}
	}
	def construct(self):
		#PARTE 1: Titulo
		#1.1 Elementos de texto
		title = TextMobject(r"{\huge{Solución Gráfica de un PPL}")
		subtitle = TextMobject(r"\small{A. Barreto, M. Correa, K. Herrera, M. Martinez, D. Moreno}")
		t1 = TextMobject(r"\textsc{Universidad Nacional de Colombia}")

		#1.2 Posicionamiento
		subtitle.next_to(title,DOWN)
		t1.next_to(subtitle,DOWN)

		#1.3 Animación
		self.play(Write(title),Write(subtitle),Write(t1))
		self.wait(3)
		self.play(FadeOut(title),FadeOut(subtitle),FadeOut(t1))
		self.wait()

class MainFrame (GraphScene):
	CONFIG ={
		"camera_config" : {"background_color":"#070707"},
		"y_max" : 100,
		"y_min" : 0,
		"x_max" : 100,
 		"x_min" : 0,
		"x_axis_width": 4,
		"y_axis_height": 4,
		"y_tick_frequency": 20,
		"x_tick_frequency": 20,
		"axes_color" : BLUE,
		"x_axis_label" : "$x_{1}$",
		"y_axis_label" : "$x_{2}$",
	}
	def construct(self):
		#Problema de programación lineal
		fo = TextMobject(r"\small{Maximizar $3x_{1} + 2x_{2}$}")
		sa = TextMobject(r"\small{Sujeto a:}")
		r1 = TextMobject(r"\small{$2x_{1} + x_{2} \leq 100$}")
		r2 = TextMobject(r"\small{$x_{1} + x_{2} \leq 80$}")
		r3 = TextMobject(r"\small{$x_{1}, x_{2} \geq 0$}")

		fo.to_corner(UL)
		sa.next_to(fo,DOWN)
		sa.to_edge(LEFT)
		r1.next_to(sa,DOWN)
		r1.to_edge(LEFT,buff = 1.5)
		r2.next_to(r1,DOWN)
		r2.to_edge(LEFT,buff = 1.5)
		r3.next_to(r2,DOWN,buff=0.9)
		r3.to_edge(LEFT)
		#Escritura del PPL
		self.play(Write(fo),Write(sa),Write(r1),Write(r2),Write(r3))
		self.wait()

		#Ploteo
		self.graph_origin =  DOWN +  RIGHT
		self.setup_axes()
		self.wait()
		
		#Graficar las restricciones
		p1 = TextMobject(r"\small{1. Graficar las restricciones}")
		p2 = TextMobject(r"\small{2. Graficar la funci\'on objetivo}")
		
		p1.next_to(r3,DOWN,buff=1.5)
		p1.to_edge(LEFT)
		p2.next_to(r3,DOWN,buff=1.5)
		p2.to_edge(LEFT)

		self.play(Write(p1))
		self.wait()
		
		#Para la primera restricción
		r1_a1 = TextMobject(r"\small{$2x_{1} + x_{2} = 100$}")
		r1_a2 = TextMobject(r"\small{$2x_{1} = 100$}")
		r1_a3 = TextMobject(r"\small{$x_{1} = 50$}")
		r1_a4 = TextMobject(r"\small{$x_{2} = 100$}")
		
		r1_a1.next_to(sa,DOWN)
		r1_a1.to_edge(LEFT,buff=1.5)
		r1_a1.set_color(BLUE)
		r1_a2.next_to(sa,DOWN)
		r1_a2.to_edge(LEFT,buff=1.5)
		r1_a2.set_color(BLUE)
		r1_a3.next_to(sa,DOWN)
		r1_a3.to_edge(LEFT,buff=1.5)
		r1_a3.set_color(BLUE)
		r1_a4.next_to(sa,DOWN)
		r1_a4.to_edge(LEFT,buff=1.5)
		r1_a4.set_color(BLUE)

		self.play(Transform(r1,r1_a1))
		self.play(Transform(r1,r1_a2))
		self.play(Transform(r1,r1_a3))
		self.wait()
		self.play(Transform(r1,r1_a1))
		self.play(Transform(r1,r1_a4))
		self.wait()
		self.play(Transform(r1,r1_a1))
		
		line1 = self.get_graph(lambda x : 100 - 2*x, color = BLUE)
		self.play(ShowCreation(line1),run_time=2)
		self.wait()

		#Para la segunda restricción
		r2_a1 = TextMobject(r"\small{$x_{1} + x_{2} = 80$}")
		r2_a2 = TextMobject(r"\small{$x_{1} = 80$}")
		r2_a3 = TextMobject(r"\small{$x_{2} = 80$}")
		
		r2_a1.next_to(r1,DOWN)
		r2_a1.to_edge(LEFT,buff=1.5)
		r2_a1.set_color(GREEN)
		r2_a2.next_to(r1,DOWN)
		r2_a2.to_edge(LEFT,buff=1.5)
		r2_a2.set_color(GREEN)
		r2_a3.next_to(r1,DOWN)
		r2_a3.to_edge(LEFT,buff=1.5)
		r2_a3.set_color(GREEN)

		self.play(Transform(r2,r2_a1))
		self.play(Transform(r2,r2_a2))
		self.wait()
		self.play(Transform(r2,r2_a1))
		self.play(Transform(r2,r2_a3))
		self.wait()
		self.play(Transform(r2,r2_a1))
		
		line2 = self.get_graph(lambda x : 80 - x, color = GREEN)
		area = self.get_area(line1,line2,0)
		self.play(ShowCreation(line2),run_time=2)
		self.wait()

	def setup_axes(self):
		GraphScene.setup_axes(self)
		init_label_x = 20
		end_label_x = 100
		step_x = 20
		init_label_y = 20
		end_label_y = 100
		step_y = 20
		self.x_axis.label_direction = DOWN
		self.y_axis.label_direction = LEFT
		self.x_axis.add_numbers(*range(init_label_x,end_label_x+step_x, step_x))
		self.y_axis.add_numbers(*range(init_label_y,end_label_y+step_y, step_y))
		self.play(ShowCreation(self.x_axis), ShowCreation(self.y_axis))
