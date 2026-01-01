import os

from textual.app import App, ComposeResult, on
from textual.widgets import Input, TextArea, Button

from frontend.ui.ui import MainUI


from backend.ds import generate_summary


class DocSummary(App):
	CSS_PATH = "styles/styles.tcss"

	@staticmethod
	def compose(self) -> ComposeResult:
		yield MainUI()

	@on(Button.Pressed, "#submit_btn")
	def on_submit(self):
		file = self.query_one("#file", Input).value.strip()
		ext = os.path.splitext(file)[1].lower()
		supported_extensions = {".docx", ".pdf", ".txt", ".rtf", ".odt", ".html", ".ppt", ".pptx"}
		if ext not in supported_extensions:
			self.notify(f"Unsupported file type {ext}!\n\nSupported types:\n.docx, .pdf, .txt, .rtf, .odt, .html, .ppt, .pptx", title="Error", severity="error")
			return

		prompt = self.query_one("#prompt", TextArea).text.strip()

		self.notify(f"file:\n{file}\n\nprompt:\n{prompt}")

		summary = generate_summary(file, prompt)
		self.query_one("#summary", TextArea).text = summary

		if summary:
			self.query_one("#submit_btn", Button).label = "Regenerate"
		else:
			self.query_one("#submit_btn", Button).label = "Generate"
