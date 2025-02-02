from manim import * 
import numpy as np


#def fun_color(x):
    #colors = [RED, BLUE, YELLOW, ORANGE, PURPLE, TEAL, PINK]
    #for i in range(len(x)):
        #x[i].set_color(colors[i])
    #return (x)

#crirar a classe para animação
class waves(ThreeDScene): #cena 3D
    def construct(self): #construção da cena
        #posição da camera
        self.set_camera_orientation(zoom=0.6, phi=-30 * DEGREES, theta=-80 * DEGREES)
        a = ThreeDAxes(x_range=[0, 25], y_range=[-6, 6]).rotate(60*DEGREES, about_point= ORIGIN, axis=UP)
        t = ValueTracker(0)
        
	
        #x_lab = a.get_x_axis_label("X axis")
        #y_lab = a.get_y_axis_label("Y axis")
        #z_lab = a.get_z_axis_label("Z axis")

        #self.add(x_lab, y_lab, z_lab)

        #always_redraw para ficar sempre se reconstruindo o grafico
        graph = always_redraw(lambda: a.plot(lambda x: 
                       np.sin(x+ t.get_value())
                         + np.sin(x*0.737+ t.get_value()) 
                         + np.cos(x/2+ t.get_value())
                         + np.sin(x/0.69+ t.get_value())
                         + np.cos(3*x+ t.get_value())
                         + np.sin(2*x+ t.get_value())
                         + np.sin(x/2 + t.get_value()),
                       color=WHITE))
        
        #s1 = always_redraw(lambda:a.plot(lambda x: np.sin(x + t.get_value()), color=RED).shift(OUT*2))
        #s2 = always_redraw(lambda:a.plot(lambda x: np.sin(x*0.737 + t.get_value()), color=BLUE).shift(OUT*1))
        #s3 = always_redraw(lambda:a.plot(lambda x: np.cos(x/2 + t.get_value()), color=YELLOW).shift(OUT*-1))
        #s4 = always_redraw(lambda:a.plot(lambda x: np.sin(x/0.69 + t.get_value()), color=ORANGE).shift(OUT*-2))
        #s5 = always_redraw(lambda:a.plot(lambda x: np.cos(3*x + t.get_value()), color=PURPLE).shift(OUT*3))
        #s6 = always_redraw(lambda:a.plot(lambda x: np.sin(2*x + t.get_value()), color=TEAL).shift(OUT*-3))
        #s7 = always_redraw(lambda:a.plot(lambda x: np.sin(x/2 + t.get_value()), color=PINK))

        #g = VGroup(s1, s2, s3, s4, s5, s6, s7)

        #fun_color(g)

        wave_colors = [RED, BLUE, YELLOW, ORANGE, PURPLE, TEAL, PINK]
        wave_funcs = [
            lambda x: np.sin(x + t.get_value()),
            lambda x: np.sin(x * 0.737 + t.get_value()),
            lambda x: np.cos(x / 2 + t.get_value()),
            lambda x: np.sin(x / 0.69 + t.get_value()),
            lambda x: np.cos(3 * x + t.get_value()),
            lambda x: np.sin(2 * x + t.get_value()),
            lambda x: np.sin(x / 2 + t.get_value())
        ]

        wave_shift = [OUT * 2, OUT, OUT * -1, OUT * -2, OUT * 3, OUT * -3, ORIGIN]
        waves = VGroup(*[
            always_redraw(lambda f=wave_funcs[i], c=wave_colors[i], s=wave_shift[i]: 
                          a.plot(f, color=c).shift(s))
            for i in range(len(wave_funcs))
        ])

        self.add(graph,a)#adiciona o grafico e o plano 
        #em teoria é para mexer o priemiro grafico branco
        self.play(t.animate.set_value(-40), run_time=10, rate_func = rate_functions.linear)
        #troca o grafico branco pelos graficos separados
        self.play(ReplacementTransform(graph, waves))
        self.play(t.animate.set_value(-40), run_time = 10, rate_func = rate_functions.ease_in_sine)
        self.wait(3)


############################################################AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH