from manim import *

class ContinuousMotion(Scene):
    def construct (self):
        func = lambda pos: np.sin(pos[0] / 2) * UR +  np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=50)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.0)
        self.wait(10)
        ##self.wait(stream_lines.duration.virtual_time / stream_lines.flow_speed)