#!/usr/bin/env python3

import manim as mn

class IlluminaWorkflow(mn.Scene):
    def construct(self):
        # Define the title of the animation
        title = mn.Text("Illumina Sequencing Workflow").scale(0.8)
        self.play(mn.FadeIn(title))
        self.play(mn.FadeOut(title), mn.Write(mn.Text("Raw Reads")))
        self.wait(2)

        # Step 1: Raw Reads Generation
        raw_reads = mn.Circle(color=mn.YELLOW).scale(0.5)
        self.play(mn.Create(raw_reads))
        self.wait(2)  # Wait for the circle to represent raw reads

        # Transition to next step
        self.play(mn.FadeOut(raw_reads), mn.Write(mn.Text("Aligning Reads")))

        # Step 2: Aligning Reads
        aligning_reads = mn.Rectangle(color=mn.BLUE).scale(0.6)
        self.play(mn.Create(aligning_reads))
        self.wait(2)  # Wait for the rectangle to represent aligned reads

        # Transition to final step
        self.play(mn.FadeOut(aligning_reads), mn.Write(mn.Text("Variant Calling")))

        # Step 3: Variant Calling
        variant_calling = mn.Square(color=mn.GREEN).scale(0.7)
        self.play(mn.Create(variant_calling))
        self.wait(2)  # Wait for the square to represent variant calling

        # Finalize the animation
        self.play(mn.FadeOut(variant_calling), mn.Uncreate(title))

# Run the animation
# if __name__ == "__main__":
#     manim -pql alignment.py IlluminaWorkflow

