from textual.containers import VerticalScroll, Container
from textual.widgets import Header, Footer, Label, Input, TextArea, Button


class MainUI(VerticalScroll):
	def compose(self):
		yield Header(show_clock=True)
		yield Footer()

		with Container():
			yield Label("Document Path:", shrink=True)
			yield Input(id="file", placeholder="Enter the location to your document file here...")

		with Container(id="prompt_container"):
			yield Label("Custom Prompt:", shrink=True)
			yield TextArea(id="prompt", placeholder="Enter your custom AI prompt here...")

		with Container(id="button_container"):
			yield Button("Generate", id="submit_btn", variant="primary")

		with Container():
			yield Label("Generated Summary:", shrink=True)
			yield TextArea(id="summary", placeholder="The generated summary will appear here...", disabled=True)
